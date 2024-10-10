class Alumno:
    #Crea la función constructor con atributos vacios "_init_", "none"
    def _init_(self):
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None
        self.__nombre_completo= None

    # Métodos para asignar valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    def set_nombre_completo(self, nombre_completo):
        self.__nombre_completo = nombre_completo

    # Métodos para obtener valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_nombre_completo(self):
        return self.__nombre_completo

    def get_nombre_completo_2(self):
        return self._nombre + " " + self.apellido_paterno + " " + self._apellido_materno

# Ejemplo de uso : Crear la instancia de Alumno
# Una instancia es la creación de un objeto a partir de una clase
alumno = Alumno()

registro_alumnos = { }

#Capturar tres registros
for i in range(3):
    alumno = Alumno()
    alumno.set_nombre(input("Introduce el nombre: "))
    alumno.set_apellido_paterno(input("Introduce el apellido paterno: "))
    alumno.set_apellido_materno(input("Introduce el apellido materno: "))
    alumno.set_no_control(input("Introduce el número de control del alumno: "))
    alumno.set_semestre(int(input("Introduce el semestre: ")))

    registro_alumnos[i] = alumno

#Mostrar los nombres de los registros
for i in range(3):
    print(f"Nombre: {registro_alumnos[i].get_nombre()}")


# #Asignar valoópres a los setters.
# alumno.set_nombre("Juan")
# alumno.set_apellido_paterno("Pérez")
# alumno.set_apellido_materno("Gómez")
# alumno.set_no_control("449100")
# alumno.set_semestre(3)
# alumno.set_nombre_completo("Juan Pérez Gómez")

#registro_alumnos[0] = alumno

#print(f"Nombre : {registro_alumnos[0].get_nombre()}")

# print(f"Nombre: {alumno.get_nombre()}")
# print(f"Apellido paterno: {alumno.get_apellido_paterno()}")
# print(f"Apellido materno: {alumno.get_apellido_materno()}")
# print(f"Número de control: {alumno.get_no_control()}")
# print(f"Semestre: {alumno.get_semestre()}")
# # print(f"Nombre completo: {alumno.get_nombre_completo()}")
# print(f"Nombre completo: {alumno.get_nombre_completo_2()}")
