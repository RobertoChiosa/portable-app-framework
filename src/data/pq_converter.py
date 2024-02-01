"""
Author:       Roberto Chiosa
Copyright:    Roberto Chiosa, © 2024
Email:        roberto.chiosa@pinvision.it

Created:      05/01/24
Script Name:  pq_converter.py
Path:         data

Script Description:


Notes:
"""
import os

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from src.app.utils.util import list_files, ensure_dir

if __name__ == '__main__':
    directory = "AHU_SX"
    ensure_dir(directory)
    ensure_dir(directory + "_PQ")

    files = list_files(directory, file_formats=[".csv", ".parquet"])

    for filename in files:
        print(filename)
        csv_file_path = os.path.join(directory, filename)  # Replace with the path to your CSV file
        df = pd.read_csv(csv_file_path)
        # Specify the path for the Parquet output file
        parquet_file_path = os.path.join(directory + "_PQ", filename.replace(".csv",
                                                                             '.parquet'))
        table = pa.Table.from_pandas(df)
        pq.write_table(table, parquet_file_path)
