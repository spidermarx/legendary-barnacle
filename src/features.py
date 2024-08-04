import pandas as pd
import logging

logger = logging.getLogger(__name__)

columns_with_mode = ['WindGustDir', 'WindDir9am', 'WindDir3pm', 'Cloud9am', 'Cloud3pm']

def drop_empty_columns(df):
    """Elimina las columnas con todas las entradas vacías."""
    return df.dropna(axis=1, how='all')

def fill_na_mode_mean(df, columns_with_mode):
    """Rellena NaN con la moda para columnas específicas y con la media para el resto."""
    for col in columns_with_mode:
        if col in df.columns:
            moda = df[col].mode()[0]
            df[col].fillna(moda, inplace=True)
    
    for col in df.columns:
        if col not in columns_with_mode and df[col].dtype in ['float64', 'int64']:
            media = df[col].mean()
            df[col].fillna(media, inplace=True)
    
    return df

def create_location_dict(df):
    """Crea un diccionario con DataFrames filtrados por locación."""
    logger.info('Creando diccionario de locaciones...')
    locations = df['Location'].unique()
    df_dict_Loc = {loc: df[df['Location'] == loc] for loc in locations}

    # Aplicar la función de quitar columnas vacías a cada DataFrame en el diccionario
    logger.info('Quitando columnas vacías...')
    for key in df_dict_Loc:
        df_dict_Loc[key] = drop_empty_columns(df_dict_Loc[key])
    
    # Aplicar la función de relleno a cada DataFrame en el diccionario
    logger.info('Rellenando NaNs con Moda o Promedio, segun el caso...')
    for key in df_dict_Loc:
        df_dict_Loc[key] = fill_na_mode_mean(df_dict_Loc[key], columns_with_mode)
    
    return df_dict_Loc