def sistema_evaluacion():
    """Sistema para registrar y evaluar alumnos."""
    alumnos = []  # Lista principal para almacenar todos los alumnos
    
    try:
        num_alumnos = int(input("Ingresa el número de alumnos: "))
        num_materias = int(input("Ingresa el número de materias: "))
        
        if num_alumnos <= 0 or num_materias <= 0:
            print("Error: El número de alumnos y materias debe ser positivo.")
            return
            
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
        return
    
    # Bucle principal para registrar a cada alumno
    for i in range(num_alumnos):
        print(f"\n--- Registrando Alumno {i+1} de {num_alumnos} ---")
        
        # Validación de nombre no vacío
        nombre = input("Nombre: ").strip()
        while not nombre:
            nombre = input("Error: El nombre no puede estar vacío. Nombre: ").strip()
        
        # Validación de matrícula no vacía
        matricula = input("Matrícula: ").strip()
        while not matricula:
            matricula = input("Error: La matrícula no puede estar vacía. Matrícula: ").strip()
        
        calificaciones = []
        # Bucle interno para registrar las calificaciones por materia
        for j in range(num_materias):
            while True:
                try:
                    nota = float(input(f"  Calificación de la materia {j+1}: "))
                    # Validar que la nota esté en un rango típico (0-10)
                    if 0 <= nota <= 10:
                        calificaciones.append(nota)
                        break
                    else:
                        print("Error: La calificación debe estar entre 0 y 10.")
                except ValueError:
                    print("Error: Debes ingresar un número válido.")
        
        # Determinar el estado final del alumno (aprobado/reprobado)
        promedio = sum(calificaciones) / num_materias
        estado = "Aprobado" if promedio > 6 else "Reprobado"
        
        # Crear el diccionario del alumno y agregarlo a la lista
        alumno = {
            "nombre": nombre,
            "matricula": matricula,
            "calificaciones": calificaciones,
            "promedio": promedio,
            "estado": estado
        }
        alumnos.append(alumno)
    
    # Mostrar resumen final
    print("\n" + "="*50)
    print("RESUMEN DE EVALUACIÓN")
    print("="*50)
    for alumno in alumnos:
        print(f"\nAlumno: {alumno['nombre']} ({alumno['matricula']})")
        print(f"  Calificaciones: {alumno['calificaciones']}")
        print(f"  Promedio: {alumno['promedio']:.2f}")
        print(f"  Estado: {alumno['estado']}")

# Llamada a la función principal
if __name__ == "__main__":
    sistema_evaluacion()