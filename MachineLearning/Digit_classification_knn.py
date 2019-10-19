# https://towardsdatascience.com/scanned-digits-recognition-using-k-nearest-neighbor-k-nn-d1a1528f0dea
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import datasets
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys


def get_train_test_data(dataset):
    (trainData, testData, trainLabels, testLabels) = train_test_split(np.array(dataset.data), dataset.target,
                                                                      test_size=0.25, random_state=42)

    (trainData, valData, trainLabels, valLabels) = train_test_split(trainData, trainLabels, test_size=0.1,
                                                                    random_state=84)
    return trainData, testData, valData, trainLabels, testLabels, valLabels


def get_k_for_max_accuracy(k_range, trainData, trainLabels, valData, valLabels):
    accuracies = []
    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(trainData, trainLabels)
        score = model.score(valData, valLabels)
        print("k=%d, accuracy=%.2f%%" % (k, score*100))
        accuracies.append(score)
    i = np.argmax(accuracies)
    print("k=%d achieved maximum accuracy of %.2f%% on validation data" % (k_range[i], accuracies[i] * 100))
    return k_range[i]


def get_prediction_with_max_k(k, trainData, trainLabels, testData):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(trainData, trainLabels)
    prediction = model.predict(testData)
    return model, prediction


def get_classify_report(prediction, testLabels):
    classify_report = classification_report(testLabels, prediction)
    conf_matrix = confusion_matrix(testLabels, prediction)
    return classify_report, conf_matrix

def show_predictions(model, testData, testLabels):
    for i in np.random.randint(0, high=len(testLabels), size=(5,)):
        data = testData[i]
        print(data.shape)
        predict = model.predict([data])[0]
        image_data = np.array(data, dtype='float')
        img_reshaped = image_data.reshape((8,8))
        plt.imshow(img_reshaped, cmap='gray')
        plt.annotate(predict, (3,3), bbox={'facecolor':'white'}, fontsize=32)
        print("I think the digit is: ", predict)
        plt.show()
        cv2.waitKey(0)


def get_prediction_realtime(model, image):
    img = Image.open(image)
    img.load()
    img = np.resize(img, (64,))
    predict = model.predict([img])[0]
    im2arr = np.array(img, dtype="float64")
    im2arr = im2arr.reshape((8, 8))
    plt.imshow(im2arr, cmap='gray')
    plt.annotate(predict, (3,3), bbox={'facecolor':'white'}, fontsize=32)
    print("I think digit is: ", predict)
    plt.show()



def main():
    dataset = datasets.load_digits()
    trainData, testData, valData, trainLabels, testLabels, valLabels = get_train_test_data(dataset)
    k_range = range(1, 30, 2)
    k_max = get_k_for_max_accuracy(k_range, trainData, trainLabels, valData, valLabels)
    model, prediction = get_prediction_with_max_k(k_max, trainData, trainLabels, testData)
    if len(sys.argv) >= 2:
        get_prediction_realtime(model, sys.argv[1])
    else:
        cls_report, cnf_matrix = get_classify_report(prediction, testLabels)
        print("Classification Report: \n", cls_report)
        print("Confusion Matrix: \n", cnf_matrix)
        show_predictions(model, testData, testLabels)


if __name__ == "__main__":
    main()

