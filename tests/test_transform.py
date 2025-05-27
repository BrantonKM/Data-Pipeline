import pandas as pd
from scripts.transform import clean_data

def test_clean_data_columns():
    # Arrange
    data = {'Month ': ['JAN'], ' 1958 ': [340], '1959': [360], '1960': [417]}
    test_df = pd.DataFrame(data)
    test_file = "data/test_airtravel.csv"
    test_df.to_csv(test_file, index=False)

    # Act
    cleaned_df = clean_data(test_file)

    # Assert
    assert list(cleaned_df.columns) == ['month', '1958', '1959', '1960']
    assert cleaned_df.shape == (1, 4)
