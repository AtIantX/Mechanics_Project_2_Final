import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class Prediction:
    force_acceleration_data = "Simulation_results/force_acceleration.csv"
    df = None
    clf = None

    @staticmethod
    def read_data():
        df = pd.read_csv(Prediction.force_acceleration_data)
        return df

    @staticmethod
    def predict_acceleration(force):
        Prediction.train_model()
        acc = Prediction.clf.predict(force)
        return acc

    @staticmethod
    def train_model():
        df = Prediction.read_data()
        x = np.array(df["External_Force"])
        y = np.array(df['Acceleration of Object 2/3'])
        # Normalize X
        # x = preprocessing.scale(x)
        # Check lenght of data
        print(len(x), len(y))
        x.reshape(-1, 1)
        y.reshape(-1, 1)
        if len(x) != len(y):
            print("Malformed Data!!!")
            exit()

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8)

        Prediction.clf = LinearRegression(n_jobs=-1)
        Prediction.clf.fit(x_train, y_train)
        accuracy = Prediction.clf.score(x_test, y_test)
        # See Accuracy
        print(accuracy)


