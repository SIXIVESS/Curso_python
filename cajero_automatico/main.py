#Creación de variables que representan el inventario por
#denominación de billetes
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50=10
billetes_20=10

#Variables para el número de billetes por cada denominación
entregar_1000 = 0
entregar_500 = 0
entregar_200 = 0
entregar_100 = 0
entregar_50 = 0
entregar_20=0

while True:
    #Mensaje de inicio y solicitud de monto a retirar
    print("\n --- Dispensadora de Billetes ---") #Inicia el sistema
    print("\nIngrese el monto a retirar (0 para salir): ") #Solicita el monto 
    entrada =input()

    monto=int(entrada) #Convierte la entrada a entero
    if monto == 0:
        print("Nos vemos...")
        break

    # Reiniciar variables de entrega
    entregar_1000 = 0
    entregar_500 = 0
    entregar_200 = 0
    entregar_100 = 0
    entregar_50 = 0
    entregar_20=0
    
    restantes = monto

    # Calcular la menor cantidad de billetes empezando por el más grande
    entregar_1000 = min(restantes // 1000, billetes_1000)
    restantes -= entregar_1000 * 1000
    
    entregar_500 = min(restantes // 500, billetes_500)
    restantes -= entregar_500 * 500
    
    entregar_200 = min(restantes // 200, billetes_200)
    restantes -= entregar_200 * 200
    
    entregar_100 = min(restantes // 100, billetes_100)
    restantes -= entregar_100 * 100
    
    entregar_50 = min(restantes // 50, billetes_50)
    restantes -= entregar_50 * 50

    entregar_20 = min(restantes // 20, billetes_20)
    restantes -= entregar_20 * 20

    if restantes > 0:
        print("No hay suficientes billetes para este monto.")
    else:
        # Actualizar inventario
        billetes_1000 -= entregar_1000
        billetes_500 -= entregar_500
        billetes_200 -= entregar_200
        billetes_100 -= entregar_100
        billetes_50 -= entregar_50
        billetes_20 -= entregar_20
        
        print(f"Billetes entregados: 1000: {entregar_1000}, 500: {entregar_500}, 200: {entregar_200}, 100: {entregar_100}, 50: {entregar_50}, 20: {entregar_20}")
        print(f"Inventario restante: 1000: {billetes_1000}, 500: {billetes_500}, 200: {billetes_200}, 100: {billetes_100}, 50: {billetes_50}, 20: {billetes_20}")





