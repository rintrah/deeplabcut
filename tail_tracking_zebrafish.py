# Script for the tracking of the tail of the zebrafish during one-photon 
# light sheet recording.

import deeplabcut 
from sys import platform, exit 

from datetime import date 
import locale 

from IPython import get_ipython

ipython = get_ipython()
ipython.run_line_magic("load_ext", "autoreload")
ipython.run_line_magic("autoreload", "1")

from deeplabcut.core.engine import Engine

engine = Engine.PYTORCH

not_analyzed = ["/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-10-13-10-44-34.mp4",
				"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-16-14-04-55.mp4",
				"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-18-14-53-12.mp4",
				"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-23-10-11-32.mp4",
				]

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
							"/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-14-12-12-26.mp4"]
							# "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-10-13-10-44-34.mp4",
							# "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-16-14-04-55.mp4",
							# "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-18-14-53-12.mp4",
							# "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-03-23-10-11-32.mp4",] # Enter a folder or a list of videos to analyze.
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

task			= "One-photon"  # Enter the name of your experiment Task. 
experimenter	= "Hansen"   # Enter the name of the experimenter. 


# path_config_file = deeplabcut.create_new_project(
			# task,
			# experimenter,
			# video,
			# copy_videos=True,
			# working_directory=working_directory,
# )


# NOTE: The function returns the path, where your project is. 
# You could also enter this manually (e.g. if the project is already created and you want to pick up, where you stopped...)
# Enter the path of the config file that was just created from the above step (check the folder):
# path_config_file = "/home/Mackenzie/Reaching/config.yaml"

#deeplabcut.extract_frames(path_config_file, mode="automatic", cluster_step=1, userfeedback=True)

# Napari will pop up!
# Please go to plugin > deeplabcut to start
# then, drag-and-drop the project configuration file into the viewer (the value of path_config_file)
# finally, drop the folder containing the images (in 'labeled-data') in the viewer.

# deeplabcut.label_frames(path_config_file)

# deeplabcut.check_labels(path_config_file) # This creates a subdirectory with the frames + your labels.


# %gui qt6 
# import napari
# napari.Viewer()

# deeplabcut.create_training_dataset(path_config_file, net_type='resnet_50')  # Remember, there are several networks you can pick, the default is resnet-50!

# deeplabcut.train_network(path_config_file)

# deeplabcut.evaluate_network(path_config_file, plotting=True)


#deeplabcut.analyze_videos(path_config_file, videofile_path, videotype='.mp4', save_as_csv=True, destfolder=destfolder, dynamic=(True,.5,10))

#deeplabcut.create_labeled_video(path_config_file, "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-07-13-12-49-43.mp4", videotype=".mp4", fastmode=False, save_frames=False, draw_skeleton=True)

deeplabcut.extract_outlier_frames(path_config_file, ["/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2021-06-08-14-54-59.mp4", "/home/enrique/DeepLabCut/One-photon-Hansen-04-03-2025/analyze-videos/2022-02-18-13-11-27.mp4"])
