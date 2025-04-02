# Script for the tracking of the tail of the zebrafish during one-photon 
# light sheet recording.

import deeplabcut 
from sys import platform, exit 


from IPython import get_ipython

ipython = get_ipython()
ipython.run_line_magic("load_ext", "autoreload")
ipython.run_line_magic("autoreload", "1")

if platform == 'linux' or platform == 'linux2':
    video = ["/home/enrique/WashU/Data/20220218-f11/videos/2022-02-18-13-11-27.mp4"] # Enter the paths of your videos or Folder you want to grab frames from.
    #matplotlib.use('Agg')
elif platform == 'darwin':
    video ["/home/enrique/WashU/Data/20220218-f11/videos/2022-02-18-13-11-27.mp4"] # Enter the paths of your videos or Folder you want to grab frames from.
    matplotlib.use('MacOSX')
elif platform == 'win32':
    video = ["/home/enrique/WashU/Data/20220218-f11/videos/2022-02-18-13-11-27.mp4"] # Enter the paths of your videos or Folder you want to grab frames from.
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
			# working_directory="/home/enrique/DeepLabCut/",
# )

path_config_file = "/home/enrique/DeepLabCut/One-photon-Hansen-2025-03-27/config.yaml"

# NOTE: The function returns the path, where your project is. 
# You could also enter this manually (e.g. if the project is already created and you want to pick up, where you stopped...)
# Enter the path of the config file that was just created from the above step (check the folder):
# path_config_file = "/home/Mackenzie/Reaching/config.yaml"

# deeplabcut.extract_frames(path_config_file, mode="automatic", cluster_step=1)

# # Napari will pop up!
# # Please go to plugin > deeplabcut to start
# # then, drag-and-drop the project configuration file into the viewer (the value of path_config_file)
# # finally, drop the folder containing the images (in 'labeled-data') in the viewer.

# deeplabcut.label_frames(path_config_file)

# deeplabcut.check_labels(path_config_file) # This creates a subdirectory with the frames + your labels.


# %gui qt6 
# import napari
# napari.Viewer()

# deeplabcut.create_training_dataset(path_config_file)  # Remember, there are several networks you can pick, the default is resnet-50!

# deeplabcut.train_network(path_config_file)

# deeplabcut.evaluate_network(path_config_file, plotting=True)

# videofile_path = "/home/enrique/WashU/Data/20220218-f11/videos/2022-02-18-13-11-27.mp4" # Enter a folder or a list of videos to analyze.

# deeplabcut.analyze_videos(path_config_file, videofile_path, videotype='.mp4')

# deeplabcut.create_labeled_video(path_config_file, videofile_path)
