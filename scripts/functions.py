#%%
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import os
import pandas as pd
import re
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

#%%
def excel_a_df(archivo, rango_hojas):
    df_compras = pd.DataFrame() #df vacio para almacenar los resultados
    for a in archivo:
        try:
            datos = pd.read_excel(a, sheet_name= rango_hojas, header= None, skiprows= 5)
            #concatenar todas las hojas de los arhicvos en el df final
            for hoja, df in datos.items():
                df_compras = pd.concat([df_compras, df], ignore_index= True) #directamente concatena
            #manejo de errores
        except ValueError as e:
            #print(f"Algunas hojas especificadas no existen en {archivo}: {e}")
            continue
        except Exception as e:
            #print(f"Error inesperado al procesar el libro {a} y la hoja {l}")
            continue
    return df_compras 

#%%
def eliminar_columnas(df, col):
    df_completo = df.drop(col, axis = 1)
    return df_completo
#%%
def renombrar_col(df, nombre):
    df.columns = nombre
    return df
#%%
def tipos_datos(df):
    print(df.dtypes)
#%%
