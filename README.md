# Convolution Operator on input image

This is a project about applying the convolution operation on any input image in Python with taking in user input image and user input fixed kernel 3x3 kernel values to perform the convolution on the input image.

### Prerequisites
To run this code, you will need python3 in your local machine. I have used and tested the code using the ClearLinux OS to run this convolution operation on a few input images. Before running the program,we need to make sure that the input image has to be placed with the same path as the image_convolutions.py.

### Steps to run
In this program, the project scope confine to a single channel image only which is the input image in greyscale.

The kernel size is fixed of 3x3, the fixed kernel stride of 1x1, same padding.

Let's consider we are going to perform convolution on image,frame07.png with a 

Sobel X Kernel: [-1 0 1 
                 -2 0 2
                 -1 0 1]

Image convolution operation with Sobel X Kernel using the command below:
```
python3 image_convolutions.py --image <frame07.png> -a11 <-1> -a12<0> -a13<1> -a21<-2> -a22<0> -a23<2> -a31<-1> -a32<0> -a33<1>
```

Let's consider we are going to perform convolution on image,frame07.png with a 

Sobel Y Kernel: [-1 -2 1
                 0 0 0
                 1 2 1]

Image convolution operation with Sobel Y Kernel:
```
python3 image_convolutions.py --image <image01.png> -a11 <-1> -a12<-2> -a13<1> -a21<0> -a22<0> -a23<0> -a31<1> -a32<2> -a33<1>
```

### References
1. Understanding Edge Detection Sobel Operator https://medium.com/datadriveninvestor/understanding-edge-detection-sobel-operator-2aada303b900

2. Sobel Operator https://www.tutorialspoint.com/dip/sobel_operator.htm

3. Adaptive Histogram Equalization https://en.wikipedia.org/wiki/Adaptive_histogram_equalization#Contrast_Limited_AHE

4. Histogram Equalization https://en.wikipedia.org/wiki/Histogram_equalization

5. Convolution Operation https://towardsdatascience.com/acomprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53 

6. Object Oriented Programming https://realpython.com/python3-object-oriented-programming/


