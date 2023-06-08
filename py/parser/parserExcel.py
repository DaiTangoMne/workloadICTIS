import pandas as pd


def get_df(path: str) -> pd.DataFrame:
    df = pd.read_excel(
        path,
        sheet_name='TDSheet',
        engine="openpyxl"
    )
    df = df.where(df.notnull(), None)
    return df
