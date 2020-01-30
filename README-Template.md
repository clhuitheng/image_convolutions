# Convolution Operator on input image

This is a project about applying the convolution operation on any input image in Python. 

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

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

