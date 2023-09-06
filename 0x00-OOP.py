class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def trabajar(self):
        pass  # Este método se definirá en las subclases

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, responsabilidades):
        super().__init__(nombre, sueldo)
        self.responsabilidades = responsabilidades

    def trabajar(self):
        print(f"El gerente {self.nombre} está supervisando.")

class Cocinero(Empleado):
    def __init__(self, nombre, sueldo, especialidad):
        super().__init__(nombre, sueldo)
        self.especialidad = especialidad

    def trabajar(self):
        print(f"El cocinero {self.nombre} está cocinando deliciosos platillos.")

class Mesero(Empleado):
    def __init__(self, nombre, sueldo, turno):
        super().__init__(nombre, sueldo)
        self.turno = turno

    def trabajar(self):
        print(f"El mesero {self.nombre} está atendiendo a los clientes en el turno {self.turno}.")

class Limpiadora(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)

    def trabajar(self):
        print(f"La limpiadora {self.nombre} está manteniendo el restaurante impecable.")

gerente1 = Gerente("Laura", 5000, "Gestión y planificación")
cocinero1 = Cocinero("Carlos", 3000, "Comida italiana")
mesero1 = Mesero("Ana", 2000, "noche")
limpiadora1 = Limpiadora("María", 1500)

empleados = [gerente1, cocinero1, mesero1, limpiadora1]

for empleado in empleados:
    empleado.trabajar()

## super
¡Por supuesto! Explicaré el concepto de super() en la programación orientada a objetos de manera sencilla y natural:

Imagina que estás construyendo algo genial con piezas de LEGO. Cada pieza tiene su forma única y encaja en su lugar especial. Ahora, a veces, cuando creas una pieza nueva que es similar a otra que ya tienes, puedes usar esa pieza anterior como base y simplemente agregar algunos detalles nuevos.

En la programación, las clases son como esas piezas de LEGO. Cuando tienes una clase base (como una pieza de LEGO que ya tienes) y quieres hacer una nueva clase similar pero con algunas diferencias, puedes usar super().

En el mundo de la programación orientada a objetos, super() es como una herramienta mágica que te permite "pedir ayuda" a la clase base. Si estás creando una nueva clase que hereda características de otra clase, puedes usar super() para acceder a los métodos y atributos de la clase base.

Por ejemplo, piensa en una clase de "Animales" y una subclase de "Perros". Los perros son animales, ¿verdad? Entonces, cuando estás haciendo una clase para perros, puedes usar super() para tomar cosas de la clase "Animales" y luego agregar las características especiales de los perros.

En resumen, super() es como decir: "¡Hey, clase base, ayúdame a construir esta nueva clase y luego agregaré lo que la hace única!" Es como usar una pieza de LEGO que ya tienes para construir algo nuevo y genial.

Espero que esto te ayude a entender qué es super() en la programación orientada a objetos. ¡Es una forma de hacer que tus clases trabajen juntas como piezas de LEGO para crear programas asombrosos!



## constructor
¡Por supuesto! Explicaré el concepto de `__init__()` en la programación orientada a objetos de manera simple y natural:

Imagina que estás construyendo una casa de muñecas. Antes de que puedas jugar con ella, necesitas configurar las habitaciones, poner muebles y hacer que todo esté listo. Ahí es donde entra en juego el "constructor" de la casa de muñecas.

En la programación, `__init__()` es como el constructor de una clase. Cuando creas una nueva instancia (como una nueva casa de muñecas), esta función se llama automáticamente. Su trabajo es configurar y preparar todo lo que la instancia necesita antes de que puedas comenzar a usarla.

Digamos que estás creando una clase para coches. Cuando haces un coche nuevo, necesitas establecer cosas como el color, la marca y el modelo, ¿verdad? Bueno, `__init__()` es el lugar donde haces exactamente eso. Es como decirle al coche cómo debe verse y comportarse cuando lo creas.

Aquí está el truco: `__init__()` se llama automáticamente cada vez que haces una nueva instancia de una clase. Por lo tanto, no tienes que recordar establecer todas esas cosas manualmente cada vez que haces algo nuevo. ¡Es como si la casa de muñecas se arreglara sola cuando la sacas de la caja!

En resumen, `__init__()` es como el "preparador" que configura todo lo que necesitas en una nueva instancia de una clase. Cuando creas una nueva instancia, se llama automáticamente para que todo esté listo para que puedas comenzar a usarla.

¡Espero que esta explicación te ayude a entender el propósito de `__init__()` en la programación orientada a objetos!