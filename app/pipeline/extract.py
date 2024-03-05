import os
import glob

import pandas as pd

from typing import List

"""
Função para ler os arquivos da pasta data/input e retornar uma lista de dataframes

args: input_path (str): caminho da pasta com os arquivos

return: lista de dataframes
"""

input_path = "data/input"

def extract_data(input_path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(input_path, "*.xlsx"))

    data_frame_list = []

    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_data(input_path)
    print(data_frame_list)
