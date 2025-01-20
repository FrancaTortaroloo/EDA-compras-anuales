#%%
import functions as func

#%%ç
print('Importar xslxs y convertir a DF')
#%%
nombre_archivo = ["Presupuesto_mensual_2021.xlsx", "Presupuesto_mensual_2022.xlsx", "Presupuesto_mensual_2023.xlsx", "Presupuesto_mensual_2024.xlsx"]
rango_hojas = list(range(1,13))

df = func.excel_a_df(nombre_archivo, rango_hojas)
#%%
#eliminar columnas que no voy a ocupar
columnas = [0,4,7,8,9]
df_completo = func.eliminar_columnas(df, columnas)
#verificar que se han eliminado las columnas
df_completo
#%%
#ponerle nombre a las columnas
nom_col =['Fecha', 'Precio', 'Producto', 'Lugar', 'Categoria']
df_completo = func.renombrar_col(df_completo, nom_col)
df_completo.sample()
# %%
#verificar los tipos de datos y hacer cambios donde se requiera
d_type = func.tipos_datos(df_completo)
# %%
#normalizar datos de la columna categoria

dict_datos = {'Supermercado Otros': 'Supermercado', 
     'Comida': 'Supermercado', 
     'Comidas': 'Supermercado', 
     'Supermercados':'Supermercado',
     'Carnes': 'Supermercado',
     'Varios': 'Otros',
     'Salud/médicos': 'Farmacia'}

reemplazo_categ = func.reemplazar_valores(df_completo, 'Categoria', dict_datos)
# %%
#normalizar datos de la columna lugar

dict_datos = {'carrefour': 'Carrefour',
     'Carrefuour': 'Carrefour' }

reemplazo_lugar = func.reemplazar_valores(df_completo, 'Lugar', dict_datos)
# %%

#normalizar datos de la columna producto

dict_datos = {'Jamon cocido': 'Jamon', 
     'Jamon lonchas': 'Jamon', 
     'Jamon en lonchas': 'Jamon', 
     'jamon york':'Jamon',
     'Lonchas jamon': 'Jamon',
     'Huevo': 'Huevos',
     'Queso': 'Queso en lonchas',
     'Queso lonchas': 'Queso en lonchas',
     'Lonchas queso': 'Queso en lonchas',
     'Leche desnatada': 'Leche',
     'Leche semi desnatada': 'Leche',
     'Leche sin lactosa': 'Leche'
     }

reemplazo_prod = func.reemplazar_valores(df_completo, 'Producto', dict_datos)
#%%
# capitalize en columna lugar y producto

mayus = func.capitalize(df_completo, 'Producto')
mayus = func.capitalize(df_completo, 'Lugar')
#%%
#eliminar nulos de la columna fecha
nulos = func.eliminar_nulos(df_completo, 'Fecha')
#%%
#comprobar valores negativos o fuera de rango en la columna precio
val_neg = func.valores_negativos(df_completo, 'Precio')
#al haber valores negativos, vamos a eliminarlos
df_completo = func.eliminar_negativos(df_completo, 'Precio')
#%%
#comprobar que se hayan eliminado
comprobar = func.valores_negativos(df_completo, 'Precio')
# %%
#guardar en csv para ocuparlo cuando quiero continuar con el trabajo y no tener que recargar el código completo
csv = func.guardar_csv(df_completo, 'compras_anuales.csv')


