import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np

class MarsLanderenv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 50
    }

    def __init__(self):
        self.gravity = 3.711 #gravity on mars
        self.mass = 0.1 #mass of each bar in Kg.
        self.length = 1 #length of each bar in m.
