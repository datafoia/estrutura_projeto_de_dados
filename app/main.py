from pipeline.extract import extract_data
from pipeline.transform import concat_dataframes
from pipeline.load import load_excel


if __name__ == "__main__":
    listas_de_data_frame = extract_data("data/input")
    data_frame = concat_dataframes(listas_de_data_frame)
    load_excel(data_frame,"data/output", "output")


