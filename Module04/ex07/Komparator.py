import sys
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, "..")

from ex00.FileLoader import FileLoader

loader = FileLoader()
df = loader.load("../ex00/athlete_events.csv")
print(df)

class Komparator():
    def compare_histogram(self, categorical_var, numerical_var):

        categories = numerical_var[categorical_var[0]].unique()
        fig, axes = plt.subplots( len(categories) // 2, 2)
        for i, category in enumerate(categories):
            axes[i].title.set_text(category)
            numerical_var[numerical_var[categorical_var[0]] == category][categorical_var[1]].hist(ax=axes[i])
        plt.show()
    def density(self, categorical_var, numerical_var):
        categories = numerical_var[categorical_var[0]].unique()
        fig, axes = plt.subplots( len(categories) // 2, 2)
        for i, category in enumerate(categories):
            try:
                axes[i].title.set_text(category)
                numerical_var[numerical_var[categorical_var[0]] == category][categorical_var[1]].plot.density(ax=axes[i])
            except:
                print("no pasa nada", i)
        plt.show()
    def compare_box_plot(self, categorical_var, numerical_var):
        categories = numerical_var[categorical_var[0]].unique()
        fig, axes = plt.subplots( len(categories) // 2, 2)
        for i, category in enumerate(categories):
            try:
                axes[i].title.set_text(category)
                numerical_var[numerical_var[categorical_var[0]] == category][categorical_var[1]].plot(kind= "box", ax=axes[i])
            except:
                print("no pasa nada", i)
        plt.show()

plotter = Komparator()
plotter.compare_box_plot(["Season", "Weight"], df)