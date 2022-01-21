## Exp_04 - Run inference inside the camera using the Myriad X chip

### Objectives
- Run the Luxonis hello_world.py program on the Mac and on the Raspberry Pi 3 A+
- Verify that everything works
- Check inference performance (i.e. is there any lag?)

### Tutorial
- Luxonis Hello World tutorial:<br>
https://docs.luxonis.com/projects/api/en/latest/tutorials/hello_world/#hello-world

- Code for the above tutorial:<br>
https://github.com/luxonis/depthai-tutorials/blob/master/1-hello-world/hello_world.py

### Notes
- I modified the original tutorial code so that the frame rate (fps) is displayed on the image. Then I just ran it on the Mac and Raspberry Pi without any changes.
- The code includes loading an OpenVINO model and then using if for inference.
- I needed to install blobconverter on the Pi:<br>
$ pip install blobconverter
- The model detects people.
- The Raspberry Pi has USB 2.0 and not the faster USB 3.0 for which the camera was designed.
- The program ran smoothly on both the Mac and Raspberry Pi. Predictions are in real time and there's no lag.
- The fast and real time performance on the Raspberry Pi (only 512MB RAM, USB 2.0) exceeded my expectations.

<br>
