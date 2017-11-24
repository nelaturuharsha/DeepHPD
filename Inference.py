"""
Run the online classification system.

Capture an image, classify, do it again.
"""
import time
#from picamera import PiCamera
#from picamera.array import PiRGBArray
import tensorflow as tf
import cv2
import os

def get_labels():
    """Get a list of labels so we can see if it's an ad or not."""
    with open('./inception/retrained_labels.txt', 'r') as fin:
        labels = [line.rstrip('\n') for line in fin]
    return labels

def run_classification(labels):
    """Stream images off the camera and process them."""

    with tf.gfile.FastGFile("./inception/retrained_graph.pb", 'rb') as fin:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fin.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # And capture continuously forever.
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        #for video in os.listdir("./predictimage"):
        cam = cv2.VideoCapture("0")
        while True:
            ret, frame = cam.read()
            #frame = cv2.resize(frame, (1920, 1080))
            #cv2.imshow("frame", frame)
            decoded_image = frame

        # Make the prediction. Big thanks to this SO answer:
        # http://stackoverflow.com/questions/34484148/feeding-image-data-in-tensorflow-for-transfer-learning
            predictions = sess.run(softmax_tensor, {'DecodeJpeg:0': decoded_image})
            prediction = predictions[0]

            # Get the highest confidence category.
            prediction = prediction.tolist()
            max_value = max(prediction)
            max_index = prediction.index(max_value)
            predicted_label = labels[max_index]
            #return (predicted_label)
            #print("%s (%.2f%%)" % (predicted_label, max_value * 100))
            return(predicted_label)
            # Reset the buffer so we're ready for the next one.
            #raw_capture.truncate(0)

if __name__ == '__main__':
    run_classification(get_labels())
