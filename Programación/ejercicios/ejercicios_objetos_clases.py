# Ejercicio 1. Crear una clase y sus objetos
# Define la clase Coche. Dentro de ella, escribe un __init__ que reciba la marca y el modelo y los guarde como atributos de cada objeto.
# Una vez definida la clase, fuera de ella:
# - Crea dos objetos que representen coches distintos.
# - Muestra la marca y el modelo de cada uno.
# - Cambia el modelo del primer coche y comprueba que el segundo conserva el suyo.
print("******Solución ejercicio 1******")
class Coche:
    # __init__ es un método especial ejecutado para inicializar sus atributos con los valores
    def __init__(self, marca, modelo):
        # marca y modelo son los parámetros que recibe el método y, self.marca y self.modelo son los atributos que guardan esos valores
        self.marca = marca
        self.modelo = modelo

# Crear objetos
coche1 = Coche("Volkswagen", "Polo")
coche2 = Coche("Audi", "Q5")

# Cambiar valores de un objeto
coche1.modelo = "Tiguan"

# Acceder a los atributos
print("Marca del primer coche: ",coche1.marca)
print("Modelo del primer coche: ",coche1.modelo)
print("Marca del segundo coche: ",coche2.marca)
print("Modelo del segundo coche: ",coche2.modelo)

# Ejercicio 2. Modificar el estado de un objeto
# Escribe la definición completa de la clase CochePruebas. Los tres métodos siguientes deben quedar definidos dentro del cuerpo de la clase:
# - __init__(): crea el atributo de instancia velocidad con valor inicial 0, en km/h.
# - acelerar(): aumenta en 10 la velocidad del propio objeto.
# - detener(): pone a cero la velocidad del propio objeto.
# Después de terminar la definición de la clase, fuera de ella, crea dos coches de pruebas. Llama a sus métodos para acelerarlos un número distinto de veces y detén solo uno. Comprueba que cada coche conserva su propia velocidad y que detener uno no cambia la del otro.
print("******Solución ejercicio 2******")
class CochePruebas:
    def __init__(self):
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10

    def detener(self):
        self.velocidad = 0

coche_prueba1 = CochePruebas()
coche_prueba2 = CochePruebas()

# Aceleramos cada coche un número distinto de veces
coche_prueba1.acelerar()
coche_prueba1.acelerar()
coche_prueba1.acelerar()

coche_prueba2.acelerar()
coche_prueba2.acelerar()

# Detenemos solamente el primer coche
coche_prueba1.detener()

# Comprobamos las velocidades
print("Velocidad coche 1:",coche_prueba1.velocidad)
print("Velocidad coche 2:",coche_prueba2.velocidad)

# Ejercicio 3. Heredar atributos y métodos
# Define una clase Vehiculo. Su inicializador debe guardar marca y modelo, y su método describir() debe devolver un texto que incluya ambos atributos.
# Define después una clase CocheElectrico que herede de Vehiculo. Dentro de ella, escribe un inicializador que reutilice el de Vehiculo mediante super() y guarde también autonomia_km. Utiliza describir() por herencia, sin volver a definirlo.
# Fuera de las clases, crea un coche eléctrico y comprueba que puedes consultar sus tres atributos y utilizar la descripción heredada.
print("******Solución ejercicio 3******")
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def describir(self):
        return f"Vehículo de la marca {self.marca}, modelo {self.modelo}"

# Nueva clase CocheElectrico que hereda de Vehiculo 
class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km

coche_electrico1 = CocheElectrico("Hyundai", "IONIQ 3", 350)

# Uso del método describir() heredado de la clase Vehiculo
coche_electrico1.describir()

print("Marca de coche:", coche_electrico1.marca)
print("Modelo de coche:", coche_electrico1.modelo)
print("Autonomía de coche:", coche_electrico1.autonomia_km)
print(coche_electrico1.describir())

# Ejercicio 4. Sobrescribir un método heredado
# Define una clase Motor para representar motores de coches. Su inicializador debe guardar
# modelo y su método arrancar() debe devolver "Motor en marcha". Crea dos subclases:
# - MotorGasolina: su método arrancar() debe devolver "Motor de gasolina en marcha".
# - MotorElectrico: su método arrancar() debe devolver "Motor eléctrico en marcha".
# Ambas subclases deben utilizar el inicializador heredado de Motor, sin definir otro __init__. Después, crea un motor de cada tipo con modelos distintos y comprueba sus modelos y mensajes de arranque.
print("******Solución ejercicio 4******")
class Motor:
    def __init__(self, modelo):
        self.modelo = modelo
    def arrancar():
        return f"Motor en marcha"

class MotorGasolina(Motor):
    def __init__(self, modelo):
        super().__init__(modelo)
    def arrancar(self):
        return f"Motor de gasolina en marcha"
    
class MotorElectrico(Motor):
    def __init__(self, modelo):
        super().__init__(modelo)
    def arrancar(self):
         return f"Motor eléctrico en marcha"

# Crear instacias
motor_gasolina1 = MotorGasolina("EA888 2.0 TSI")
motor_electrico1 = MotorElectrico("APP310")

print("Modelo de motor de gasolina:", motor_gasolina1.modelo)
print(motor_gasolina1.arrancar())
print("Modelo de motor eléctrico:", motor_electrico1.modelo)
print(motor_electrico1.arrancar())

# Ejercicio 5. Utilizar el polimorfismo
# Reutiliza las clases del ejercicio anterior. Escribe una función poner_en_marcha(motor) que llame al método arrancar() del objeto recibido y devuelva su resultado. Después:
# - Crea una lista con un objeto MotorGasolina y otro MotorElectrico.
# - Recorre la lista con un bucle y utiliza poner_en_marcha() para mostrar el mensaje de cada motor.
# La función debe funcionar sin comprobar el tipo del motor con type() o isinstance().
# Finalmente, añade una clase MotorDiesel que herede de Motor y cuyo método arrancar() devuelva "Motor diésel en marcha" Incorpora un motor diésel a la lista y comprueba que funciona sin modificar la función poner_en_marcha() ni el bucle.
print("******Solución ejercicio 5******")
def poner_en_marcha(motor):
    return motor.arrancar()

motor_gasolina2 = MotorGasolina("EcoBoost")
motor_electrico2 = MotorElectrico("BMW Gen5 eDrive")

motores = [motor_gasolina2, motor_electrico2]

for motor in motores:
    inicio_motor = poner_en_marcha(motor)
    print(inicio_motor)

class MotorDiesel(Motor):
    def __init__(self, modelo):
        super().__init__(modelo)
    def arrancar(self):
        return f"Motor diésel en marcha"

motor_diesel1 = MotorDiesel("OM654")

motores.append(motor_diesel1)

# Recorremos la lista y arrancamos todos los motores
for motor in motores:
    inicio_motor = poner_en_marcha(motor)
    print(inicio_motor)

# Ejercicio 6. Ampliar un método heredado con super()
# Retoma las clases del ejercicio 3. Escribe una nueva versión de CocheElectrico que conserve su inicializador y defina su propio método describir().
# Ese método debe aprovechar la descripción de Vehiculo mediante super(), añadir una frase con la autonomía en kilómetros y devolver el mensaje completo. Reutiliza la descripción original sin volver a escribirla manualmente.
# Una vez definida esta versión de la clase, crea un coche eléctrico y comprueba tanto la descripción ampliada como la conservación de sus atributos.
print("******Solución ejercicio 6******")
class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km
    def describir(self):
        descripcion = super().describir()
        return f"{descripcion}. Tiene una autonomía de {self.autonomia_km} km"

coche_electrico2 = CocheElectrico("Omoda", "E5", 600)

print(coche_electrico2.describir())
print("Marca de coche:", coche_electrico2.marca)
print("Modelo:", coche_electrico2.modelo)
print("Autonomía:", coche_electrico2.autonomia_km)

# Ejercicio 7. Mostrar datos con f-strings
# Utiliza estos datos:
# marca = "Seat"
# modelo = "Ibiza"
# anio = 2020
# Escribe un único print() con una f-string que inserte los valores de las tres variables en una frase legible.
# Después, cambia los valores de las variables y comprueba que el mensaje se actualiza sin modificar el print(). No necesitas crear ninguna clase.
print("******Solución ejercicio 7******")
marca = "Opel"
modelo = "Corsa"
anio = 2010

print (f"Coche de la marca {marca}, modelo {modelo} vendido por primera vez en {anio}")

# Ejercicio 8. Gestionar una entrada incorrecta con try y except
# Pide al usuario los kilómetros recorridos por un coche con input() e intenta convertirlos a un entero con int() dentro de un bloque try.
# - Si la conversión funciona, muestra "Kilómetros indicados:" seguido del número.
# - Si se produce ValueError, muestra "Debes escribir un número entero.".
# - Fuera del try / except, muestra siempre "Programa finalizado.".
# Haz dos pruebas en ejecuciones distintas: introduce primero 12000 y después doce mil.
# Comprueba que el programa muestra el mensaje adecuado y llega al mensaje final en ambos casos.
# Solo debes comprobar si la entrada puede convertirse a entero. No hace falta repetir la pregunta ni utilizar un bucle.
print("******Solución ejercicio 8******")
km_recorridos = input("Introduce el número de km recorridos:")
try:
    convertir_km_a_int = int(km_recorridos)
    if convertir_km_a_int > 0:
        print ("Kilómetros indicados:", convertir_km_a_int)
except:
    print ("Debes escribir un número entero.")

print ("Programa finalizado.")
