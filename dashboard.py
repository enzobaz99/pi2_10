import pandas as pd

# Cargar el DataFrame desde un archivo CSV u otra fuente de datos
df = pd.read_csv('df_accidntepower.csv')

def calcular_numero_promedio_pasajeros(df):
    promedio_pasajeros = df['Pasajeros'].mean()
    return promedio_pasajeros

def calcular_porcentaje_accidentes_militares(df):
    total_accidentes = len(df)
    accidentes_militares = df[df['Operador'].str.contains('Military', case=False)]
    porcentaje_militares = len(accidentes_militares) / total_accidentes * 100
    return porcentaje_militares

def calcular_relacion_fallecidos_sobrevivientes(df):
    total_fallecidos = df['Total de Fallecidos'].sum()
    muertos_en_tierra = df['Muertos en tierra'].sum()
    sobrevivientes = df['Total de personas a bordo'].sum() - total_fallecidos
    return (total_fallecidos, muertos_en_tierra, sobrevivientes)

# Aquí deberías cargar el DataFrame desde un archivo CSV o de otra fuente de datos
df = pd.read_csv('df_accidntepower.csv')

# Luego, puedes llamar a las funciones personalizadas para obtener los resultados de los KPIs
numero_promedio_pasajeros = calcular_numero_promedio_pasajeros(df)
porcentaje_accidentes_militares = calcular_porcentaje_accidentes_militares(df)
relacion_fallecidos_sobrevivientes = calcular_relacion_fallecidos_sobrevivientes(df)

# Finalmente, puedes imprimir los resultados de los KPIs junto con sus descripciones
print("KPI: Número promedio de pasajeros por vuelo")
print("Este KPI muestra el promedio de pasajeros que viajan en cada vuelo.")
print("Permite tener una idea general de la ocupación promedio de las aeronaves")
print("y puede ser útil para evaluar la demanda de transporte aéreo y la capacidad")
print("de las aerolíneas para atender a los pasajeros.")
print("Resultado:", numero_promedio_pasajeros)
print()

print("KPI: Porcentaje de accidentes que involucran aeronaves militares")
print("Este KPI muestra el porcentaje de accidentes que ocurren con aeronaves militares")
print("en comparación con el total de accidentes.")
print("Proporciona una visión de la proporción de accidentes en los que están involucradas")
print("aeronaves militares, lo que puede ser relevante para evaluar la seguridad y el riesgo")
print("asociado con este tipo de operaciones.")
print("Resultado:", porcentaje_accidentes_militares)
print()

print("KPI: Relación entre fallecidos, muertos en tierra y sobrevivientes")
print("Este KPI muestra la relación entre el total de fallecidos, los muertos en tierra")
print("y los sobrevivientes de accidentes aéreos.")
print("Permite comprender la magnitud de las pérdidas humanas en comparación con el total")
print("de personas a bordo, así como identificar el número de muertos en tierra y el número")
print("de personas que lograron sobrevivir. Este KPI es importante para evaluar el impacto humano")
print("de los accidentes aéreos y la efectividad de las medidas de seguridad y supervivencia.")
print("Resultado:")
print("Total de fallecidos:", relacion_fallecidos_sobrevivientes[0])
print("Muertos en tierra:", relacion_fallecidos_sobrevivientes[1])
print("Sobrevivientes:", relacion_fallecidos_sobrevivientes[2])
