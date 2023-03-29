import sys

sys.path.insert(0, "..")

from ex00.FileLoader import FileLoader


def proportion_by_sport(df, year, sport, gender):
    df.drop_duplicates('Name', inplace=True)
    df = df[df["Year"] == year]
    divisor = df[df["Sex"] == gender]
    dividend = divisor[divisor["Sport"] == sport]
    print(dividend.tail(24))
    solution = dividend.shape[0] / divisor.shape[0]
    return solution * 100
    
#no me esta dando bien me cago en la leche cafe, uste dut ondo dagoela eta nire errua ez dela
loader = FileLoader()
df = loader.load("../ex00/athlete_events.csv")
# loader.display(df, 12)
print(proportion_by_sport(df, 2004, "Tennis", "F"))
