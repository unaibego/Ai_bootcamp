import sys

sys.path.insert(0, "..")

from ex00.FileLoader import FileLoader

def how_many_medals(df, name):
    df = df[df["Name"] == name]
    years = df.Year.unique()
    for year in years:
        new_df = df[df["Year"] == year]
        new_df["Medal"].value_counts()["Gold"]
    print(df)
    pass

loader = FileLoader()
df = loader.load("../ex00/athlete_events.csv")
how_many_medals(df, "Lisa Raymond")