# Nombre del proyecto: model_DS
# Nombre del responsable: Marcos Macias Mier
# Correo: marcos.macias@walmart.com

Contexto:
Se analizó la libreta modelo_DS.ipynb para estudiar los elementos que tuvieran una estructura deficiente que pusieran en riesgo la aplicabilidad, escalamiento y el monitoreo constante del performance del modelo. Se encontraron las siguientes áreas de oportunidad:
1)	El código estaba en un solo archivo de Jupyter, lo que dificulta la lectura y la ejecución del código
2)	Existían problemas de consistencia en el mismo, como errores en el cálculo de la matriz de correlaciones derivado de columnas que contenían variables categóricas (como Location).
3)	Se tenían diversos for loops anidados que podían tener una estructura más eficiente. Por ejemplo, el cambio de las direcciones de viento a variables numéricas podía realizarse con un remap
4)	Existían diversos análisis gráficos que resultan redundantes. El cálculo de matrices de correlación completas y su visualización para cada locación resulta ineficiente e innecesaria en el ambiente de producción
5)	Las rutinas de limpieza de datos no tenían estructura
6)	Se tenían números mágicos a lo largo del código
7)	Se tenían comentarios innecesarios a lo largo del código
8)	Los modelos obtenidos no se guardaban para su uso futuro
9)	Existían diferentes nomenclaturas dentro del mismo código

Las soluciones implementadas fueron las siguientes:
1) Se hizo una reestructuración del código en múltiples archivos .py, cada uno con una responsabilidad bien definida, todos orquestados por un archivo main.py. La estructura de carpetas escogida fue la siguiente:





modelo_SD/
│
├── data/
│   ├── raw/                 # Datos sin procesar
│   └── processed/           # Datos procesados
│
├── models/
│   ├── Adelaide_model.pkl	# Modelos de cada ciudad, “Ciudad_model.pkl”
│   ├── Albany_model.pkl                 
│   ├── . . . 
│
├── notebooks/
│   └── 1.0-EL-original-code-modelo_DS.ipynb      # Libreta original
│   └── 2.0-MMM-pruebas-modelo_DS_refactorizado.ipynb      # Libreta de pruebas
│
├── src/
│   ├── data_processing.py   # Procesamiento de datos
│   ├── feature.py # Cálculo de features relevantes
│   ├── model_training.py    # Entrenamiento del modelo
│
├── tests/
│   └── test_data_processing.py # Pruebas unitarias
│
└── main.py  	# Orquestación
│
└── requirements.txt  	# Requisitos para el ambiente virtual


2) Se añadieron argumentos a las funciones que permiten calcular la matriz de correlación y se estructuraron dentro de una sola función
3) Para los cambios de variable categórica a numérica se usó el método “remap” de pandas y para los for anidados usados en los otros procesos se utilizaron funciones definidas
4) Se resumió toda la selección de columnas importantes o “features” (es decir, aquellas con un valor absoluto para el coeficiente de correlación mayor a 0.1) en una sola función con responsabilidad definida y testeable
5) Se organizó la estructura del código para que resultara legible y con un flujo de trabajo claro:
# Cargar y limpiar los datos
# Creación de diccionario de dataframes
# Limpieza de diccionario de dataframes 
# Entrenar modelos para cada locación y evaluar
# Guardar modelos
	6) Todo parámetro fue incorporado en las funciones para su fácil mantenimiento, cambio o lectura en el futuro
	7) Se eliminaron los comentarios que no resultaran útiles para el código. Se incorporaron docstrings 
	8) Añadí una función para guardar los modelos, uno para cada locación, en archivos .pkl
9) Se adoptó una misma nomenclatura para todas las variables (PEP 8)

De esta manera se refactorizó el código para hacer más fácil su monitoreo y legibilidad.  Se incluye el archivo .txt con los requerimientos del ambiente virtual, así como una carpeta con archivos .py para las pruebas unitarias (por el momento sólo se agrega la prueba test_data_processing.py para la primera parte del proceso) y una carpeta para los notebooks con la siguiente nomenclatura: “número-iniciales de autor/a-breve descripción”. El archivo .ini es un archivo auxiliar para las pruebas unitarias.
