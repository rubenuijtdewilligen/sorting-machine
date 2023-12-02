import cv2
import numpy as np
import requests

# Function to detect red and blue objects
def detect_objects(frame):
    # Convert the frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the ranges for red and blue colors in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    lower_blue = np.array([70, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create masks to extract red and blue regions
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply masks to the original frame
    result_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    result_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    return result_red, result_blue

# Function to check if an object is present
def check_object_presence(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the grayscale image
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contours are present
    return len(contours) > 0

# Open the video capture (change 0 to the video file path if using a file)
cap = cv2.VideoCapture(1)

while True:
    # Read a frame from the video capture
    ret, img = cap.read()
    frame = img[150:260, 280:440]

    if not ret:
        break

    # Detect red and blue objects in the frame
    result_red, result_blue = detect_objects(frame)

    # Display the original frame, red objects, and blue objects
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Red Objects', result_red)
    cv2.imshow('Blue Objects', result_blue)

    # Check if a blue object is present in the frame every second
    # if time.time() % 1 == 0:
    blue_object_present = check_object_presence(result_blue)

    if blue_object_present:
        requests.get(url = 'http://peperman:3000/trigger')

    # Break the loop when q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
