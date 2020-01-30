# Convolution Operator on input image

This is a project about applying the convolution operation on any input image in Python with taking in user input image and user input fixed kernel 3x3 kernel values to perform the convolution on the input image.

### Prerequisites
To run this code, you will need python3 in your local machine. I have used and tested the code using the ClearLinux OS to run this convolution operation on a few input images. Before running the program,we need to make sure that the input image has to be placed with the same path as the image_convolutions.py.

### Steps to run
In this program, the project scope confine to a single channel image only which is the input image in greyscale.

The kernel size is fixed of 3x3, the fixed kernel stride of 1x1, same padding.

Image convolution operation with Sobel X Kernel using the command below:
```
python3 image_convolutions.py --image <image01.png> -a11 <1> -a12<0> -a13<1> -a21<-2> -a22<0> -a23<2> -a31<1> -a32<0> -a33<1>
```
Image convolution operation with Sobel Y Kernel:
```
python3 image_convolutions.py --image <image01.png> -a11 <-1> -a12<-2> -a13<-1> -a21<0> -a22<0> -a23<0> -a31<1> -a32<2> -a33<1>
```

End with an example of getting some data out of the system or using it for a little demo

```

## Authors

* **Chew Leong Hui Theng** - *Initial work* -(https://github.com/clhuitheng/image_convolutions)
