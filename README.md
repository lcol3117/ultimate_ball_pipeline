# ultimate_ball_pipeline
UBP is a computer vision pipeline for tracking yellow balls extremely reliably, such as those in the 2020 FRC game. 

This is designed to run on the OpenMV M7

The pipeline: 

Convert to LAB colorspace 
Threshold LAB
Erosion 
Dilation
Erosion
Blob Detection 
-limit to circles
If multiple in Frame, use largest
output data

Outputs: 
Image: Red circle indicates ball
Onboard LED: 
-off=no target
-red=left side target
-green=right side target

Outputs x coord of target over I2C
