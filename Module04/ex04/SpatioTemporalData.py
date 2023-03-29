import sys

sys.path.insert(0, "..")

from ex00.FileLoader import FileLoader

class SpatioTempolarData():
    def __init__(self, df):
        self.df = df
    def where(self, year):
        new_df = self.df[self.df["Year"] == year].reset_index()
        return str(new_df.loc[0, "City"])
    def when(self, city):
        new_df = self.df[self.df["City"] == city]
        return new_df.Year.unique()

loader = FileLoader()
df = loader.load("../ex00/athlete_events.csv")
info_df = SpatioTempolarData(df)
print(info_df.when("Paris"))
print(info_df.where(2016))
