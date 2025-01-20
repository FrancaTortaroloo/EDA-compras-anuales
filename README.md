### Exploración y análisis de datos de compras anuales personales (2021 - 2024) 💰

En este proyecto he codigo todos los archivos de Google Sheets donde con mi pareja apuntamos todos y cada uno de nuestros gastos en conjunto, he exportado los datos a excel y de allí hice la carga a Python 🐍 como archivos xlsx.

A lo largo del proyecto, he normalizado los datos para que Python los reconozca y pueda hacer los gráficos para analizar los comportamientos de los datos.

Dentro del proyecto se van a encontrar con los siguientes archivos y carpetas:

📂 Carpeta `assets`: en esta carpeta se encuentran las imágenes de los gráficos que se ven más abajo.


📂 Carpeta `scripts`: en esta carpeta se encuentran los siguientes archivos: **analisis_compras.ipynb**: aquí se encuentra el código completo en un jupyter notebook y los gráficos hechos con seaborn y matplotlib. **analisis_compras.py**: aquí se encuentra el archivo que le da funcionalidad al otro archivo **functions.py**. Este último, procesa los datos y genera archivos limpios y transformados. Por último, el archivo **compras_anuales.csv** son los datos con los que he graficado y analizado el comportamiento de ellos.


📄 Arhivo`Compras_anuales.csv`: es un único dataframe con todos los datos desde junio de 2021 a diciembre de 2024.

***Conclusiones finales y aspectos a tener en cuenta***

<u>A tener en cuenta:</u> En este análsis ha quedado fuera el monto del alquiler. 

Para la comparación he hecho graficos con gastos totales y gastos promedio. En ambos casos, el resultado es diferente, como por ejemplo el gasto anual según categoría es en Supermercado pero en cuanto a la media, el gimnasio es en el que más se gasta en promedio. Esto demuetra que en supermercado realizo más transacciones pero de montos pequeños, en cambio gimnasio es de menor transacción pero con montos más altos.

El año 2023 fue donde más se gastó porque con mi pareja compramos más muebles/electrodomésticos ya que nos estamos estableciendo en España.

Nuestro top de cosas que más consumimos son: jamón, huevo y queso en lonchas. Es lo que normalmente consumimos en nuestro desayuno


!['Media de gastos anuales'](https://github.com/FrancaTortaroloo/EDA-compras-anuales/blob/main/assets/Media%20gastos%20anuales.png)

![Gasto total por categoria](https://github.com/FrancaTortaroloo/EDA-compras-anuales/blob/main/assets/Gasto%20total%20por%20categoria.png)

![Media de gastos por categoría](https://github.com/FrancaTortaroloo/EDA-compras-anuales/blob/main/assets/Media%20de%20gastos%20productos.png)

![Gasto total según lugar](https://github.com/FrancaTortaroloo/EDA-compras-anuales/blob/main/assets/Gasto%20total%20seg%C3%BAn%20lugar.png)

![Top 10 productos](https://github.com/FrancaTortaroloo/EDA-compras-anuales/blob/main/assets/Top%2010%20productos.png)





