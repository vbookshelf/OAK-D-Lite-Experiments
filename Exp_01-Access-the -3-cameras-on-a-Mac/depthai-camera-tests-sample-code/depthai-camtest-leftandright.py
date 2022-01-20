# Ref: Depthai Baby Steps
# https://www.youtube.com/watch?v=e_uPEE_zlDo&list=PLfYPZalDvZDLOjzSkoHQ2_h4joHNUegbB&index=3


import depthai as dai
import cv2
import numpy as np
import time


# Set up a pipeline
pipeline = dai.Pipeline()


# Set up the left camera
mono_left = pipeline.createMonoCamera()
mono_left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
mono_left.setBoardSocket(dai.CameraBoardSocket.LEFT)


# Set up the right camera
mono_right = pipeline.createMonoCamera()
mono_right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
mono_right.setBoardSocket(dai.CameraBoardSocket.RIGHT)



# Set output XLink for the left camera
xout_left = pipeline.createXLinkOut()
xout_left.setStreamName("left")


# Set output XLink for the right camera
xout_right = pipeline.createXLinkOut()
xout_right.setStreamName("right")


# Attach the cameras to the output XLink
mono_left.out.link(xout_left.input)
mono_right.out.link(xout_right.input)


start_time = 0

# Pipe line is defined, now we can connect to the device
with dai.Device(pipeline) as device:
	
	# get output queues
	left_queue = device.getOutputQueue(name="left", maxSize=1)
	right_queue = device.getOutputQueue(name="right", maxSize=1)

	# set the display window name
	cv2.namedWindow("Stereo Pair")
	
	# variable to toggle between one frame view and side-by-side view
	side_by_side = True
	
	
	while True:
		
		# get the left frame
		left_frame = left_queue.get()
		# convert to OpenCV format
		left_frame = left_frame.getCvFrame()
		
		# get the right frame
		right_frame = right_queue.get()
		# convert to OpenCV format
		right_frame = right_frame.getCvFrame()
		

		if side_by_side:
			# stack the frames side by side
			image_out = np.hstack((left_frame, right_frame))
		else:
			# overlap the frames
			image_out = np.uint8(left_frame/2 + right_frame/2)
			
			
		# Get the frame rate
		current_time = time.time()
		fps = 1/(current_time - start_time)
		start_time = current_time
		# Uncomment this line to display the frame rate on the image (top left corner)
		cv2.putText(image_out, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255,255,255), 3)
			
			
		
		cv2.imshow("Stereo Pair", image_out)
		
		
		# check for keyboard input
		key = cv2.waitKey(1)
		if key == ord('q'):
			# quit when 'q' is pressed
			break
		elif key == ord('t'):
			# toggle display when 't' is pressed by changing the side_by_side to True and False
			side_by_side = not side_by_side






