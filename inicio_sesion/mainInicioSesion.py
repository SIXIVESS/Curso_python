#Variable que almacena al usuario y contraseña
usuario_correcto ="admin"
clave_correcta = "1234"

#Variable para controlar los intentos
intentos = 3
sesion_iniciada = False

#Bucle para los intentos de inicio de sesión
while intentos > 0 and not sesion_iniciada:
    #Mensaje de inicio al sistema
    print(" --- Sistema de Inicio de Sesión ---")
    #Mensaje de intentos restantes
    print(f"Intentos restantes: {intentos}")
    #Solicitud de usuario y contraseña
    print("Ingrese su usuario: ")
    usuario=input()
    print("Ingrese su contraseña: ")
    clave=input()
    
    #Validar que los campos no estén vacíos
    if usuario == "" or clave == "":
        print("Error de autentificación: Los campos usuario y contraseña no pueden estar vacíos.\n")
        intentos -= 1
    #Validar que el usuario y contraseña sean correctos
    elif usuario == usuario_correcto and clave == clave_correcta:
        print("¡Sesión iniciada correctamente!")
        sesion_iniciada = True
    else:
        print("Error: Usuario o contraseña incorrectos.\n")
        intentos -= 1

#Mensaje final si no se logró iniciar sesión
if not sesion_iniciada:
    print("Ha agotado todos los intentos. Acceso denegado.")

