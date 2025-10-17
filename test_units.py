# FOR ANY AND ALL UNIT TESTS YOU NEED TO START FILE AND FUNCTION NAMES WITH TEST[_] OTHERWISE PYTEST WILL NOT RECOGNISE IT AND WON'T WORK

import pandas as pd
import os

print(os.getcwd())

def test_csv_saved():
    # testing to make sure the csv file actually exists to be analysed from
    folder_path = os.getcwd()
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The specified directory does not exist: {folder_path}")

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    assert csv_files, "no csv files in folder"

    csv_path = os.path.join(folder_path, csv_files[0])
    df = pd.read_csv(csv_path)

    assert not df.empty, f"csv file '{csv_files[0]}' is empty."

def test_csv_values():
    # testing to make sure all values in the csv file are numerical and do not contain null values
    folder_path = os.getcwd()
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The specified directory does not exist: {folder_path}")

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    assert not df.empty, f"csv file '{csv_files[0]}' is empty."

    csv_path = os.path.join(folder_path, csv_files[0])
    df = pd.read_csv(csv_path)

    numeric_df = df.apply(pd.to_numeric, errors='coerce')
    is_all_numeric = not numeric_df.isnull().values.any()
    print(is_all_numeric)

    assert not numeric_df.isnull().values.any(), f"csv contains null/non-numerical values"

def test_correlation_coefficient():
    folder_path = os.getcwd()
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The specified directory does not exist: {folder_path}")

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    assert csv_files, "no csv files in folder"

    csv_path = os.path.join(folder_path, csv_files[0])
    df = pd.read_csv(csv_path)

    df.corr()

    if df.corr() < 0.95:
        raise TypeError(f"file contains non-numerical/null values")
    
            
