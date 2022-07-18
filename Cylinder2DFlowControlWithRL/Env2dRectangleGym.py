import gym
from gym import spaces
import copy
import subprocess
import os
import shutil
import numpy as np
import csv
import scipy.signal as sgn
import io
from probes import PenetratedDragProbeANN, PenetratedLiftProbeANN, PressureProbeANN, VelocityProbeANN, RecirculationAreaProbe


class RingBuffer():
    "A 1D ring buffer using numpy arrays"
    def __init__(self, length):
        self.data = np.zeros(length, dtype='f')  # Initialise ring array 'data' as length-array of floats
        self.index = 0  # Initialise InPointer as 0 (where new data begins to be written)

    def extend(self, x):
        "adds array x to ring buffer"
        x_indices = (self.index + np.arange(x.size)) % self.data.size  # Find indices that x will occupy in 'data' array
        self.data[x_indices] = x  # Input the new array into ring buffer ('data')
        self.index = x_indices[-1] + 1  # Find new index for next new data

    def get(self):
        "Returns the first-in-first-out data in the ring buffer (returns data in order of introduction)"
        idx = (self.index + np.arange(self.data.size)) % self.data.size
        return self.data[idx]



class Env2dRec(gym.Env):
  
  def __init__(self, output_params):
        super().__init__()
        
        self.output_params = output_params
        self.ann_probes = PressureProbeANN(self.flow, self.output_params['locations'])
        state_shape = self.ann_probes.nprobes
        
        self.action_space = gym.spaces.Box(shape=(self.action_shape,), low=, high, 
        
        self.observation_space = gym.spaces.Box(shape=(state_shape,), low=-np.inf, high=np.inf) # Shape is number of probes

    def step(self, action):
        ...
        return observation, reward, done, info
    def reset(self):
        ...
        return observation  # reward, done, info can't be included
    def render(self, mode='human'):
        ...
    def close (self):
        ...
  
  
  
  
  
  























