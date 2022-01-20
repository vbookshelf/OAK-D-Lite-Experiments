
import depthai as dai
import cv2
import numpy as np
import time

# Set up a pipeline
pipeline = dai.Pipeline()

# set up the rgb camera
cam_rgb = pipeline.createColorCamera()
# This sets the size of the preview window. Is the resolution always 4k?
cam_rgb.setPreviewSize(640, 480) # (w, h)
cam_rgb.setInterleaved(False)

# Set output XLink for the rgb camera
xout_rgb = pipeline.createXLinkOut()
xout_rgb.setStreamName("rgb")

# Attach the camera to the output XLink
cam_rgb.preview.link(xout_rgb.input)

start_time = 0


# Pipe line is defined, now we can connect to the device
with dai.Device(pipeline) as device:
	
	# get output queue
	rgb_queue = device.getOutputQueue(name="rgb", maxSize=1)
	
	# set the display window name
	cv2.namedWindow("RGB Image")
	
	while True:
		# tryGet() will return the data or None if there isn't any
		rgb_frame = rgb_queue.tryGet()
		
		if rgb_frame is not None:
			# convert to OpenCV format
			image_out = rgb_frame.getCvFrame()
			
			# shape is 480 x 640 x 3
			#print(image_out.shape)
			
			# Get the frame rate
			current_time = time.time()
			fps = 1/(current_time - start_time)
			start_time = current_time
			# Uncomment this line to display the frame rate on the image (top left corner)
			cv2.putText(image_out, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255,255,255), 3)
			
			
			# display the image
			cv2.imshow("RGB Image", image_out)
		
		
		# check for keyboard input
		key = cv2.waitKey(1)
		if key == ord('q'):
			# quit when 'q' is pressed
			break
			
			
			
			
			