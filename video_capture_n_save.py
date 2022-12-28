import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Camera is unable to open.")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
video_cod = cv2.VideoWriter_fourcc(*'XVID')
video_output= cv2.VideoWriter('captured_video.avi', video_cod, 10, (frame_width,frame_height))

while(True):
  ret, frame = cap.read()

  if ret == True: 
    # Write the frame into the file 'captured_video.avi'
    video_output.write(frame)
    # Display the frame   
    cv2.imshow('frame',frame)
    # Press x on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('x'):
      break

  else:
    break 
   
cap.release()
video_output.release()
cv2.destroyAllWindows() 
print("The video was successfully saved")  
