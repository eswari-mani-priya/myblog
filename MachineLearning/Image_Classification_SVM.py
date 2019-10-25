from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm, metrics, datasets
from sklearn.utils import Bunch
from sklearn.model_selection import GridSearchCV, train_test_split
from skimage.io import imread
from skimage.transform import resize
from sklearn.externals import joblib


def load_data(folder_path, dimension=(64, 64)):
    image_path = Path(folder_path)
    folders = [directory for directory in image_path.iterdir() if directory.is_dir()]
    print(folders)
    categories = [f.name for f in folders]
    print(categories)
    description = "An image classification dataset"
    images=[]
    flat_data = []
    target = []
    for i, direc in enumerate(folders):
        for file in direc.iterdir():
            img = imread(file)
            img_resized = resize(img, dimension, anti_aliasing=True, mode='reflect')
            flat_data.append(img_resized.flatten())
            images.append(img_resized)
            target.append(i)
    flat_data = np.array(flat_data)
    images = np.array(images)
    target = np.array(target)

    return categories, Bunch(data=flat_data, target=target, target_names=categories, images=images, DESCR=description)


def predict_custom_image(image):
    model = joblib.load('./models/svm_imageclf_model.pkl')
    img = imread(image)
    plt.imshow(img)
    plt.show()
    img_resized = resize(img, (64,64), anti_aliasing=True, mode='reflect')
    img_flat = img_resized.flatten().reshape(1,-1)
    prediction = model.predict(img_flat)
    return prediction


def main():
    categories, image_dataset = load_data('./svm_images')
    X_train, X_test, Y_train, Y_test = train_test_split(image_dataset.data, image_dataset.target, test_size=0.3, random_state=109)
    param_grid = [
        {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
        {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
        ]
    svc = svm.SVC()
    clf = GridSearchCV(svc, param_grid)
    clf.fit(X_train, Y_train)
    joblib.dump(clf, './models/svm_imageclf_model.pkl')
    y_pred = clf.predict(X_test)
    print("Classification report for - \n{}:\n{}\n".format(
        clf, metrics.classification_report(Y_test, y_pred)))
    predict = predict_custom_image('./images/pizza.jpg')
    print("Custom Prediction:", categories[predict[0]])


if __name__ == "__main__":
    main()

