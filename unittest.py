import pandas as pd
import os

def csv_saved_unit_test():
    #df = pd.read_csv("/Users/sophieb/Visual Studio Code/CircleCI/*.csv")
    #print(df)
    if 'output' in os.listdir('/Users/sophieb/Visual Studio Code/CircleCI'):
        if len(os.listdir('/Users/sophieb/Visual Studio Code/CircleCI'))>0:
            x=[_ for _ in os.listdir('/Users/sophieb/Visual Studio Code/CircleCI') if _[-3:]=='csv'][0]
            new_file=pd.read_csv(x)
            print(new_file)

csv_saved_unit_test()
