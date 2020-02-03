from skimage import io, color
from skimage import exposure

import matplotlib.pyplot as plt
import argparse
import numpy as np

class PlotImage:
    def __init__(self, image):
        self.image = image

    def ShowTitle(self, title):
        plt.title(title)
        plt.imshow(image.GetCurrentImage(), cmap=plt.cm.gray)
        plt.axis('off')
        plt.show()

class InputImage:
    # constructor
    def __init__(self, imagepath):
        self.image = io.imread(imagepath)

    def ConvertToGrayScale(self):
      # Convert the image to grayscale (1 channel)
      self.image = color.rgb2gray(self.image)

    def GetCurrentImage(self):
        return self.image

    def GenerateZerosLikeImage(self):
        return np.zeros_like(self.image)

    def GeneratePaddedImage(self, iH, iW):
        image_padded = np.zeros((iH + 2, iW + 2))
        image_padded[1:-1, 1:-1] = self.image

        return image_padded

    def Convolve(self, kernel):
        # the dimensions of input image
        (iH, iW) = self.image.shape[:2]

        # the dimensions of kernel
        (kH, kW) = kernel.shape[:2]

        # convolution output
        output = self.GenerateZerosLikeImage()

        # Add zero padding to the input image
        image_padded = self.GeneratePaddedImage(iH, iW)

        # Loop over every pixel of the image
        for x in range(iW):
            for y in range(iH):
                # element-wise multiplication of the kernel and the image
                output[y, x] = (kernel * image_padded[y:y + 3, x:x + 3]).sum()

        self.image = output
        return output

    def ApplyHistogramEqualization(self):
      self.image = exposure.equalize_adapthist(self.image /
                                               np.max(np.abs(self.image)),
                                               clip_limit=0.03)

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

image = InputImage(args['image'])

# Convert the image to grayscale (1 channel)
image.ConvertToGrayScale()

# Apply Convolution
image.Convolve(kernel)

# Plot the filtered image
imageGraph = PlotImage(image)
imageGraph.ShowTitle("ConvolveOutput")

# Adjust the contrast of the filtered image by applying Histogram Equalization
image.ApplyHistogramEqualization()
imageGraph.ShowTitle("image_sharpen_equalized")
