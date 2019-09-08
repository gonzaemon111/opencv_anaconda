{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import cv2\n",
    "\n",
    "img = np.zeros((400, 400, 3), np.uint8)\n",
    "cv2.circle(img, (200, 200), 50, (255, 0, 0), 1)\n",
    "cv2.imwrite('./images/circle1.jpg', img)\n",
    "cv2.imshow('img1', img)\n",
    "\n",
    "img = np.zeros((400, 400, 3), np.uint8)\n",
    "cv2.circle(img, (200, 200), 100, (0, 255, 0), 3)\n",
    "cv2.imwrite('./images/circle2.jpg', img)\n",
    "cv2.imshow('img2', img)\n",
    "\n",
    "img = np.zeros((400, 400, 3), np.uint8)\n",
    "cv2.circle(img, (200, 200), 150, (0, 0, 255), -1)\n",
    "cv2.imwrite('./images/circle3.jpg', img)\n",
    "cv2.imshow('img3', img)\n",
    "\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
