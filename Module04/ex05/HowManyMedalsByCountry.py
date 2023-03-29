import sys

sys.path.insert(0, "..")

from ex00.FileLoader import FileLoader 

def how_many_medals_by_country(df, team):
    df = df[df["Team"] == team]
    df = df.drop_duplicates(subset=['Event'])
    years = df.Year.unique()
    my_dict = {}
    for year in years:
        new_df = df[df["Year"] == year]
        golds = new_df[new_df["Medal"] == 'Gold'].shape[0]
        bronzes = new_df[new_df["Medal"] == 'Bronze'].shape[0]
        silvers = new_df[new_df["Medal"] == 'Silver'].shape[0]
        if golds or silvers or bronzes:
            my_dict[year] = {'G' : golds, 'S' : silvers, 'B' : bronzes}
    return my_dict

loader = FileLoader()
df = loader.load("../ex00/athlete_events.csv")

dictionary = how_many_medals_by_country(df, "Poland")
print(dictionary)