Desafio OOP

**Desafío: Crear Clases para Vehículos**

Imagina que estás diseñando un sistema para gestionar diferentes tipos de vehículos. Tu tarea es crear clases para diferentes tipos de vehículos y configurar sus características utilizando `__init__()`.

1. Crea una clase base llamada `Vehiculo` con los siguientes atributos:
   - `marca`
   - `modelo`
   - `anio`

2. Crea subclases para tipos específicos de vehículos:
   - `Automovil`: Agrega el atributo `num_puertas`.
   - `Motocicleta`: Agrega el atributo `cilindrada`.
   - `Camion`: Agrega el atributo `capacidad_carga`.

3. En el constructor (`__init__()`) de cada subclase, utiliza `super()` para asegurarte de que los atributos heredados de la clase `Vehiculo` sean configurados correctamente.

4. Crea instancias de diferentes tipos de vehículos y configura sus atributos usando los constructores.

5. Imprime la información de cada vehículo, mostrando sus características únicas además de las comunes.

Aquí hay un inicio para el código:

```python
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

# Completa las clases Motocicleta y Camion

# Crea instancias y muestra la información
auto1 = Automovil("Toyota", "Corolla", 2022, 4)
# Crea más instancias aquí

print(f"Automóvil: {auto1.marca} {auto1.modelo} {auto1.anio}, Puertas: {auto1.num_puertas}")
# Imprime información de las otras instancias
```

¡Anima a tus alumnos a completar las clases para `Motocicleta` y `Camion`, crear más instancias y mostrar la información de cada vehículo! Este desafío les ayudará a practicar el uso de `__init__()` y herencia en la programación orientada a objetos.