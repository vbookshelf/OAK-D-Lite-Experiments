
# Ref: Depthai Baby Steps
# https://www.youtube.com/watch?v=e_uPEE_zlDo&list=PLfYPZalDvZDLOjzSkoHQ2_h4joHNUegbB&index=3


import depthai as dai
import cv2
import numpy as np




pipeline = dai.Pipeline()

# Connect the host (pc or pi) to the camera on the device (camera)
# by creating an XLinkIn node.
# XLinkIn is an input to the device (camera).
mono = pipeline.createMonoCamera()
# set the resolution of the mono camera to be 400 pixels across.
# There are different options: 400, 720, 800
mono.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
# specify that we are using the left camera
mono.setBoardSocket(dai.CameraBoardSocket.LEFT)


# Create an XLinkOut
# We name the output because there could be several outputs e.g. right camera, left camera etc.
xout = pipeline.createXLinkOut()
xout.setStreamName("left")
# link the mono camera to the output
# Take the output of the mono camera and
# put it as the input to the XLinkOut.
mono.out.link(xout.input)


# transfer the pipeline onto the device (camera)
with dai.Device(pipeline) as device:
	
	# query the XLinkOut to get our frame
	# The output is a queue that can have many frames.
	# maxSize=1 means we only want one frame in the queue.
	# "left" is the name we used to set the stream name.
	queue = device.getOutputQueue(name="left", maxSize=1)
	
	# set the display window name
	cv2.namedWindow("Left Cam")
	
	while True:
	
		# Get one frame from the queue.
		# The frame is transferred from the device into the host.
		frame = queue.get()
		
		# getCvFrame() converts the frame into OpenCV (cv2) format.
		imOut = frame.getCvFrame()
		
		cv2.imshow("Left Cam", imOut)
		
		key = cv2.waitKey(1)
		if key == ord('q'):
			break
		
	
	