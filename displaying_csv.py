import pandas as pd

if __name__=="__main__":
    df = pd.read_csv('output.csv')
    # I did not need to use n=5
    # because it is the defualt params
    # however I always forget the attributes
    # of the head() method... (I should make it as an argument using CLI)
    print(df.head(n=5))
