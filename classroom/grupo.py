from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12" 

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []

    def listadoAsignaturas(self, **kwargs):
        for key, value in kwargs.items():
            self._asignaturas.append(Asignatura(value))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos.extend(lista)

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
