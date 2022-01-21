## Exp_01 Access the 3 cameras on a Mac

### Ojectives
- Install DepthAi on a Mac that's running macOC Big Sur.
- Learn how to access the cameras using Python and OpenCV.
- Run the attched python code examples on the Mac. These code samples simply display a window showing the video feed from the two mono camaeras and from the rgb camera.

<br>
<img src="https://github.com/vbookshelf/OAK-D-Lite-Experiments/blob/main/images/mac-oak-d-lite.jpg" width="400"></img>
<i>OAK D Lite Camera</i><br>
<br>

### Tutorials

- I followed these excellent tutorials by OpenCV:<br>
https://www.youtube.com/playlist?list=PLfYPZalDvZDLOjzSkoHQ2_h4joHNUegbB

<br>

### Notes
- The default python environment on my computer is Python 2. I therefore, had to install DepthAi in a Python 3 virtual environment.
- The installation steps are decribed in the Luxonis docs:<br>
https://docs.luxonis.com/en/latest/

$ git clone https://github.com/luxonis/depthai.git<br>
$ cd depthai<br>
$ python3 install_requirements.py<br>
$ python3 depthai_demo.py<br>
