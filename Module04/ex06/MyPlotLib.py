import sys
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, "..")

from ex00.FileLoader import FileLoader

loader = FileLoader()
df = loader.load("../ex00/athlete_events.csv")

class MyPlotLib():
    def histogram(self, data, features):
        fig, axes = plt.subplots(1, 2)
        axes[0].title.set_text(features[0])
        axes[1].title.set_text(features[1])
        data[features[0]].hist(ax=axes[0])
        data[features[1]].hist(ax=axes[1])
        plt.show()
    def density(self, data, features):
        data[features[0]].plot.density()
        data[features[1]].plot.density()
        plt.legend(labels=features)
        plt.show()
    def pair_plot(self, data, features):
        sns.pairplot(data[features], diag_kws = {'alpha':0.55, 'bins':15})
        plt.show()
    def box_plot(self, data, features):
        data[features].plot(kind='box')
        # data[features].plot(kind='box')
        plt.show()

plotter = MyPlotLib()
plotter.box_plot(df, ["Height", "Weight"])