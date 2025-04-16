"""
Script for analyzing pickle file from DeepLabCut. 
"""
from sys import platform
import os 
from pathlib import Path 

import numpy as np 

import pandas as pd 

import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d
from skspatial.objects import Line, Point


import pdb

import deeplabcut

from deeplabcut.core.engine import Engine

engine = Engine.PYTORCH

if platform == 'linux' or platform == 'linux2':
    video = ["/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-06-08-14-54-59.mp4",
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-07-13-12-49-43.mp4", 
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-07-06-13-48-55.mp4",
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-06-25-15-21-37.mp4",
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-02-18-13-11-27.mp4",
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-14-12-12-26.mp4"]  # Enter the paths of your videos or Folder you want to grab frames from.
    working_directory = "/home/enrique/DeepLabCut/"
    path_config_file  = "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/config.yaml"
    videofile_path    = ["/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-06-08-14-54-59.mp4",
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-07-13-12-49-43.mp4", 
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-07-06-13-48-55.mp4",
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-06-25-15-21-37.mp4",
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-02-18-13-11-27.mp4",
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-14-12-12-26.mp4"] # Enter a folder or a list of videos to analyze.
    destfolder        = "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos"
    #matplotlib.use('Agg')
elif platform == 'darwin':
    video ["/home/enrique/WashU/Data/20220218-f11/videos/2022-02-18-13-11-27.mp4"] # Enter the paths of your videos or Folder you want to grab frames from.
    matplotlib.use('MacOSX')
elif platform == 'win32':
    video             = [r"C:\Users\enriq\Data\WashU\Data\Video\2022-03-14-12-12-26.mp4"] # Enter the paths of your videos or Folder you want to grab frames from.
    path_config_file  = r"C:\Users\enriq\Data\WashU\DeepLabCut\One-photon-Hansen-2025-04-03\config.yaml"
    working_directory = r"C:\Users\enriq\Data\WashU\DeepLabCut"
    videofile_path    = [r"C:\Users\enriq\Data\WashU\DeepLabCut\One-photon-Hansen-2025-04-03\videos"] # Enter a folder or a list of videos to analyze.
    destfolder        = r"C:\Users\enriq\Data\WashU\DeepLabCut\One-photon-Hansen-2025-04-03\analyze-videos"
    #path_config_file = "/home/enrique/DeepLabCut/One-photon-Hansen-2025-03-27/config.yaml"
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
else:
    raise NameError("Unknown OS.")



idx = pd.IndexSlice

def get_cmap(n, name='hsv'):
	return plt.get_cmap(name, n)
	
def Histogram(vector, color, bins):
	dvector = np.diff(vector)
	dvector = dvector[np.isfinite(dvector)]
	plt.hist(dvector, color=color, histype='step', bins=bins)
	

    
def PlottingResults(Dataframe, bodyparts2plot, path_and_name:str, alphavalue=0.2, pcutoff=0.5, colormap='jet', fs=(8, 8)):
	"""
	Plots poses vs time; pose x vs pose y; histogram of differences and likelihoods.
	"""
	colors = get_cmap(len(bodyparts2plot), name=colormap)
	# We focus on the range defined by 70 minutes and 80 minutes of the recording.
	# Create matrix with the DeepLabCut information.  (Pandas is too slow!)
	xytp = np.array([Dataframe.loc[:, idx[:, :, 'x']].values, Dataframe.loc[:, idx[:, :, 'y']].values])
	n_segments = 30
	fig, ax = plt.subplots(figsize=fs)
	for t in np.arange(0, xytp.shape[1], 500):
		points = np.array([xytp[0, t, :], xytp[1, t,:]]).T
		is_nan = np.any(np.isnan(points))
		if not is_nan:
			id_first_nan = points.shape[0]
			N_seg = n_segments + 1
		else:
			id_first_nan = np.where(np.any(np.isnan(points), axis=1))[0][0]
			N_seg = int(np.round(id_first_nan / n_segments_init * (n_segments + 1)))

		alpha = np.linspace(0, 1, N_seg)
		distance = np.cumsum(
		np.sqrt(np.sum(np.diff(points[:id_first_nan, :], axis=0) ** 2, axis=1))
		)
		distance = np.insert(distance, 0, 0) / distance[-1]

		kind = "cubic" if len(distance) > 3 else "linear"
		interpolator = interp1d(
		distance, points[:id_first_nan, :], kind=kind, axis=0
		)

		curve = interpolator(alpha)
		ax.plot(curve[:, 0], curve[:, 1], c='#de2d26', alpha=0.1)

	
	# line = Line.from_points(point_a=[xytp[0, 0,0], xytp[1, 0,0]], point_b=[xytp[0, 0,-1], xytp[1, 0,-1]])
	# point = Point([xytp[0, 10000, -1], xytp[1, 10000,-1]])
	# point_projected = line.project_point(point)

	coefficients = np.polyfit([xytp[0, 0, 0], xytp[0, 0,-1]],[xytp[1, 0,0], xytp[1, 0,-1]], deg=1)
	
	# Let's compute the values of the line...
	polynomial = np.poly1d(coefficients)
	x_axis = np.linspace(0,300,100)
	y_axis = polynomial(x_axis)
	
	ax.invert_yaxis()
	ax.set_axis_off()
	plt.savefig((path_and_name + '.png'), dpi=300, format='png', bbox_inches="tight", transparent=True)
	
	
	
	

if __name__ == "__main__":
	
	path_name = "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/"

	files = []
	for p, d, f in os.walk(path_name):
		for file in f:
			if file.endswith('.h5'):
				files.append(os.path.join(p, file))

	for path_to_file in files:
		Dataframe = pd.read_hdf(path_to_file)
		Dataframe.head()

		# The way the programmers of DeepLabCut established that Dataframe columns has three levels:  1. The name of the model, 2. the body parts, and 3. the coordinates and likelihood.
		bodyparts =  Dataframe.columns.levels[1].to_list() 

		PlottingResults(Dataframe, bodyparts, path_to_file[:-3], alphavalue=0.2, pcutoff=0.5, fs=(8, 8))
		
		
deeplabcut.plot_trajectories(path_config_file, videofile_path)
