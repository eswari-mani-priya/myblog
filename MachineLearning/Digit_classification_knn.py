# https://towardsdatascience.com/scanned-digits-recognition-using-k-nearest-neighbor-k-nn-d1a1528f0dea
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import datasets, decomposition
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.externals import joblib
from skimage.transform import resize
from skimage import color, exposure


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
    joblib.dump(model, './models/knn_model.pkl')
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


def feature_extraction(image):
    plt.imshow(color.rgb2gray(image))
    plt.show()
    return

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def predict(model, image):
    df = rgb2gray(cv2.imread(image))
    # print("Shape before resize: ", df.shape)
    df = (8 - df * 8).astype(int)
    plt.imshow(df, cmap=plt.get_cmap('gray_r'))
    plt.show()
    print("Shape after resize: ", df.shape)
    df = df.flatten().reshape(1, -1)
    plt.imshow(df)
    plt.show()
    print("Shape after reshape: ", df.shape)
    predict = model.predict(df)[0]
    predict_proba = model.predict_proba(df.reshape(1, -1))
    return predict, predict_proba[0][predict]


def get_prediction_realtime(image):
    model = joblib.load('./models/knn_model.pkl')
    feature_extraction(cv2.imread(image))
    predictions = predict(model, image)
    print("Predict:", predictions[0])
    print("Predict Probability: ", predictions[1])


def main():
    dataset = datasets.load_digits()
    trainData, testData, valData, trainLabels, testLabels, valLabels = get_train_test_data(dataset)
    k_range = range(1, 30, 2)
    k_max = get_k_for_max_accuracy(k_range, trainData, trainLabels, valData, valLabels)
    model, prediction = get_prediction_with_max_k(k_max, trainData, trainLabels, testData)
    if len(sys.argv) >= 2:
        get_prediction_realtime(sys.argv[1])
    else:
        cls_report, cnf_matrix = get_classify_report(prediction, testLabels)
        print("Classification Report: \n", cls_report)
        print("Confusion Matrix: \n", cnf_matrix)
        show_predictions(model, testData, testLabels)


if __name__ == "__main__":
    main()

