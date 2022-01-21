## Exp_01 Access the 3 cameras on a Mac

### Ojectives
- Install DepthAi on a Mac that's running macOS Big Sur.
- Learn how to access the cameras using Python and OpenCV.
- Run the attached python code examples on the Mac. These code samples simply display a window showing the video feed from the two mono cameras and from the rgb camera. The depth.py file shows how to create a depth map.

<br>
<img src="https://github.com/vbookshelf/OAK-D-Lite-Experiments/blob/main/images/mac-oak-d-lite.jpg" width="400"></img>
<i>OAK D Lite Camera with USB 3.0 cable</i><br>
<br>

### Tutorials

- I followed these excellent tutorials by OpenCV:<br>
https://www.youtube.com/playlist?list=PLfYPZalDvZDLOjzSkoHQ2_h4joHNUegbB

<br>

### Notes
- The default python environment on my computer is Python 2. I therefore, had to install DepthAi in a Python 3 virtual environment.
- The installation steps are decribed in the Luxonis docs: https://docs.luxonis.com/en/latest/<br>
$ git clone https://github.com/luxonis/depthai.git<br>
$ cd depthai<br>
$ python3 install_requirements.py<br>
$ python3 depthai_demo.py<br>
- The Mac has a USB 3.0 port. I used a USB 3.0 cable to ensure fast data transfer between the camera and the Mac. However, when I replaced this with a USB 2.0 cable I found that the frame rate was still the same - approx. 30fps.

<br>
