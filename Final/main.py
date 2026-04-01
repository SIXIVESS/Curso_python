from calculadora import Calculadora

def main():
    calc = Calculadora()
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial' para ver operaciones.")
    print("Operaciones soportadas: +, -, *, /, ^ (potencia)\n")
    
    while True:
        entrada = input("Ingresa una operación (Ej: 5 + 3, 2 ^ 3): ")
        
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break

        if entrada.strip().lower() == "historial":
           calc.ver_historial()
           continue
           
        # Interpretar la expresión usando el método estático de la clase Calculadora
        resultado = Calculadora.interpretar_expresion(entrada)
        if not resultado:
            print("Expresión no válida. Usa el formato: número operador número (Ej: 5 + 3, 2 ^ 3)")
            continue
        
        num1, num2, operador = resultado
        # Asignar los números a la instancia de la calculadora
        calc.numero1 = num1
        calc.numero2 = num2

        # --- DICCIONARIO DE OPERACIONES ACTUALIZADO ---
        # Se utiliza un diccionario para mapear operadores a métodos, facilitando la adición de nuevas operaciones.
        operaciones = {
            '+': calc.sumar,
            '-': calc.restar,
            '*': calc.multiplicar,
            '/': calc.dividir,
            '^': calc.potencia
        }

        # Ejecutar la operación correspondiente
        if operador in operaciones:
            try:
                # Llamar al método asociado al operador
                resultado_operacion = operaciones[operador]()
                print("Resultado: ", resultado_operacion)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            # Este caso no debería ocurrir porque interpretar_expresion ya valida, pero es una buena práctica.
            print(f"Operador '{operador}' no soportado.")
                
if __name__ == "__main__":
    main()