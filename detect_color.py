# USAGE
# python detect_color.py --image pokemon_games.png

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
    ([0, 0, 0], [55, 55, 55]),
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    small = cv2.resize(image, (0,0), fx=0.25, fy=0.25)
    small_output = cv2.resize(output, (0,0), fx=0.25, fy=0.25)

    # show the images
    cv2.namedWindow('images', cv2.WINDOW_NORMAL)
    cv2.imshow("images", np.hstack([small, small_output]))
    cv2.waitKey(0)
