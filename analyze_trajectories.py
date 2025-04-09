"""
Script for analyzing pickle file from DeepLabCut. 
"""
import os 
from pathlib import Path 

import numpy as np 

import pandas as pd 

import matplotlib.pyplot as plt 

path_name = "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-14-12-12-26DLC_Resnet50_One-photonApr3shuffle1_snapshot_030.h5"

# Load h5 file. 
Dataframe = pd.read_hdf(path_name)

Dataframe.head()

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
	scorer = Dataframe.columns.get_level_values(0)[0] # You can read out the header to get the scorer name! 
	
	for bpindex, bp in enumerate(bodyparts2plot):
		Index = Dataframe[scorer][bp]['likelihood'].values > pcutoff
		plt.plot(Dataframe[scorer][bp]['x'].values[Index], Dataframe[scorer][bp]['y'].values[Index], '.', markersize=5, color=colors(bpindex), alpha=alphavalue)
		
	plt.gca().invert_yaxis()
	
	sm    = plt.cm.ScalarMappable(cmap=plt.get_cmap(colormap), norm=plt.Normalize(vmin=0, vmax=len(bodyparts2plot) - 1))
	sm._A = [] 
	cbar  = plt.colorbar(sm, ticks=range(len(bodyparts2plot)))
	cbar.set_ticklabels(bodyparts2plot)
	plt.figure(figsize=fs)
	Time = np.arange(np.size([scorer][bodyparts2plot[0]]['x'].values))
	
	plt.xlabel('Frame index')
	plt.ylabel('X and y-position in pixels')
	
	plt.figure(figsize=fs)
	
bodyparts =  Dataframe.columns.get_level_values(1)  # You can read out the header to get body part names!

bodyparts2plot = np.unique(bodyparts)

PlottingResults(Dataframe, bodyparts2plot, alphavalue=0.2, pcutoff=0.5, fs=(8,4))
