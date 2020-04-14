import matplotlib as mtp
import matplotlib.pyplot as plt
import pandas as pd


class VisualizationController:
    force_acceleration_data = "Simulation_results/force_acceleration.csv"

    @staticmethod
    def read_data(path):
        df = pd.read_csv(path)
        return df

    @staticmethod
    def visualise_connection(type, var_1, var_2):
        if type == "force_acc":
            df = VisualizationController.read_data(VisualizationController.force_acceleration_data)
            labels = ["Acceleration", "Force"]
            title = "Force Acceleeration Relation"
        plt.plot(df[var_1], df[var_2], 'ro') # noqa
        plt.ylabel(labels[0])
        plt.xlabel(labels[1])
        plt.title(title)
        plt.grid(True)
        plt.xlim((-300, 0))

        plt.show()


