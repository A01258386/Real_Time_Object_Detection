
Elephas maximus - v5 El-Max v5
==============================

This dataset was exported via roboflow.ai on March 23, 2022 at 9:09 PM GMT

It includes 99 images.
Elephas-maximus are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise
* Randomly crop between 20 and 81 percent of the image
* Random brigthness adjustment of between -74 and 0 percent
* Random Gaussian blur of between 0 and 10 pixels
* Salt and pepper noise was applied to 3 percent of pixels


