import pandas as pd
from pprint import pprint


def import_csv(file_path):
    df = pd.read_csv(file_path, sep=";")
    return df.to_dict('records')

def import_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict('records')

pprint(import_csv(r'C:\PyProject\1\pythonProject\Data\transactions.csv'))
#pprint(import_excel(r'C:\PyProject\1\pythonProject\Data\transactions_excel.xlsx'))