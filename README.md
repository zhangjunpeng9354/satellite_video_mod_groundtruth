# Satellite Video MOD Groundtruth

This is a set of groundtruth on satellite video for evaluating moving object detection algorithm.

## What is included?

In this project, we annotate the moving vehicles on two satellite videos, each of whom contains 700 frames. 
The geo-territories of them are shown as below (Red for 001, and Green for 002).

![](/images/intro.png)

For each moving vehicle, a boundary box is provided across the video with an unique id, therefore this dataset can alse 
be used for evaluating multiple target tracking algorithm.

## How is the groundtruth built?

The boundary boxes are annotated on [Computer Vision Annotation Tool (CVAT)]((https://www.google.com)).

## How to use it?

Please refer to the [example](/example.py) file for more details.

## Citation

If you use this library for your publications, please cite it as:

```
@ARTICLE{8930094, 
author={J. {Zhang} and X. {Jia} and J. {Hu}}, 
journal={IEEE Transactions on Geoscience and Remote Sensing}, 
title={Error Bounded Foreground and Background Modeling for Moving Object Detection in Satellite Videos}, 
year={2019}, 
volume={}, 
number={}, 
pages={1-11}, 
doi={10.1109/TGRS.2019.2953181}, 
ISSN={1558-0644}, 
month={},}
```

Additional refereence:
```
@ARTICLE{9037205, 
author={J. {Zhang} and X. {Jia} and J. {Hu} and J. {Chanussot}}, 
journal={IEEE Transactions on Geoscience and Remote Sensing}, 
title={Online Structured Sparsity-Based Moving-Object Detection From Satellite Videos}, 
year={2020}, 
volume={}, 
number={}, 
pages={1-14}, 
doi={10.1109/TGRS.2020.2976855}, 
ISSN={1558-0644}, 
month={},}
```


