import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_data(filepath):
    """Carga los datos desde un archivo CSV."""
    logger.info('Cargando el archivo CSV.')
    return pd.read_csv(filepath)

def clean_data(df):
    """Limpia y prepara los datos para el análisis."""
    logger.info('Haciendo la limpieza.')
    # Convertir 'Date' a datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Convertir valores 'Yes'/'No' a booleanos
    df['RainToday'] = df['RainToday'].map({'No': 0, 'Yes': 1})
    df['RainTomorrow'] = df['RainTomorrow'].map({'No': 0, 'Yes': 1})

    # Convertir valores de direcciones de viento a grados
    direction_to_degrees = {
                            'N': 0,
                            'NNE': 22.5,
                            'NE': 45,
                            'ENE': 67.5,
                            'E': 90,
                            'ESE': 112.5,
                            'SE': 135,
                            'SSE': 157.5,
                            'S': 180,
                            'SSW': 202.5,
                            'SW': 225,
                            'WSW': 247.5,
                            'W': 270,
                            'WNW': 292.5,
                            'NW': 315,
                            'NNW': 337.5
                        }
    # Convertir la columna Wind_dir utilizando el diccionario
    df['WindGustDir'] = df['WindGustDir'].map(direction_to_degrees)
    df['WindDir9am'] = df['WindDir9am'].map(direction_to_degrees)
    df['WindDir3pm'] = df['WindDir3pm'].map(direction_to_degrees)
    return df