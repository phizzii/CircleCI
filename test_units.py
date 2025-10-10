import pandas as pd
import os

def test_csv_saved():
    folder_path = '/Users/sophieb/Visual Studio Code/CircleCI'
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    assert csv_files, "no csv files in folder"

    csv_path = os.path.join(folder_path, csv_files[0])
    df = pd.read_csv(csv_path)

    assert not df.empty, f"csv file '{csv_files[0]}' is empty."