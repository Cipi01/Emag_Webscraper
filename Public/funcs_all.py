import glob
import os
import pandas as pd


def unique_col_inserter(path_end, df):
    csv_dir = f"D:/P/Webscrapers/BD/{path_end}"
    list_of_files = glob.glob(f"{csv_dir}/*.csv")
    if not list_of_files:
        pass
    else:
        latest_file = max(list_of_files, key=os.path.getctime)
        prev_df = pd.read_csv(latest_file)

        if 'UniqueID' in prev_df.columns:
            last_row = prev_df.tail(1)
            highest_id = last_row['UniqueID'].values[0]
            start_index = highest_id + 1
        else:
            start_index = 1
        df.insert(0, 'UniqueID', range(start_index, start_index + len(df)))