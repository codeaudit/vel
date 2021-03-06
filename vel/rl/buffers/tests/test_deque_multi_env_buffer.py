import gym
import nose.tools as t
import numpy as np
import numpy.testing as nt

from vel.exceptions import VelException
from vel.rl.buffers.deque_multi_env_buffer_backend import DequeMultiEnvBufferBackend


def get_half_filled_buffer():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 1), dtype=int)
    action_space = gym.spaces.Discrete(4)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(8).reshape((2, 2, 2, 1))

    for i in range(10):
        item = v1.copy()
        item[0] *= (i+1)
        item[1] *= 10 * (i+1)

        buffer.store_transition(item, 0, float(i)/2, False)

    return buffer


def get_filled_buffer():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 1), dtype=int)
    action_space = gym.spaces.Discrete(4)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(8).reshape((2, 2, 2, 1))

    for i in range(30):
        item = v1.copy()
        item[0] *= (i+1)
        item[1] *= 10 * (i+1)

        buffer.store_transition(item, 0, float(i)/2, False)

    return buffer


def get_filled_buffer1x1():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2,), dtype=int)
    action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(2,), dtype=float)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(4).reshape((2, 2))
    a1 = np.arange(4).reshape((2, 2))

    for i in range(30):
        item = v1.copy()
        item[:, 0] *= (i+1)
        item[:, 1] *= 10 * (i+1)

        buffer.store_transition(item, a1 * i, float(i)/2, False)

    return buffer


def get_filled_buffer2x2():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2), dtype=int)
    action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(2, 2), dtype=float)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(8).reshape((2, 2, 2))
    a1 = np.arange(8).reshape((2, 2, 2))

    for i in range(30):
        item = v1.copy()
        item[:, 0] *= (i+1)
        item[:, 1] *= 10 * (i+1)

        buffer.store_transition(item, a1 * i, float(i)/2, False)

    return buffer


def get_filled_buffer3x3():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 2), dtype=int)
    action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(2, 2, 2), dtype=float)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(16).reshape((2, 2, 2, 2))
    a1 = np.arange(16).reshape((2, 2, 2, 2))

    for i in range(30):
        item = v1.copy()
        item[:, 0] *= (i+1)
        item[:, 1] *= 10 * (i+1)

        buffer.store_transition(item, i * a1, float(i)/2, False)

    return buffer


def get_filled_buffer1x1_history():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 1), dtype=int)
    action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(2,), dtype=float)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(4).reshape((2, 2, 1))
    a1 = np.arange(4).reshape((2, 2))

    for i in range(30):
        item = v1.copy()
        item[:, 0] *= (i+1)
        item[:, 1] *= 10 * (i+1)

        buffer.store_transition(item, a1 * i, float(i)/2, False)

    return buffer


def get_filled_buffer2x2_history():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 1), dtype=int)
    action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(2, 2), dtype=float)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(8).reshape((2, 2, 2, 1))
    a1 = np.arange(8).reshape((2, 2, 2))

    for i in range(30):
        item = v1.copy()
        item[:, 0] *= (i+1)
        item[:, 1] *= 10 * (i+1)

        buffer.store_transition(item, a1 * i, float(i)/2, False)

    return buffer


def get_filled_buffer3x3_history():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 2, 1), dtype=int)
    action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(2, 2, 2), dtype=float)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(16).reshape((2, 2, 2, 2, 1))
    a1 = np.arange(16).reshape((2, 2, 2, 2))

    for i in range(30):
        item = v1.copy()
        item[:, 0] *= (i+1)
        item[:, 1] *= 10 * (i+1)

        buffer.store_transition(item, i * a1, float(i)/2, False)

    return buffer


def get_filled_buffer_extra_info():
    """ Return simple preinitialized buffer """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 1), dtype=int)
    action_space = gym.spaces.Discrete(4)

    buffer = DequeMultiEnvBufferBackend(
        20, num_envs=2, observation_space=observation_space, action_space=action_space,
        extra_data={
            'neglogp': np.zeros((20, 2), dtype=float)
        }
    )

    v1 = np.ones(8).reshape((2, 2, 2, 1))

    for i in range(30):
        item = v1.copy()
        item[0] *= (i+1)
        item[1] *= 10 * (i+1)
        buffer.store_transition(item, 0, float(i)/2, False, extra_info={
            'neglogp': np.array([i / 30.0, (i+1) / 30.0])
        })

    return buffer


def get_filled_buffer_with_dones():
    """ Return simple preinitialized buffer with some done's in there """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 1), dtype=int)
    action_space = gym.spaces.Discrete(4)

    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(8).reshape((2, 2, 2, 1))

    done_set = {2, 5, 10, 13, 18, 22, 28}

    for i in range(30):
        item = v1.copy()
        item[0] *= (i+1)
        item[1] *= 10 * (i+1)

        done_array = np.array([i in done_set, (i+1) in done_set], dtype=bool)
        buffer.store_transition(item, 0, float(i)/2, done_array)

    return buffer


def test_simple_get_frame():
    """ Check if get_frame returns frames from a buffer partially full """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 1), dtype=int)
    action_space = gym.spaces.Discrete(4)
    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(8).reshape((2, 2, 2, 1))
    v1[1] *= 2

    v2 = v1 * 2
    v3 = v1 * 3

    buffer.store_transition(v1, 0, 0, False)
    buffer.store_transition(v2, 0, 0, False)
    buffer.store_transition(v3, 0, 0, False)

    assert np.all(buffer.get_frame(0, 0, 4).max(0).max(0) == np.array([0, 0, 0, 1]))
    assert np.all(buffer.get_frame(1, 0, 4).max(0).max(0) == np.array([0, 0, 1, 2]))
    assert np.all(buffer.get_frame(2, 0, 4).max(0).max(0) == np.array([0, 1, 2, 3]))

    assert np.all(buffer.get_frame(0, 1, 4).max(0).max(0) == np.array([0, 0, 0, 2]))
    assert np.all(buffer.get_frame(1, 1, 4).max(0).max(0) == np.array([0, 0, 2, 4]))
    assert np.all(buffer.get_frame(2, 1, 4).max(0).max(0) == np.array([0, 2, 4, 6]))

    with t.assert_raises(VelException):
        buffer.get_frame(3, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(4, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(3, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(4, 1, 4)


def test_full_buffer_get_frame():
    """ Check if get_frame returns frames for full buffer """
    buffer = get_filled_buffer()

    nt.assert_array_equal(buffer.get_frame(0, 0, 4).max(0).max(0), np.array([18, 19, 20, 21]))
    nt.assert_array_equal(buffer.get_frame(1, 0, 4).max(0).max(0), np.array([19, 20, 21, 22]))
    nt.assert_array_equal(buffer.get_frame(9, 0, 4).max(0).max(0), np.array([27, 28, 29, 30]))

    nt.assert_array_equal(buffer.get_frame(0, 1, 4).max(0).max(0), np.array([180, 190, 200, 210]))
    nt.assert_array_equal(buffer.get_frame(1, 1, 4).max(0).max(0), np.array([190, 200, 210, 220]))
    nt.assert_array_equal(buffer.get_frame(9, 1, 4).max(0).max(0), np.array([270, 280, 290, 300]))

    with t.assert_raises(VelException):
        buffer.get_frame(10, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(11, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(12, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(10, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(11, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(12, 1, 4)

    nt.assert_array_equal(buffer.get_frame(13, 0, 4).max(0).max(0), np.array([11, 12, 13, 14]))
    nt.assert_array_equal(buffer.get_frame(19, 0, 4).max(0).max(0), np.array([17, 18, 19, 20]))

    nt.assert_array_equal(buffer.get_frame(13, 1, 4).max(0).max(0), np.array([110, 120, 130, 140]))
    nt.assert_array_equal(buffer.get_frame(19, 1, 4).max(0).max(0), np.array([170, 180, 190, 200]))


def test_full_buffer_get_future_frame():
    """ Check if get_frame_with_future works with full buffer """
    buffer = get_filled_buffer()

    nt.assert_array_equal(buffer.get_frame_with_future(0, 0, 4)[1].max(0).max(0), np.array([19, 20, 21, 22]))
    nt.assert_array_equal(buffer.get_frame_with_future(1, 0, 4)[1].max(0).max(0), np.array([20, 21, 22, 23]))

    nt.assert_array_equal(buffer.get_frame_with_future(0, 1, 4)[1].max(0).max(0), np.array([190, 200, 210, 220]))
    nt.assert_array_equal(buffer.get_frame_with_future(1, 1, 4)[1].max(0).max(0), np.array([200, 210, 220, 230]))

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(9, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(10, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(11, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(12, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(9, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(10, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(11, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(12, 1, 4)

    nt.assert_array_equal(buffer.get_frame_with_future(13, 0, 4)[1].max(0).max(0), np.array([12, 13, 14, 15]))
    nt.assert_array_equal(buffer.get_frame_with_future(19, 0, 4)[1].max(0).max(0), np.array([18, 19, 20, 21]))

    nt.assert_array_equal(buffer.get_frame_with_future(13, 1, 4)[1].max(0).max(0), np.array([120, 130, 140, 150]))
    nt.assert_array_equal(buffer.get_frame_with_future(19, 1, 4)[1].max(0).max(0), np.array([180, 190, 200, 210]))


def test_buffer_filling_size():
    """ Check if buffer size is properly updated when we add items """
    observation_space = gym.spaces.Box(low=0, high=255, shape=(2, 2, 1), dtype=int)
    action_space = gym.spaces.Discrete(4)
    buffer = DequeMultiEnvBufferBackend(20, num_envs=2, observation_space=observation_space, action_space=action_space)

    v1 = np.ones(8).reshape((2, 2, 2, 1))

    t.eq_(buffer.current_size, 0)

    buffer.store_transition(v1, 0, 0, False)
    buffer.store_transition(v1, 0, 0, False)

    t.eq_(buffer.current_size, 2)

    for i in range(30):
        buffer.store_transition(v1 * (i+1), 0, float(i)/2, False)

    t.eq_(buffer.current_size, buffer.buffer_capacity)


def test_get_frame_with_dones():
    """ Check if get_frame works properly in case there are multiple sequences in buffer """
    buffer = get_filled_buffer_with_dones()

    nt.assert_array_equal(buffer.get_frame(0, 0, 4).max(0).max(0), np.array([0, 0, 20, 21]))
    nt.assert_array_equal(buffer.get_frame(1, 0, 4).max(0).max(0), np.array([0, 20, 21, 22]))
    nt.assert_array_equal(buffer.get_frame(2, 0, 4).max(0).max(0), np.array([20, 21, 22, 23]))
    nt.assert_array_equal(buffer.get_frame(3, 0, 4).max(0).max(0), np.array([0, 0, 0, 24]))

    nt.assert_array_equal(buffer.get_frame(8, 0, 4).max(0).max(0), np.array([26, 27, 28, 29]))
    nt.assert_array_equal(buffer.get_frame(9, 0, 4).max(0).max(0), np.array([0, 0, 0, 30]))

    nt.assert_array_equal(buffer.get_frame(0, 1, 4).max(0).max(0), np.array([0, 190, 200, 210]))
    nt.assert_array_equal(buffer.get_frame(1, 1, 4).max(0).max(0), np.array([190, 200, 210, 220]))
    nt.assert_array_equal(buffer.get_frame(2, 1, 4).max(0).max(0), np.array([0, 0, 0, 230]))
    nt.assert_array_equal(buffer.get_frame(3, 1, 4).max(0).max(0), np.array([0, 0, 230, 240]))

    nt.assert_array_equal(buffer.get_frame(8, 1, 4).max(0).max(0), np.array([0, 0, 0, 290]))
    nt.assert_array_equal(buffer.get_frame(9, 1, 4).max(0).max(0), np.array([0, 0, 290, 300]))

    with t.assert_raises(VelException):
        buffer.get_frame(10, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(10, 1, 4)

    nt.assert_array_equal(buffer.get_frame(11, 0, 4).max(0).max(0), np.array([0, 0, 0, 12]))
    nt.assert_array_equal(buffer.get_frame(12, 0, 4).max(0).max(0), np.array([0, 0, 12, 13]))

    with t.assert_raises(VelException):
        buffer.get_frame(11, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(12, 1, 4)


def test_get_frame_future_with_dones():
    """ Check if get_frame_with_future works properly in case there are multiple sequences in buffer """
    buffer = get_filled_buffer_with_dones()

    nt.assert_array_equal(buffer.get_frame_with_future(0, 0, 4)[1].max(0).max(0), np.array([0, 20, 21, 22]))
    nt.assert_array_equal(buffer.get_frame_with_future(1, 0, 4)[1].max(0).max(0), np.array([20, 21, 22, 23]))
    nt.assert_array_equal(buffer.get_frame_with_future(2, 0, 4)[1].max(0).max(0), np.array([21, 22, 23, 0]))

    nt.assert_array_equal(buffer.get_frame_with_future(3, 0, 4)[1].max(0).max(0), np.array([0, 0, 24, 25]))
    nt.assert_array_equal(buffer.get_frame_with_future(8, 0, 4)[1].max(0).max(0), np.array([27, 28, 29, 0]))

    nt.assert_array_equal(buffer.get_frame_with_future(0, 1, 4)[1].max(0).max(0), np.array([190, 200, 210, 220]))
    nt.assert_array_equal(buffer.get_frame_with_future(1, 1, 4)[1].max(0).max(0), np.array([200, 210, 220, 0]))
    nt.assert_array_equal(buffer.get_frame_with_future(2, 1, 4)[1].max(0).max(0), np.array([0, 0, 230, 240]))

    nt.assert_array_equal(buffer.get_frame_with_future(3, 1, 4)[1].max(0).max(0), np.array([0, 230, 240, 250]))
    nt.assert_array_equal(buffer.get_frame_with_future(7, 1, 4)[1].max(0).max(0), np.array([260, 270, 280, 0]))

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(9, 0, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(10, 0, 4)

    nt.assert_array_equal(buffer.get_frame_with_future(11, 0, 4)[1].max(0).max(0), np.array([0, 0, 12, 13]))
    nt.assert_array_equal(buffer.get_frame_with_future(12, 0, 4)[1].max(0).max(0), np.array([0, 12, 13, 14]))

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(9, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame_with_future(10, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(11, 1, 4)

    with t.assert_raises(VelException):
        buffer.get_frame(12, 1, 4)

    nt.assert_array_equal(buffer.get_frame_with_future(13, 1, 4)[1].max(0).max(0), np.array([0, 0, 140, 150]))


def test_get_batch():
    """ Check if get_batch works properly for buffers """
    buffer = get_filled_buffer_with_dones()

    batch = buffer.get_batch(np.array([
        [0, 1, 2, 3, 4, 5, 6, 7],  # Frames for env=0
        [1, 2, 3, 4, 5, 6, 7, 8],  # Frames for env=1
    ]).T, history_length=4)

    obs = batch['states']
    act = batch['actions']
    rew = batch['rewards']
    obs_tp1 = batch['states+1']
    dones = batch['dones']

    nt.assert_array_equal(dones[:, 0], np.array([False, False, True, False, False, False, False, False]))
    nt.assert_array_equal(dones[:, 1], np.array([True, False, False, False, False, False, True, False]))

    nt.assert_array_equal(obs[:, 0].max(1).max(1), np.array([
        [0, 0, 20, 21],
        [0, 20, 21, 22],
        [20, 21, 22, 23],
        [0, 0, 0, 24],
        [0, 0, 24, 25],
        [0, 24, 25, 26],
        [24, 25, 26, 27],
        [25, 26, 27, 28],
    ]))

    nt.assert_array_equal(obs[:, 1].max(1).max(1), np.array([
        [190, 200, 210, 220],
        [0, 0, 0, 230],
        [0, 0, 230, 240],
        [0, 230, 240, 250],
        [230, 240, 250, 260],
        [240, 250, 260, 270],
        [250, 260, 270, 280],
        [0, 0, 0, 290],
    ]))

    nt.assert_array_equal(act[:, 0], np.array([0, 0, 0, 0, 0, 0, 0, 0]))
    nt.assert_array_equal(rew[:, 0], np.array([10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5]))

    nt.assert_array_equal(act[:, 1], np.array([0, 0, 0, 0, 0, 0, 0, 0]))
    nt.assert_array_equal(rew[:, 1], np.array([10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0]))

    nt.assert_array_equal(obs_tp1[:, 0].max(1).max(1), np.array([
        [0, 20, 21, 22],
        [20, 21, 22, 23],
        [21, 22, 23, 0],
        [0, 0, 24, 25],
        [0, 24, 25, 26],
        [24, 25, 26, 27],
        [25, 26, 27, 28],
        [26, 27, 28, 29]
    ]))

    nt.assert_array_equal(obs_tp1[:, 1].max(1).max(1), np.array([
        [200, 210, 220, 0],
        [0, 0, 230, 240],
        [0, 230, 240, 250],
        [230, 240, 250, 260],
        [240, 250, 260, 270],
        [250, 260, 270, 280],
        [260, 270, 280, 0],
        [0, 0, 290, 300],
    ]))

    with t.assert_raises(VelException):
        buffer.get_batch(np.array([
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]).T, history_length=4)


def test_sample_and_get_batch():
    """ Check if batch sampling works properly """
    buffer = get_filled_buffer_with_dones()

    for i in range(100):
        indexes = buffer.sample_batch_uniform(batch_size=5, history_length=4)
        batch = buffer.get_batch(indexes, history_length=4)

        obs = batch['states']
        act = batch['actions']
        rew = batch['rewards']
        obs_tp1 = batch['states+1']
        dones = batch['dones']

        with t.assert_raises(AssertionError):
            nt.assert_array_equal(indexes[:, 0], indexes[:, 1])

        t.eq_(obs.shape[0], 5)
        t.eq_(act.shape[0], 5)
        t.eq_(rew.shape[0], 5)
        t.eq_(obs_tp1.shape[0], 5)
        t.eq_(dones.shape[0], 5)


def test_storing_extra_info():
    """ Make sure additional information are stored and recovered properly """
    buffer = get_filled_buffer_extra_info()

    indexes = np.array([
        [0, 1, 2, 17, 18, 19],
        [0, 1, 2, 17, 18, 19],
    ]).T

    batch = buffer.get_batch(indexes, history_length=4)

    nt.assert_equal(batch['neglogp'][0, 0], 20.0/30)
    nt.assert_equal(batch['neglogp'][1, 0], 21.0/30)
    nt.assert_equal(batch['neglogp'][2, 0], 22.0/30)
    nt.assert_equal(batch['neglogp'][3, 0], 17.0/30)
    nt.assert_equal(batch['neglogp'][4, 0], 18.0/30)
    nt.assert_equal(batch['neglogp'][5, 0], 19.0/30)

    nt.assert_equal(batch['neglogp'][0, 1], 21.0/30)
    nt.assert_equal(batch['neglogp'][1, 1], 22.0/30)
    nt.assert_equal(batch['neglogp'][2, 1], 23.0/30)
    nt.assert_equal(batch['neglogp'][3, 1], 18.0/30)
    nt.assert_equal(batch['neglogp'][4, 1], 19.0/30)
    nt.assert_equal(batch['neglogp'][5, 1], 20.0/30)


def test_sample_rollout_half_filled():
    """ Test if sampling rollout is correct and returns proper results """
    buffer = get_half_filled_buffer()

    indexes = []

    for i in range(1000):
        rollout_idx = buffer.sample_batch_rollout(rollout_length=5, history_length=4)
        rollout = buffer.get_rollout(indexes=rollout_idx, rollout_length=5, history_length=4)

        t.assert_equal(rollout['states'].shape[0], 5)  # Rollout length
        t.assert_equal(rollout['states'].shape[-1], 4)  # History length

        indexes.append(rollout_idx)

    t.assert_equal(np.min(indexes), 4)
    t.assert_equal(np.max(indexes), 8)

    with t.assert_raises(VelException):
        buffer.sample_batch_rollout(rollout_length=10, history_length=4)

    rollout_idx = buffer.sample_batch_rollout(rollout_length=9, history_length=4)
    rollout = buffer.get_rollout(indexes=rollout_idx, rollout_length=9, history_length=4)

    nt.assert_array_equal(rollout_idx, np.array([8, 8]))

    nt.assert_array_equal(rollout['rewards'], np.array([
        [0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4.],
        [0., 0.5, 1., 1.5, 2., 2.5, 3., 3.5, 4.],
    ]).T)


def test_sample_rollout_filled():
    """ Test if sampling rollout is correct and returns proper results """
    buffer = get_filled_buffer()

    indexes = []

    for i in range(1000):
        rollout_idx = buffer.sample_batch_rollout(rollout_length=5, history_length=4)
        rollout = buffer.get_rollout(indexes=rollout_idx, rollout_length=5, history_length=4)

        t.assert_equal(rollout['states'].shape[0], 5)  # Rollout length
        t.assert_equal(rollout['states'].shape[-1], 4)  # History length

        indexes.append(rollout_idx)

    t.assert_equal(np.min(indexes), 0)
    t.assert_equal(np.max(indexes), 19)

    with t.assert_raises(VelException):
        buffer.sample_batch_rollout(rollout_length=17, history_length=4)

    max_rollout = buffer.sample_batch_rollout(rollout_length=16, history_length=4)

    rollout = buffer.get_rollout(max_rollout, rollout_length=16, history_length=4)

    nt.assert_array_equal(max_rollout, np.array([8, 8]))
    t.assert_almost_equal(np.sum(rollout['rewards']), 164.0 * 2)


def test_buffer_flexible_obs_action_sizes():
    b1x1 = get_filled_buffer1x1()
    b2x2 = get_filled_buffer2x2()
    b3x3 = get_filled_buffer3x3()

    nt.assert_array_almost_equal(b1x1.get_frame(0, 0), np.array([21, 210]))
    nt.assert_array_almost_equal(b2x2.get_frame(0, 0), np.array([[21, 21], [210, 210]]))
    nt.assert_array_almost_equal(b3x3.get_frame(0, 0), np.array([[[21, 21], [21, 21]], [[210, 210], [210, 210]]]))

    nt.assert_array_almost_equal(b1x1.get_transition(0, 0)['action'], np.array([0, 20]))
    nt.assert_array_almost_equal(b2x2.get_transition(0, 0)['action'], np.array([[0, 20], [40, 60]]))
    nt.assert_array_almost_equal(b3x3.get_transition(0, 0)['action'], np.array(
        [[[0, 20], [40, 60]],
        [[80, 100], [120, 140]]]
    ))

    with t.assert_raises(AssertionError):
        b1x1.get_frame(0, 0, history_length=2)

    with t.assert_raises(AssertionError):
        b1x1.get_transition(0, 0, history_length=2)

    with t.assert_raises(AssertionError):
        b2x2.get_frame(0, 0, history_length=2)

    with t.assert_raises(AssertionError):
        b2x2.get_transition(0, 0, history_length=2)

    with t.assert_raises(AssertionError):
        b3x3.get_frame(0, 0, history_length=2)

    with t.assert_raises(AssertionError):
        b3x3.get_transition(0, 0, history_length=2)


def test_buffer_flexible_obs_action_sizes_with_history():
    b1x1 = get_filled_buffer1x1_history()
    b2x2 = get_filled_buffer2x2_history()
    b3x3 = get_filled_buffer3x3_history()

    nt.assert_array_almost_equal(b1x1.get_frame(0, 0, history_length=2), np.array([[20, 21], [200, 210]]))
    nt.assert_array_almost_equal(b2x2.get_frame(0, 0, history_length=2), np.array([[[20, 21], [20, 21]], [[200, 210], [200, 210]]]))
    nt.assert_array_almost_equal(b3x3.get_frame(0, 0, history_length=2), np.array(
        [[[[20, 21], [20, 21]], [[20, 21], [20, 21]]], [[[200, 210], [200, 210]], [[200, 210], [200, 210]]]]
    ))

    nt.assert_array_almost_equal(b1x1.get_transition(0, 0, history_length=2)['state+1'], np.array([[21, 22], [210, 220]]))
    nt.assert_array_almost_equal(b2x2.get_transition(0, 0, history_length=2)['state+1'], np.array(
        [[[21, 22], [21, 22]], [[210, 220], [210, 220]]]
    ))
    nt.assert_array_almost_equal(b3x3.get_transition(0, 0, history_length=2)['state+1'], np.array(
        [[[[21, 22], [21, 22]], [[21, 22], [21, 22]]],
         [[[210, 220], [210, 220]], [[210, 220], [210, 220]]]]
    ))
