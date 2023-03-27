import sys
sys.path.insert(0,"..")
from ex00.FileLoader import FileLoader

def youngest_fellah(df, year):
    new_df_boy = df[(df["Year"] == year) & (df["Sex"] == "M")]
    new_df_girl = df[(df["Year"] == year) & (df["Sex"] == "F")]
    new_df_boy = new_df_boy.sort_values("Age")
    new_df_girl = new_df_girl.sort_values("Age")
    return {'f' : float(new_df_girl["Age"].head(1)), 'm' : float(new_df_boy["Age"].head(1))}

loader = FileLoader()
df = loader.load("athlete_events.csv")
dictionary = youngest_fellah(df, 2004)
print(dictionary)