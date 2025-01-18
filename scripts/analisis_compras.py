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
df_completo = func.tipos_datos(df_completo)
# %%
#convertir la columna precio de object a float
df_completo['Precio'] = pd.to_numeric(df_completo['Precio'], errors='coerce')
df_completo['Precio'].dtype
# %%
