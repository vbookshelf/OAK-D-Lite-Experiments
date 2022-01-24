## Exp_05 - Explore how image pre-processing is being handled in hello_world.py

### Objective
- Try to understand how the image pre-processing is being accompished in the hello_world.py example.

### Notes
- The hello_world.py example uses a mobilenet-ssd model from OpenVINO. This is the model info page:<br>
https://docs.openvino.ai/latest/omz_models_model_mobilenet_ssd.html

- According to the info page, the input image format needs to be as follows:<br>
a) size 300x300<br>
b) normalized (subtract [127.5, 127.5, 127.5] and divide by 0.007843)<br>
c) BGR<br>

- By reviewing the hello_world.py code it's not possible to see how the input image has been normalized and the format converted from RBR to BGR before the image is fed into the model.

- There appears to be three possible ways that this could have been done:<br>
1. Make the pre-processing steps a part of the model architecture as described here:<br>
https://opencv.org/openvino-merging-pre-and-post-processing-into-the-model/

2. Use the Preprocessors class in OpenVINO. More info here:<br>
https://docs.openvino.ai/latest/omz_tools_accuracy_checker_preprocessor.html

3. Use the Script node. The Script node allows users to run custom Python scripts on the device.<br>
https://docs.luxonis.com/projects/api/en/latest/components/nodes/script/#how-to-place-it

### Takeaway

- When building custom models that will be run on the Oak D Lite, try to ensure the image pre-processing steps are included in the model architecture.
