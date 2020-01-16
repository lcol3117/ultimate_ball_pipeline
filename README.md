# ultimate_ball_pipeline
UBP is a computer vision pipeline for tracking yellow balls extremely reliably, such as those in the 2020 FRC game. 

This is designed to run on the OpenMV M7

The pipeline: 

Convert to HSV colorspace 
Threshold HSV
Erosion 
Dilation 
Dilation
Erosion
EDT (Euclidean Distance Transform)
Pass into step function
Hough Circle Detection
