# DeepHPD - Deep Human Presence Detection

Contributers : [Sree Harsha Nelaturu](https://github.com/TheBigFundamental), [Anith Patel](https://github.com/anithp), [Avyay Sah](https://github.com/avyay1997)

DeepHPD is a novel application which uses Deep Learning in order to detect the presence of a human being. This is done by using a combination of Convolutional Neural Networks and OpenCV which along with a Raspberry pi and Basler Dart Camera, which blinks an LED when it detects human presence.



Software Used : 
<ul>
<li> Tensorflow
<li> OpenCV
<li> Numpy
<li> RPi-GPIO
<li> CUDA
</ul>

The two classes provided by the classifier are:
<ol>
<li> human
<li> nohuman
</ol>
For running the project,
Key files required are :
<ol>
<li> Inference.py - Uses weights of trained Convolutional Neural Network for classification
<li> LED-Blink.py - Script to be run to use inferred labels from footage in order to detect humans and blink LED
</ol>
Once these resources are compiled, run LED-Blink.py to access the program.

Sample:
[INPUT]
Footage via Basler DART is taken via OpenCV

[OUTPUT]
Label : "human"
LED Blinks
