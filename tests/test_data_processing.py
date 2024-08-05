import pandas as pd
import pytest
from src.data_processing import drop_empty_columns, fill_na_mode_mean, create_location_dict

# Datos de prueba
data = {
    'A': [None, None, 1, 2],
    'B': [1, 2, None, 4],
    'Location': ['Sydney', 'Sydney', 'Melbourne', 'Melbourne']
}



def test_clean_data(sample_data):
    df = clean_data(sample_data)
    
    assert pd.api.types.is_datetime64_any_dtype(df['Date'])
    assert df['RainToday'].dtype == 'int64'
    assert df['RainTomorrow'].dtype == 'int64'
    assert df['WindGustDir'].dtype == 'float64'
    assert df['WindDir9am'].dtype == 'float64'
    assert df['WindDir3pm'].dtype == 'float64'
    assert df['WindGustDir'].iloc[0] == 0
    assert df['WindDir9am'].iloc[0] == 45
    assert df['WindDir3pm'].iloc[0] == 90