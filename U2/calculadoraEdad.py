import datetime

def calcular_edad():
    """Calcula la edad basado en la fecha de nacimiento ingresada."""
    # Diccionario para validar días por mes de forma más legible que múltiples if
    dias_por_mes = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    while True:
        fecha_str = input("Ingresa tu fecha de nacimiento (DD-MM-AAAA). Ejemplo: 18-04-1960: ").strip()
        
        # Validación de campo vacío
        if not fecha_str:
            print("Error: No puedes dejar el campo vacío. Intenta de nuevo.")
            continue
        
        try:
            # Separar día, mes, año
            dia, mes, anio = map(int, fecha_str.split('-'))
        except ValueError:
            print("Error: Formato incorrecto. Usa DD-MM-AAAA. Ejemplo: 15-05-1990")
            continue
        
        # Validación de año
        if anio <= 1900:
            print("Error: El año debe ser mayor a 1900.")
            continue
        
        # Validación de mes
        if mes < 1 or mes > 12:
            print("Error: Mes inválido. Debe ser entre 1 y 12.")
            continue
        
        # Validación de día usando el diccionario
        if dia < 1 or dia > dias_por_mes[mes]:
            print(f"Error: Día inválido. El mes {mes} tiene {dias_por_mes[mes]} días.")
            continue
        
        # Fecha válida, salimos del bucle
        break

    # Cálculo de edad usando la librería datetime
    hoy = datetime.date.today()
    fecha_nac = datetime.date(anio, mes, dia)
    edad = hoy.year - fecha_nac.year
    
    # Verificar si ya cumplió años este año
    if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
        edad -= 1
        
    print(f"\nLa edad calculada es: {edad} años")
    
# Llamada a la función principal
if __name__ == "__main__":
    calcular_edad()