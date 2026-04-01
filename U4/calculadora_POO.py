class Calculadora:
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2
        self.historial = []

    """ ------------- setter y getter ------------- """
    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, nuevo_numero1):
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un número.")

    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, nuevo_numero2):
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un número.")
    
    def sumar(self):
        resultado = self.numero1 + self.numero2
        self.historial.append(f"{self.numero1} + {self.numero2} = {resultado}")
        return resultado
    
    def restar(self):
        resultado = self.numero1 - self.numero2
        self.historial.append(f"{self.numero1} - {self.numero2} = {resultado}")
        return resultado
    
    def multiplicar(self):
        resultado = self.numero1 * self.numero2
        self.historial.append(f"{self.numero1} * {self.numero2} = {resultado}")
        return resultado
    
    def dividir(self):
        if self.numero2 == 0:
            raise ValueError("No se puede dividir por cero.")
        resultado = self.numero1 / self.numero2
        self.historial.append(f"{self.numero1} / {self.numero2} = {resultado}")
        return resultado
    
    def ver_historial(self):
        if not self.historial:
            print("El historial está vacío.")
        else:
            print("\n=== HISTORIAL DE OPERACIONES ===")
            for operacion in self.historial:
                print(operacion)
            print()
    
    @staticmethod
    def interpretar_expresion(expresion):
        """Interpreta la expresión matemática ingresada"""
        for operador in ['+', '-', '*', '/']:
            if operador in expresion:
                partes = expresion.split(operador)
                if len(partes) == 2:
                    try:
                        num1 = float(partes[0].strip())
                        num2 = float(partes[1].strip())
                        return num1, num2, operador
                    except ValueError:
                        return None
        return None
             
def main():
    calc = Calculadora()
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial' para ver operaciones. \n")
    
    while True:
        entrada = input("Ingresa una operación (Ej: 5 + 3): ")
        
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break

        if entrada.strip().lower() == "historial":
           calc.ver_historial()
           continue
           
        resultado = Calculadora.interpretar_expresion(entrada)
        if not resultado:
            print("Expresión no válida. Usa el formato: número operador número (Ej: 5 + 3)")
            continue
        num1, num2, operador = resultado
        calc.numero1 = num1
        calc.numero2 = num2

        if operador == '+':
            print("Resultado: ", calc.sumar())
        elif operador == '-':
            print("Resultado: ", calc.restar())
        elif operador == '*':
            print("Resultado: ", calc.multiplicar())
        elif operador == '/':
            try:
                print("Resultado: ", calc.dividir())
            except ValueError as e:
                print(f"Error: {e}")
                
main()