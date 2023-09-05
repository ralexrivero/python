
# Programacion orientada a objetos

## Introduccion

La programacion orientada a objetos es un paradigma de programacion que se basa en la interaccion de objetos para resolver problemas. Un objeto es una entidad que tiene un estado y un comportamiento. Por ejemplo, un objeto puede ser un usuario, que tiene un nombre, un apellido, un email, etc. y puede hacer cosas como iniciar sesion, cerrar sesion, etc.

La programacion orientada a objetos se basa en 4 pilares:

- Abstraccion
- Encapsulamiento
- Herencia
- Polimorfismo

## Abstraccion

La abstraccion es el proceso de identificar las caracteristicas importantes de un objeto y eliminar las que no lo son. Por ejemplo, un usuario tiene un nombre, un apellido, un email, etc. pero solo nos interesa el email para iniciar sesion, por lo que podemos abstraer el objeto usuario a solo su email.

## Encapsulamiento

El encapsulamiento es el proceso de ocultar los detalles de implementacion de un objeto. Por ejemplo, un usuario tiene un nombre, un apellido, un email, etc. pero solo nos interesa el email para iniciar sesion, por lo que podemos ocultar los detalles de implementacion del objeto usuario y solo exponer su email.

## Herencia

La herencia es el proceso de crear una clase a partir de otra clase. Por ejemplo, podemos crear una clase usuario que tenga un nombre, un apellido, un email, etc. y luego crear una clase administrador que herede de la clase usuario y tenga un nombre, un apellido, un email, etc. y ademas tenga un rol de administrador.

## Polimorfismo

El polimorfismo es el proceso de redefinir un metodo de una clase padre en una clase hija. Por ejemplo, podemos crear una clase usuario que tenga un metodo iniciar_sesion() y luego crear una clase administrador que herede de la clase usuario y tenga un metodo iniciar_sesion() que ademas de iniciar sesion, haga otras cosas.

## Clases y objetos

Una clase es una plantilla para crear objetos. Por ejemplo, podemos crear una clase usuario que tenga un nombre, un apellido, un email, etc. y luego crear un objeto usuario que tenga un nombre, un apellido, un email, etc.

## Metodos y atributos

Un metodo es una funcion que pertenece a una clase. Por ejemplo, podemos crear una clase usuario que tenga un metodo iniciar_sesion() y luego crear un objeto usuario que tenga un metodo iniciar_sesion().

Un atributo es una variable que pertenece a una clase. Por ejemplo, podemos crear una clase usuario que tenga un atributo email y luego crear un objeto usuario que tenga un atributo email.

## Instanciacion

La instanciacion es el proceso de crear un objeto a partir de una clase. Por ejemplo, podemos crear una clase usuario que tenga un nombre, un apellido, un email, etc. y luego crear un objeto usuario que tenga un nombre, un apellido, un email, etc.

## Ejemplo

```python
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def iniciar_sesion(self):
        print(f'Iniciando sesion con el email {self.email}')
```

```python
usuario = Usuario('Juan', 'Perez', 'juan@email.com')

print(usuario.nombre)
print(usuario.apellido)
print(usuario.email)
```

## Ejercicio

Crear una clase usuario que tenga un nombre, un apellido, un email, un rol y un metodo iniciar_sesion() que imprima el email del usuario.

## Solucion

```python
class Usuario:
    def __init__(self, nombre, apellido, email, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.rol = rol

    def iniciar_sesion(self):
        print(f'Iniciando sesion con el email {self.email}')
```

```python
usuario = Usuario('Juan', 'Perez', 'juan@email.com', 'usuario')

usuario.iniciar_sesion()
```

## Ejercicio

Crear una clase administrador que herede de la clase usuario y tenga un metodo iniciar_sesion() que imprima el email del administrador.

## Solucion

```python
class Usuario:
    def __init__(self, nombre, apellido, email, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.rol = rol

    def iniciar_sesion(self):
        print(f'Iniciando sesion con el email {self.email}')

class Administrador(Usuario):

    def iniciar_sesion(self):
        print(f'Iniciando sesion con el email {self.email} y el rol {self.rol}')
```

```python
administrador = Administrador('Juan', 'Perez', 'juan.admin@email.com', 'administrador')

administrador.iniciar_sesion()
```

## Porque necesitamos la POO

### POO vs Procedural
