import sys
import matplotlib.pyplot as plt

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
        pass
    def pair_plot(self, data, features):
        pass
    def box_plot(data, features):
        pass

plotter = MyPlotLib()
plotter.histogram(df, ["Height", "Weight"])