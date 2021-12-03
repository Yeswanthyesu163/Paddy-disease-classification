from PIL import Image
from io import BytesIO
import os
import tensorflow as tf
import numpy as np
import cv2

#Read the file Uploaded by the User
def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image


def predict_image(image: Image.Image):
    RETRAINED_LABELS_TXT_FILE_LOC = os.getcwd() + "/" + "retrained_labels.txt"
    RETRAINED_GRAPH_PB_FILE_LOC = os.getcwd() + "/" + "retrained_graph.pb"
    # get a list of classifications from the labels file
    classifications = []
    # for each line in the label file . . .
    for currentLine in tf.gfile.GFile(RETRAINED_LABELS_TXT_FILE_LOC):
        # remove the carriage return
        classification = currentLine.rstrip()
        # and append to the list
        classifications.append(classification)
    # end for

    # load the graph from file
    with tf.gfile.FastGFile(RETRAINED_GRAPH_PB_FILE_LOC, 'rb') as retrainedGraphFile:
        # instantiate a GraphDef object
        graphDef = tf.GraphDef()
        # read in retrained graph into the GraphDef object
        graphDef.ParseFromString(retrainedGraphFile.read())
        # import the graph into the current default Graph, note that we don't need to be concerned with the return value
        _ = tf.import_graph_def(graphDef, name='')
    with tf.Session() as sess:
        dic = {}
        finalTensor = sess.graph.get_tensor_by_name('final_result:0')
        # convert the OpenCV image (numpy array) to a TensorFlow image
        tfImage = np.array(image)[:, :, 0:3]

        # run the network to get the predictions
        predictions = sess.run(finalTensor, {'DecodeJpeg:0': tfImage})

        # sort predictions from most confidence to least confidence
        sortedPredictions = predictions[0].argsort()[-len(predictions[0]):][::-1]
        onMostLikelyPrediction = True
        for prediction in sortedPredictions:
            strClassification = classifications[prediction]
            # if the classification (obtained from the directory name) ends with the letter "s", remove the "s" to change from plural to singular
            if strClassification.endswith("s"):
                strClassification = strClassification[:-1]
            # end if
            confidence = predictions[0][prediction]
            presentedAsAPercent = confidence * 100.0
            if onMostLikelyPrediction:
                # get the score as a %
                scoreAsAPercent = confidence * 100.0
                # show the result to std out
                dic["message"] = "the object appears to be a " + strClassification + ", " + "{0:.2f}".format(scoreAsAPercent) + "% confidence"
                onMostLikelyPrediction = False
            # get confidence, then get confidence rounded to 2 places after the decimal
            confidence = predictions[0][prediction]
            presentedAsAPercent = confidence * 100.0

            dic[strClassification] = presentedAsAPercent
    return dic