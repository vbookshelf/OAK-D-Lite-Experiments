## Exp_03 - Pass the rgb camera feed into a Mediapipe Hand Tracking model for CPU inference

### Objectives
- Learn how to combine DepthAi with Mediapipe models and OpenCV.
- Set up the code to run inference on the feed from the rgb camera.
- Use the CPU and not the Myriad X chip for inference.
- Run the code on both the Mac and the Raspberry Pi 3 A+

### Notes
- The python code is a simple app that detects the hand and counts the number of fingers that are being held up. This count is displayed on the screen in real time. It works with the right hand only.
- The code worked on both the Mac and on the Raspberry Pi.
- The frame rate was extremely slow on the Raspberry Pi - approx. 2 fps. This is almost the same as the performance I saw when using the Raspberry Pi camera. The Raspberry Pi 3 A+ has only 512MB of RAM. My guess is that this is the cause of the slow performance. However, the Oak D Lite is designed to run inference inside the camera using the Myriad X chip. Therefore, if inference is run inside the camera (without using the CPU) then performance on the Pi should be much faster.
