import torch

import numbers

from vel.rl.reinforcers.policy_gradient.policy_gradient_base import OptimizerPolicyGradientBase
from vel.api.metrics.averaging_metric import AveragingNamedMetric
from vel.schedules.constant import ConstantSchedule


class PpoPolicyGradient(OptimizerPolicyGradientBase):
    """ Proximal Policy Optimization - https://arxiv.org/abs/1707.06347 """
    def __init__(self, entropy_coefficient, value_coefficient, cliprange, max_grad_norm):
        super().__init__(max_grad_norm)

        self.entropy_coefficient = entropy_coefficient
        self.value_coefficient = value_coefficient

        if isinstance(cliprange, numbers.Number):
            self.cliprange = ConstantSchedule(cliprange)
        else:
            self.cliprange = cliprange

    def calculate_loss(self, batch_info, device, model, rollout):
        """ Calculate loss of the supplied rollout """
        observations = rollout['observations']
        discounted_rewards = rollout['discounted_rewards']
        advantages = rollout['advantages']
        rollout_values = rollout['values']
        rollout_actions = rollout['actions']
        rollout_neglogps = rollout['neglogps']

        # Select the cliprange
        current_cliprange = self.cliprange.value(batch_info['progress'])

        # Normalize the advantages?
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

        # PART 0 - model_evaluation
        eval_action_pd_params, eval_value_outputs = model(observations)

        # PART 1 - policy entropy
        policy_entropy = torch.mean(model.entropy(eval_action_pd_params))

        # PART 2 - value function
        value_output_clipped = rollout_values + torch.clamp(eval_value_outputs - rollout_values, -current_cliprange, current_cliprange)
        value_loss_part1 = (eval_value_outputs - discounted_rewards).pow(2)
        value_loss_part2 = (value_output_clipped - discounted_rewards).pow(2)
        value_loss = 0.5 * torch.mean(torch.max(value_loss_part1, value_loss_part2))

        # PART 3 - policy gradient loss
        eval_neglogps = model.neglogp(rollout_actions, eval_action_pd_params)
        ratio = torch.exp(rollout_neglogps - eval_neglogps)

        pg_loss_part1 = -advantages * ratio
        pg_loss_part2 = -advantages * torch.clamp(ratio, 1.0 - current_cliprange, 1.0 + current_cliprange)
        policy_gradient_loss = torch.mean(torch.max(pg_loss_part1, pg_loss_part2))

        loss_value = (
                policy_gradient_loss - self.entropy_coefficient * policy_entropy + self.value_coefficient * value_loss
        )

        with torch.no_grad():
            approx_kl_divergence = 0.5 * torch.mean((eval_neglogps - rollout_neglogps) ** 2)
            clip_fraction = torch.mean((torch.abs(ratio - 1.0) > current_cliprange).to(dtype=torch.float))

        batch_info['policy_gradient_data'].append({
            'policy_loss': policy_gradient_loss,
            'value_loss': value_loss,
            'policy_entropy': policy_entropy,
            'approx_kl_divergence': approx_kl_divergence,
            'clip_fraction': clip_fraction
        })

        return loss_value

    def metrics(self) -> list:
        """ List of metrics to track for this learning process """
        return [
            AveragingNamedMetric("policy_loss"),
            AveragingNamedMetric("value_loss"),
            AveragingNamedMetric("policy_entropy"),
            AveragingNamedMetric("approx_kl_divergence"),
            AveragingNamedMetric("clip_fraction"),
            AveragingNamedMetric("grad_norm")
        ]


def create(entropy_coefficient, value_coefficient, cliprange, max_grad_norm):
    return PpoPolicyGradient(entropy_coefficient, value_coefficient, cliprange, max_grad_norm)
