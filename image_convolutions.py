from skimage import io, color
from skimage import exposure

import argparse
import matplotlib.pyplot as plt
import numpy as np

def convolve(image, kernel):
    # This function takes in 2 arguments which are the input image and kernel
    # and returns the convolution of them
    # Args:
    #    image: a numpy array of size [image_height, image_width].
    #    kernel: a numpy array of size [kernel_height, kernel_width].
    # Returns:
    #    a numpy array of size [image_height, image_width] (convolution output)

    # the dimensions of input image
    (iH, iW) = image.shape[:2]

    # the dimensions of kernel
    (kH, kW) = kernel.shape[:2]

    # convolution output
    output = np.zeros_like(image)

    # Add zero padding to the input image
    image_padded = np.zeros((iH + 2, iW + 2))

    image_padded[1:-1, 1:-1] = image

    # Loop over every pixel of the image
    for x in range(iW):
        for y in range(iH):
            # element-wise multiplication of the kernel and the image
            output[y, x] = (kernel * image_padded[y:y + 3, x:x + 3]).sum()
    return output

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")

ap.add_argument('-a11', required=True, help='a11')
ap.add_argument('-a12', required=True, help='a12')
ap.add_argument('-a13', required=True, help='a13')

ap.add_argument('-a21', required=True, help='a21')
ap.add_argument('-a22', required=True, help='a22')
ap.add_argument('-a23', required=True, help='a23')

ap.add_argument('-a31', required=True, help='a31')
ap.add_argument('-a32', required=True, help='a31')
ap.add_argument('-a33', required=True, help='a33')

args = vars(ap.parse_args())

kernel = np.array((
    [args['a11'], args['a12'], args['a13']],
    [args['a21'], args['a22'], args['a23']],
    [args['a31'], args['a32'], args['a33']]), dtype='int')

print("[INFO] Applying Kernel: ", kernel)

# Load the input image
image = io.imread(args['image'])

# Convert the image to grayscale (1 channel)
image = color.rgb2gray(image)

convolveOutput = convolve(image, kernel)

# Plot the filtered image
plt.title("convolveOutput")
plt.imshow(convolveOutput, cmap=plt.cm.gray)
plt.axis('off')
plt.show()

# Adjust the contrast of the filtered image by applying Histogram Equalization
image_sharpen_equalized = exposure.equalize_adapthist(
    convolveOutput / np.max(np.abs(convolveOutput)), clip_limit=0.03)
plt.title("image_sharpen_equalized")
plt.imshow(image_sharpen_equalized, cmap=plt.cm.gray)
plt.axis('off')
plt.show()
