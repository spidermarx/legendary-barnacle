import pandas as pd
import pytest
from src.features import drop_empty_columns, fill_na_mode_mean, create_location_dict

# Datos de prueba
data = {
    'A': [None, None, 1, 2],
    'B': [1, 2, None, 4],
    'Location': ['Sydney', 'Sydney', 'Melbourne', 'Melbourne']
}

columns_with_mode = ['A']

def test_drop_empty_columns():
    df = pd.DataFrame(data)
    result = drop_empty_columns(df)
    assert 'A' in result.columns  # Columna 'A' no está vacía completamente
    assert 'B' in result.columns  # Columna 'B' no está vacía completamente

def test_fill_na_mode_mean():
    df = pd.DataFrame(data)
    result = fill_na_mode_mean(df, columns_with_mode)
    assert result['A'].isna().sum() == 0  # No NaN en la columna 'A'
    assert result['B'].isna().sum() == 0  # No NaN en la columna 'B'

def test_create_location_dict():
    df = pd.DataFrame(data)
    result = create_location_dict(df)
    assert 'Sydney' in result
    assert 'Melbourne' in result
    assert len(result['Sydney']) == 2  # 2 filas para 'Sydney'
    assert len(result['Melbourne']) == 2  # 2 filas para 'Melbourne'