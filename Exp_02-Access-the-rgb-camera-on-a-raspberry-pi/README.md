## Exp_02 - Access the RGB Camera on a Raspberry Pi 3 A+

### Objectives
- Install DepthAi on the Pi.
- Run the attached python code on the Pi. The code simply displays a window showing the feed from the RGB canera.

<br>
<img src="https://github.com/vbookshelf/OAK-D-Lite-Experiments/blob/main/images/rpi-oak-d-lite.jpg" width="400"></img>
<i>OAK D Lite Camera with Raspberry Pi 3 A+</i><br>
<br>

### Notes
- I've included a pdf that explains the steps I followed to install OpenCV on the Raspberry Pi.
- The process to install DepthAi on the Pi is not the same as for the Mac.
- These are the installation steps:

Step 1<br>
Docs: https://docs.luxonis.com/projects/api/en/latest/install/#install-from-pypi<br>
$ sudo curl -fL https://docs.luxonis.com/install_dependencies.sh | bash<br>

Step 2<br>
Docs: https://docs.luxonis.com/projects/api/en/latest/install/#install-from-pypi<br>
$ python3 -m pip install depthai<br>

Error Fix<br>
When running the python code I got this error:<br>
Failed to find device (ma2480), error message: X_LINK_DEVICE_NOT_FOUND<br>
Docs: https://docs.luxonis.com/en/latest/pages/troubleshooting/#failed-to-boot-the-device-1-3-ma2480-err-code-3

This is the fix from the Luxonis docs:

First unplug the Oak D Lite from the USB connection on the Raspberry Pi. Then type these two commands on the Pi command line:<br>
$ echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules<br>
$ sudo udevadm control --reload-rules && sudo udevadm trigger<br>


<br>
