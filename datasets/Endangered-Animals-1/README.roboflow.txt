
merged-4 - v1 merged-v4
==============================

This dataset was exported via roboflow.ai on April 11, 2022 at 4:00 AM GMT

It includes 511 images.
Animals-All are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Randomly crop between 0 and 20 percent of the image
* Random rotation of between -45 and +45 degrees
* Random Gaussian blur of between 0 and 10 pixels
* Salt and pepper noise was applied to 5 percent of pixels


