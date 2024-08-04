from src.data_processing import load_data, clean_data
from src.features import create_location_dict
from src.model_training import train_models, save_models
import os
import pandas as pd
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():

    raw_data_path = 'data/raw/weatherAUS.csv'
    processed_data_path = 'data/processed/clean_weatherAUS.csv'
    
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)

    logger.info("Iniciando la carga de datos...")    
    # Cargar y limpiar los datos
    df = load_data(raw_data_path)
    df_clean = clean_data(df)
    df_clean.to_csv(processed_data_path, index=False)
    
    # Creación de diccionarios
    df_dict_Loc = create_location_dict(df_clean)
    
    # Entrenar modelos para cada locación y evaluar
    models, accuracies = train_models(df_dict_Loc
                                      )
    # Guardar modelos
    save_models(models, 'models')
    
    for location, accuracy in accuracies.items():
        print(f'Model for {location} Accuracy: {accuracy}')


if __name__ == '__main__':
    main()