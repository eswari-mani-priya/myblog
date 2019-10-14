from sklearn import linear_model, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score


def get_predict_values(model, test_data):
    return model.predict(test_data)


def train_model(model, train_data_x, train_data_y):
    model.fit(train_data_x, train_data_y)


def get_mean_square_error(y_test, y_pred):
    return mean_squared_error(y_test, y_pred)


def get_r2_score(y_test, y_pred):
    return r2_score(y_test, y_pred)


def show_plot(x_test, y_test, y_pred):
    plt.scatter(x_test, y_test, color='red')
    plt.plot(x_test, y_pred, color="green", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def main():
    dataset = datasets.load_diabetes()
# Get single feature from dataset
    X = dataset.data[:, np.newaxis, 2]
    X_train = X[:-20]
    X_test = X[-20:]
    Y_train = dataset.target[:-20]
    Y_test = dataset.target[-20:]
    model = linear_model.LinearRegression()
    train_model(model, X_train, Y_train)
    Y_pred = get_predict_values(model, X_test)
    coeffs = model.coef_
    print("Coeffs: ", coeffs)
    merr = get_mean_square_error(Y_test, Y_pred)
    print("Mean Square Error: ", merr)
    variance = get_r2_score(Y_test, Y_pred)
    print("Variance Score: ", variance)
    show_plot(X_test, Y_test, Y_pred)


if __name__ == "__main__":
    main()
