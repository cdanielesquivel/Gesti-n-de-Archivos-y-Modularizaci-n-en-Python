# Proyecto: [Nombre del Proyecto]
# Estudiante: Carlos Daniel Esquivel Bolaños
# Fecha de Inicio: 24/02/2025
# Fecha de Entrega: 24/02/2025
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

# from analisis_datos.estadisticas import media,calcular_mediana

from analisis_datos import *

lista_compras = generar_lista_de_compras()
print(lista_compras)

lista_parametro = [5,3,1,2,4]
print('Media: ', media(lista_parametro))
print('Mediana: ', calcular_mediana(lista_parametro))