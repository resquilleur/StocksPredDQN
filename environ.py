import gym
import gym.spaces
from gym.utils import seeding
from gym.envs.registration import EnvSpec
import enum
import numpy as np

from . import data

DEFAULT_BARS_COUNT = 10
DEFAULT_COMMISSION_PERC = 0.1


class Actions(enum.Enum):
    Skip = 0
    Buy = 1
    Close = 2


class State:
    def __init__(self, bars_count, commission_perc,
                 reset_on_close, reward_on_close=True,
                 volumes=True):
        assert isinstance(bars_count, int)
        assert bars_count > 0
        assert isinstance(commission_perc, float)
        assert commission_perc >= 0.0
        assert isinstance(reset_on_close, bool)
        assert isinstance(reward_on_close, bool)
        self.bars_count = bars_count
        self.commission_perc = commission_perc
        self.reset_on_close = reset_on_close
        self.reward_on_close = reward_on_close
        self.volumes = volumes
