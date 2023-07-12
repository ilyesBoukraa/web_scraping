import pandas as pd

if __name__=="__main__":
    df = pd.read_csv('output.csv')
    print(df.head(n=5))