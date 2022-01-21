



import cv2
import mediapipe as mp
import numpy as np
import time

import depthai as dai



# Define the colours
WHITE_COLOR = (224, 224, 224)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 128, 0)
BLUE_COLOR = (255, 0, 0)



# Set up the depthai pipeline
# ..................................
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

# .....................................




# to draw the landmarks
mp_draw = mp.solutions.drawing_utils

# Set the drawing specs.
# the defaults also look fine.
draw_specs = mp_draw.DrawingSpec(color=WHITE_COLOR, thickness=2, circle_radius=2)

mp_pose = mp.solutions.hands
pose = mp_pose.Hands(static_image_mode=False,
               max_num_hands=1,
               min_detection_confidence=0.85,
               min_tracking_confidence=0.5)





# A video is just a sequence of images.
# Create a loop to loop through each image.

start_time = 0

# Pipe line is defined, now we can connect to the device
with dai.Device(pipeline) as device:
	
	# get output queue
	rgb_queue = device.getOutputQueue(name="rgb", maxSize=1)
	
	# set the display window name
	cv2.namedWindow("Feed from Oak D Lite")

	while True:
		
		# tryGet() will return the data or None if there isn't any
		rgb_frame = rgb_queue.tryGet()
		
		if rgb_frame is not None:
		
			# convert to OpenCV format
			image = rgb_frame.getCvFrame()
			
			# flip the image so that it's like looking in a mirror.
			image = cv2.flip(image, 1)
			
			
		
		
			# Convert the image from BGR to RGB.
			# Note that we don't display this RGB image. We display
			# the original BGR image.
			image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		
			# process the image and store the results in an object
			results = pose.process(image_rgb)
		
			
			# draw a rectangle on the screen
			cv2.rectangle(image, (25, 130), (100, 200), BLUE_COLOR, cv2.FILLED)
			
			
		
		
			# This is how to create a black background and
			# a white background.
			h, w, c = image.shape
			black_image = np.zeros((h, w, c))
			white_image = np.zeros((h, w, c)) + 255
		
			# Choose to display the original image or show the hand landmarks
			# against a black or a white background.
			display_image = image
			#display_image = black_image
			# display_image = white_image
		
		
		
			#print(results.multi_hand_landmarks)
		
		
		
			if results.multi_hand_landmarks:
		
				# We can have multiple hands.
				# Therefore, we need to loop through the hands
				for hand_landmarks in results.multi_hand_landmarks:
					
					x_list = []
					y_list = []
					fingers_up = [0,0,0,0,0]
		
					# draw the lanmarks on the image as dots only
					#mp_draw.draw_landmarks(display_image, hand_landmarks)
		
		
					# draw dots and the connections between them
					mp_draw.draw_landmarks(display_image, hand_landmarks, mp_pose.HAND_CONNECTIONS,
										draw_specs, draw_specs)
		
		
					# Get each separate point.
					# We can put the ids into a list and return them.
					for id, lm in enumerate(hand_landmarks.landmark):
		
						# These values have been normalized from 0 to 1.
						# We need to convert them to coordinates.
						#print(lm)
		
						# convert to coordinates
						h, w, c = image.shape
						x = int(lm.x * w)
						y = int(lm.y * h)
		
						#print(id, x, y)
						
						# add the x and y coords to a list
						x_list.append(x)
						y_list.append(y)
						
							
		
					#print(y_list)
					
					# This is how we check if a finger or the thumb is
					# up or down.
					# ......................................
					
					# By following this link you will find a diagram that shows which index values
					# correspond to which points on a hand:
					# https://google.github.io/mediapipe/solutions/hands#resources
					
					# The origin point (0,0) on images is in the top left corner.
					# Using the index finger as an example, if the y coord of
					# point 8 is less than or equal to the y coord of point 6 then
					# we say that the finger is up. The same applies to the other fingers.
					
					# For the thumb if the x coord of point 4 is less than or equal to 
					# the x coord of point 5 then we say that the thumb is up.
					
					# thumb
					if x_list[4] <= x_list[5]:
						fingers_up[0] = 1
					
					if y_list[8] <= y_list[6]:
						fingers_up[1] = 1
					
					if y_list[12] <= y_list[10]:
						fingers_up[2] = 1
						
					if y_list[16]  <= y_list[14]:
						fingers_up[3] = 1
						
					if y_list[20] < y_list[18]:
						fingers_up[4] = 1
						
					# print the list
					print(fingers_up)
					
					# sum the list to get the number of fingers that are up
					num_fingers_up = sum(fingers_up)
					
					
					
					
					# write the number of fingers onto the webccam image
					cv2.putText(image, str(num_fingers_up), (50, 180), cv2.FONT_HERSHEY_PLAIN, 3,
					WHITE_COLOR, 3)
		
		
			# Get the frame rate
			current_time = time.time()
			fps = 1/(current_time - start_time)
			start_time = current_time
		
			# Uncomment this line to display the frame rate on the image (top left corner)
			cv2.putText(display_image, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255,255,255), 3)
		
		
			# Display the webcam video frame
			cv2.imshow('Feed from Oak D Lite', display_image)
		
		
		
			# Press q on the keyboard to close the video
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			