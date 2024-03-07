import glob
import os
from typing import List

import pandas as pd


def extract_data(input_path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos da pasta data/input e retornar uma lista de dataframes

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """

    all_files = glob.glob(os.path.join(input_path, "*.xlsx"))

    data_frame_list = []

    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


# if __name__ == "__main__":
#     data_frame_list = extract_data("data/input")
#     print(data_frame_list)
