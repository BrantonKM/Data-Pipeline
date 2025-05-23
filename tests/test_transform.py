import pandas as pd
from scripts.transform import clean_data

def test_clean_data():
    raw = pd.DataFrame({'Month': ['JANUARY'], '1958': ['340']})
    cleaned = clean_data(raw)
    assert 'year_1958' in cleaned.columns
