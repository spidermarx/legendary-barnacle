from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)

def get_high_correlation_columns(df, target_column='RainTomorrow', threshold=0.1):
    """
    Obtiene una lista de las columnas de un DataFrame que tienen un valor absoluto del
    coeficiente de correlación con respecto a la columna objetivo mayor a un umbral dado.
    """
    correlation_matrix = df.corr(numeric_only=True)
    target_correlation = correlation_matrix[target_column].drop(target_column)
    
    # Filtrar columnas con coeficiente de correlación absoluto mayor que el umbral
    high_correlation_columns = target_correlation[abs(target_correlation) > threshold].index.tolist()
    
    return high_correlation_columns

def train_model_for_location(df, target_column='RainTomorrow', threshold=0.1):
    """Entrena un modelo de machine learning para una locación específica, considerando solo columnas relevantes."""
    # Obtener columnas relevantes
    high_corr_columns = get_high_correlation_columns(df, target_column, threshold)
    relevant_columns = high_corr_columns + [target_column]

    # Filtrar el DataFrame
    df_filtered = df[relevant_columns]

    # Selecciona la columna objetivo y la cambia a entero
    X = df_filtered.drop(columns=[target_column])
    y = df_filtered[target_column].astype(int)

    #Dividimos los datos en los conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = DecisionTreeClassifier(random_state=0)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy

def train_models(df_dict_Loc, target_column='RainTomorrow', threshold=0.1):
    """Entrena modelos de machine learning para cada locación en el diccionario, considerando solo columnas relevantes."""
    logger.info('Comenzando a entrenar...')
    models = {}
    accuracies = {}

    for location, df in df_dict_Loc.items():
        print(f"Training model for {location}...")
        model, accuracy = train_model_for_location(df, target_column, threshold)
        models[location] = model
        accuracies[location] = accuracy
        print(f"Model for {location} trained with accuracy: {accuracy}")

    return models, accuracies

def save_models(models, directory='models'):
    """Guarda los modelos entrenados en la carpeta especificada."""
    os.makedirs(directory, exist_ok=True)
    for location, model in models.items():
        model_path = os.path.join(directory, f"{location}_model.pkl")
        joblib.dump(model, model_path)
        print(f"Model for {location} saved at {model_path}")