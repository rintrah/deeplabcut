"""
Script for analyzing pickle file from DeepLabCut. 
"""
import os 
from pathlib import Path 

import numpy as np 

import pandas as pd 

import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d

import pdb

path_name = "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-14-12-12-26DLC_Resnet50_One-photonApr3shuffle1_snapshot_030.h5"

# Load h5 file. 
Dataframe = pd.read_hdf(path_name)

Dataframe.head()

idx = pd.IndexSlice

def get_cmap(n, name='hsv'):
	return plt.get_cmap(name, n)
	
def Histogram(vector, color, bins):
	dvector = np.diff(vector)
	dvector = dvector[np.isfinite(dvector)]
	plt.hist(dvector, color=color, histype='step', bins=bins)
	
def PlottingResults(Dataframe, bodyparts2plot, alphavalue=0.2, pcutoff=0.5, colormap='jet', fs=(4, 3)):
	"""
	Plots poses vs time; pose x vs pose y; histogram of differences and likelihoods.
	"""
	plt.figure(figsize=fs)
	colors = get_cmap(len(bodyparts2plot), name=colormap)
	# We focus on the range defined by 70 minutes and 80 minutes of the recording.
	# Create matrix with the DeepLabCut information.  (Pandas is too slow!)
	xytp = np.array([Dataframe.loc[:, idx[:, :, 'x']].values, Dataframe.loc[:, idx[:, :, 'y']].values])
	for t in np.arange(0, xytp.shape[1], 500):
		plt.plot(xytp[0, t,:], xytp[1, t,:], c='gray', alpha=0.2)

	plt.plot([plt.gca().axis()[0], plt.gca().axis()[3]], [xytp[0, 0,0], xytp[1, 0,0]], c='r', lw=2)
	plt.gca().invert_yaxis()
	plt.show()
	
# The way the programmers of DeepLabCut established that Dataframe columns has three levels:  1. The name of the model, 2. the body parts, and 3. the coordinates and likelihood.
bodyparts =  Dataframe.columns.levels[1].to_list() 

PlottingResults(Dataframe, bodyparts, alphavalue=0.2, pcutoff=0.5, fs=(8,4))
