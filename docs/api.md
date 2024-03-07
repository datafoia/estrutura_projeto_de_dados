# API Documentation

Abaixo, você encontrará detalhes sobre as funções e módulos do nosso projeto.

### `extract`

```python
def extract_data(input_path: str) -> List[pd.DataFrame]:

    """
    Função para ler os arquivos da pasta data/input e retornar uma lista de dataframes

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """
```

### `transform`

```python
def concat_dataframes(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de DataFrames em um único DataFrame consolidado.

    Args:
        data (list): Lista contendo DataFrames para consolidação.

    Returns:
        DataFrame: DataFrame consolidado.
    """
```

### `load`

```python
def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    Função para carregar (ou salvar) um DataFrame em um arquivo Excel.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        output_folder (str): Diretório onde o arquivo será salvo.
        filename (str): Nome do arquivo Excel.

    Returns:
        None
    """
```