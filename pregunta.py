"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    # Leer el archivo CSV
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    
    # Eliminar filas con valores faltantes
    df = df.dropna()

    # Eliminar comas, _, signo de dolar y espacios en blanco
    df = df.apply(lambda x: x.astype(str).str.replace("_", "-").str.replace("-", " ").str.replace("$", "").str.replace(",", ""))

    # Convertir todas las columnas de texto a minusculas
    df = df.apply(lambda x: x.str.lower().str.strip())
    

    # Limpiar columna fecha_de_beneficio
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='mixed', dayfirst=True)

    # Convertir a float columna monto_del_credito
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)
    
    # Eliminar registros duplicados
    df = df.drop_duplicates()


    return df




# Llamar a la función para limpiar los datos
clean_data()

# Verificar el resultado
print(clean_data().head())  # Imprimir las primeras filas del DataFrame limpio
print(clean_data().sexo.value_counts().to_list())
