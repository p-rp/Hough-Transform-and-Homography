# Computer Vision Project: Hough Transform and RANSAC Homography

This repository contains implementations of computer vision techniques such as **Hough Transform** for lane detection and **RANSAC** for estimating homography, used in augmented reality applications. The project demonstrates how these algorithms can be applied to real-world scenarios like detecting lanes in road images and overlaying images using homography.

### Dependencies

To run the code in this repository, ensure you have the following Python libraries installed:

- `numpy`
- `matplotlib`
- `opencv-python`
- `scikit-image`

Install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

## Hough Transform for Lane Detection

This part of the project implements the **Hough Transform** to detect straight lanes in road images. The process involves the following steps:

1. **Edge Detection**: Detect edges in the image using the Canny edge detector.
2. **ROI Masking**: Apply a region of interest (ROI) mask to focus on the relevant portion of the image.
3. **Hough Space Voting**: Use the Hough Transform to detect lines in polar coordinates (ρ, θ).
4. **Non-Max Suppression**: Identify the two most prominent lanes by suppressing neighboring cells in the Hough space.

#### Running the code:

```bash
cd hough
python hough.py
```

This will process the image `road.jpg` and display the results, including edge detection and lane detection.

## RANSAC Homography for Augmented Reality

This part of the project focuses on estimating the homography between two images and applying it to a basic augmented reality application. The steps involved include:

1. **Feature Matching**: Use SIFT to detect and match key points between two images.
2. **RANSAC for Homography Estimation**: Implement the RANSAC algorithm to compute the homography matrix, minimizing the effect of outliers.
3. **Image Warping and Composition**: Warp the template image using the computed homography and overlay it onto the target image.

#### Running the code:

```bash
cd homography
python run.py
```

This will compute the homography matrix and produce the augmented reality output by replacing the cover of one book with another.

## Results

The project generates visual outputs showcasing lane detection on road images and augmented reality results where one book cover is replaced by another using homography. These results can be visualized by running the scripts in the respective directories.
