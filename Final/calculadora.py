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

    def potencia(self):
        """Calcula numero1 elevado a la potencia numero2"""
        resultado = self.numero1 ** self.numero2
        self.historial.append(f"{self.numero1} ^ {self.numero2} = {resultado}")
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
        """Interpreta la expresión matemática ingresada, ahora soporta '+' '-' '*' '/' '^' """
        # Lista de operadores soportados, incluyendo '^' para la potencia
        for operador in ['+', '-', '*', '/', '^']:
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