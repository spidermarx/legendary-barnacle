import pandas as pd
import pytest
from src.data_processing import clean_data, load_data

# Datos de prueba
data = {
    'Location': ['Sydney', 'Sydney', 'Melbourne', 'Melbourne'],
    'Date': ['2017-06-21', '2018-06-21','2019-06-21', '2010-06-21'],
    'RainToday' : ['Yes', 'No', 'No','Yes'],
    'RainTomorrow' : ['Yes', 'No', 'No','Yes'],
    'WindGustDir' : ['N', 'NE', 'S','SW'],
    'WindDir9am' : ['N', 'N', 'SE','SW'],
    'WindDir3pm' : ['NE', 'N', 'SE','SW']
}

@pytest.fixture
def csv_file(tmpdir):
    df = pd.DataFrame(data)
    file_path = tmpdir.join("test_data.csv")
    df.to_csv(file_path, index=False)
    return file_path

@pytest.fixture
def sample_data():
    return pd.DataFrame(data)

def test_clean_data(sample_data):
    df = clean_data(sample_data)
    
    assert pd.api.types.is_datetime64_any_dtype(df['Date'])
    assert df['RainToday'].dtype == 'int64'
    assert df['RainTomorrow'].dtype == 'int64'
    assert df['WindGustDir'].dtype == 'float64'
    assert df['WindDir9am'].dtype == 'float64'
    assert df['WindDir3pm'].dtype == 'float64'