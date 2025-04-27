import pandas as pd


def import_csv(file_path):
    """Импорт CSV"""
    df = pd.read_csv(file_path, sep=";")
    return df.to_dict("records")


def import_excel(file_path):
    """Импорт Excel"""
    df = pd.read_excel(file_path)
    return df.to_dict("records")
