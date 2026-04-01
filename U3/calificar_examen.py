import pandas as pd

#Cargar los archivos de respuestas
df_estudiantes = pd.read_csv('respuestas_estudiantes.csv')
df_correctas = pd.read_excel('respuestas_correctas.xlsx')

#Obtener las preguntas usando métodos
preguntas=df_correctas['Pregunta'].values 

#Crear diccionario de respuestas correctas
clave_respuestas={}
for i in range (df_correctas.shape[0]):
    pregunta=df_correctas['Pregunta'].iloc[i]
    respuestas=df_correctas['Respuesta'].iloc[i]

#Almacenamos en el diccionario
    clave_respuestas[pregunta]=respuestas

#Calcular puntuación para cada estudiante
df_estudiantes['Puntuación']=0
for p in preguntas:
    respuesta_correcta=clave_respuestas[p]
    df_estudiantes['Puntuación']=df_estudiantes['Puntuación'].add(
        (df_estudiantes[p] == respuesta_correcta).astype(int))
    
# Mostrar detalle completo de respuestas
df_detalle=df_estudiantes.copy()

for p in preguntas:
    df_detalle[p]=df_detalle[p].where(
        df_detalle[p]==clave_respuestas[p],
        df_detalle[p] + 'x'
    )
#Ordena por puntuación (mayor a menor)
df_estudiantes=df_estudiantes.sort_values('Puntuación', ascending=False)
print("Leyenda: Respuesta X = Incorrecta")
print(df_detalle.to_string(index=False))

#Mostrar resumen de resultados
print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")
print(df_estudiantes[['Nombre', 'Puntuación']].sort_values('Puntuación', ascending=False).to_string(index=False))

#Guardar resultados
df_estudiantes.to_csv("resultados_examen.csv", index=False)
print ("\nResultados guardados en 'resultados_examen.csv'")