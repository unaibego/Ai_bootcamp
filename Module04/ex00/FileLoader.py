import pandas as pd

class FileLoader():
    def load(self, path):
        #  pd.set_option('display.width', 200) # honekin maximo 200 karakter jartzen ditu luzeeran
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
        return df
    def display(self, df, n):
        print(df.head(n))
