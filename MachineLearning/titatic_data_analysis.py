## __author__ == "Priya"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def age_plot(age_data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(age_data, bins=10, range=(age_data.min(), age_data.max()))
    plt.title("Titanic Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count of Passengers")
    plt.show()

def class_wise_survival(data):
    class_wise_count = data.groupby("Pclass").Survived.count()
    class_survived_probability = data.groupby("Pclass").Survived.sum()/data.groupby("Pclass").Survived.count()
    fig = plt.figure(figsize=(8,4))
    ax1 = fig.add_subplot(121)
    ax1.set_xlabel("PClass")
    ax1.set_ylabel("Count of Passengers")
    ax1.set_title("Passengers by Class")
    class_wise_count.plot(kind="bar", ax=ax1)


    ax2 = fig.add_subplot(122)
    ax2.set_xlabel("PClass")
    ax2.set_ylabel("Probability of Survival")
    ax2.set_title("Probability of Survival by Class")
    class_survived_probability.plot(kind="bar", ax=ax2)
    plt.show()


input_file = os.path.join(os.path.dirname(os.getcwd()), 'Titanic//train.csv')

#Reading file using pandas
data = pd.read_csv(input_file)
#print(data.describe())
#age_plot(data['Age'])
class_wise_survival(data)






