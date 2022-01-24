## OAK D Lite Experiments

Experiments with the OpenCV OAK D Lite Ai camera and the DepthAi API.

<br>

My purpose is to learn to use the Oak D Lite camera and to set up boilerplate code that I can use on future projects. I'm running experiments on a Mac (8GB RAM, USB 3.0) and on a Raspberry Pi 3 A+ (512MB RAM, USB 2.0).

<br>
<img src="https://github.com/vbookshelf/OAK-D-Lite-Experiments/blob/main/images/oak-d-lite.jpg" width="500"></img>
<i>OAK D Lite Camera</i><br>
<br>

<br>

### Experiments

- Exp_01 - Access the 3 cameras on a Mac<br>
Learning how to use the DepthAi API with Python and OpenCV to access the three Oak D Lite cameras - on a Mac.<br>
https://github.com/vbookshelf/OAK-D-Lite-Experiments/tree/main/Exp_01-Access-the%20-3-cameras-on-a-Mac

- Exp_02 - Access the RGB Camera on a Raspberry Pi<br>
Learning how to install and run the DepthAi API on a Raspberry Pi 3 A+.<br>
https://github.com/vbookshelf/OAK-D-Lite-Experiments/tree/main/Exp_02-Access-the-rgb-camera-on-a-raspberry-pi

- Exp_03 - Pass the rgb camera feed into a Mediapipe Hand Tracking model for CPU inference<br>
Pass the video feed from the rgb camera into a Mediapipe hand tracking model. Use the CPU for inference and not the Myriad X chip.<br>
https://github.com/vbookshelf/OAK-D-Lite-Experiments/tree/main/Exp_03-rgb-feed-w-cpu-mediapipe-hand-tracking

- Exp_04 - Run inference inside the camera using the Myriad X chip<br>
Run the Luxonis hello_world.py program on the Mac and on the Raspberry Pi to check the performance.<br>
https://github.com/vbookshelf/OAK-D-Lite-Experiments/tree/main/Exp_04-Run-inference-in-camera-using-MyriadX

- Exp_05 - Explore how image pre-processing is being handled in hello_world.py<br>
In the Luxonis hello_world.py example, try to understand how the pre-processing steps (normalization, RGB to BGR) are being handled.<br>

<br>
