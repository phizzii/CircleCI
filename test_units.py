# FOR ANY AND ALL UNIT TESTS YOU NEED TO START FILE AND FUNCTION NAMES WITH TEST[_] OTHERWISE PYTEST WILL NOT RECOGNISE IT AND WON'T WORK

import pandas as pd
import os

print(os.getcwd())

def test_csv_saved():
    folder_path = os.getcwd() # Ensure this path exists
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The specified directory does not exist: {folder_path}")

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    assert csv_files, "no csv files in folder"

    csv_path = os.path.join(folder_path, csv_files[0])
    df = pd.read_csv(csv_path)

    assert not df.empty, f"csv file '{csv_files[0]}' is empty."

def test_csv_values():
    folder_path = os.getcwd() # Ensure this path exists
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The specified directory does not exist: {folder_path}")

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    assert csv_files, "no csv files in folder"

    csv_path = os.path.join(folder_path, csv_files[0])
    df = pd.read_csv(csv_path)

    numeric_df = df.apply(pd.to_numeric, errors='coerce')
    is_all_numeric = not numeric_df.isnull().values.any()
    print(is_all_numeric)