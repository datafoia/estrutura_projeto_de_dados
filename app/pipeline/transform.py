import pandas as pd
from typing import List


"""
Função para transformar uma lista de dataframes em um dataframe
"""

def concat_dataframes(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index = True)

