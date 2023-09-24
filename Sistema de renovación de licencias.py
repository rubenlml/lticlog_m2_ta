from datetime import datetime

# Función para verificar si la fecha de nacimiento es válida
def es_nombre_valido(nombre,apellido_paterno,apellido_materno):
    nombre_completo = nombre+apellido_paterno+apellido_materno #Concatenamos para validar todo junto
    if all( x.isalpha() or x.isspace() for x in nombre_completo):
        return True
    else:
        print("Nombre inválido")
        return False

def es_fecha_nacimiento_valida(fecha_nacimiento):
    try:
        # Verificar el formato AAAA-MM-DD
        datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

        # Calcular la edad
        nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.now()
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))

        # Verificar si la persona tiene más de 18 años
        if edad >= 18:
            return True
        else:
            print("Necesita ser mayor de edad")
            return False
    except ValueError:
        print("Formato de fecha inválido")
        return False

# Función para verificar si el número de licencia es válido
def es_numero_licencia_valido(numero_licencia):
    if len(numero_licencia) == 8:
        return True
    else:
        print("Error en el formato de licencia, debe tener una longitud de 8 caracteres")
        return False

# Función para verificar si la clave de pago es válida
def es_clave_pago_valida(clave_pago):
    if len(clave_pago) == 10:
        return True
    else:
        return False

#Contador de intentos
intentos = 0

while intentos < 3:  # Limitar a 3 intentos
    # Primer paso: Solicitud de datos
    apellido_paterno = input("Ingrese su apellido paterno: ")
    apellido_materno = input("Ingrese su apellido materno: ")
    nombre = input("Ingrese su nombre(s): ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
    numero_licencia = input("Ingrese su número de licencia actual (8 dígitos): ")

    # Segundo paso: Verificación de datos
    if (
        es_nombre_valido(nombre,apellido_paterno,apellido_materno) and
        es_fecha_nacimiento_valida(fecha_nacimiento) and
        es_numero_licencia_valido(numero_licencia)
    ):
        # Tercer paso: Proceso de pago
        clave_pago = input("Ingrese la clave de pago (10 dígitos): ")
        if es_clave_pago_valida(clave_pago): #Cuarto Paso
            # Quinto paso: Finalización
            print("¡La renovación de su licencia ha sido exitosa!")
            break
        else:
            print("Clave de pago inválida. Intente nuevamente.")
    else:
        print("Por favor, verifique sus datos.")
        intentos += 1

if intentos == 3:
    print("Ha alcanzado el límite de intentos. Reinicie el proceso.")

