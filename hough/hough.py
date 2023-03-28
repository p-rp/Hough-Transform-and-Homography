# import other necessary libaries
from utils import create_line, create_mask
from skimage import io
from skimage.feature import peak_local_max
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# load the input image
img = io.imread('hough/road.jpg')

# run Canny edge detector to find edge points
edges = cv.Canny(img, 40, 140)

# create a mask for ROI by calling create_mask
mask = create_mask(img.shape[0], img.shape[1])

# extract edge points in ROI by multipling edge map with the mask
edges_ROI = edges * mask

# perform Hough transform
width, height, _ = img.shape
diagnoal_len = int(np.round(np.sqrt(width ** 2 + height ** 2)))     
thetas = np.deg2rad(np.arange(0, 180))
rhos = np.linspace(-diagnoal_len, diagnoal_len, 2*diagnoal_len)
accumulator = np.zeros((2 * diagnoal_len, len(thetas)))     # Initialize accumulator H to all zeros

for y in range(width):              # For each edge point (x,y) in the image
     for x in range(height):
          if edges_ROI[y,x] > 0:    # Check if it is an edge pixel
              for theta in range(len(thetas)):     # theta 0 to 180
                    rho = x*np.cos(thetas[theta]) + y * np.sin(thetas[theta])
                    accumulator[int(rho) + diagnoal_len,theta] += 1

# find the right lane by finding the peak in hough space
peak_rho, peak_theta = np.unravel_index(accumulator.argmax(), accumulator.shape)
x1, y1 = create_line(rhos[peak_rho], thetas[peak_theta], edges_ROI)

# zero out the values in accumulator around the neighborhood of the peak
radius_y = 5
radius_x = 25
for x in range(peak_rho-radius_x, peak_rho+radius_x):
    for y in range(peak_theta-radius_y, peak_theta+radius_y):
        accumulator[x, y] = 0
        
# find the left lane by finding the peak in hough space
peak_rho, peak_theta = np.unravel_index(accumulator.argmax(), accumulator.shape)
x2, y2 = create_line(rhos[peak_rho], thetas[peak_theta], edges_ROI)

# plot the results
rows = 2
columns = 2

plt.subplot(rows, columns, 1)
plt.imshow(edges, cmap='gray')
plt.title('Edges')
plt.axis('off')

plt.subplot(rows, columns, 2)
plt.imshow(mask, cmap='gray')
plt.title('Mask')
plt.axis('off')

plt.subplot(rows, columns, 3)
plt.imshow(edges_ROI, cmap='gray')
plt.title('Edges in ROI')
plt.axis('off')

plt.subplot(rows, columns, 4)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.imshow(img, cmap='gray')
plt.title('Hough Transform')
plt.axis('off')

plt.show()