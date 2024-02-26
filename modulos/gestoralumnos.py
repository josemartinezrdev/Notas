from tabulate import tabulate
import os


alumno = {}


def AddStudent(alumnos: dict):  # ? dict para definir como diccionario
    id = input('Ingrese un id para registrar un estudiante:\n-> ')
    nombre = input('Ingrese el nombre del estudiante:\n-> ')

    try:
        edad = int(input(f'Ingrese la edad de {nombre}:\n-> '))
    except ValueError:
        print('La edad debe ser numérica')
        AddStudent(alumnos)
    else:
        email = input(f'Ingrese el email de {nombre}:\n-> ')
        alumno = {
            'id': id,
            'nombre': nombre,
            'edad': edad,
            'email': email
        }
        alumnos.update({id: alumno})


def SearchStudent(alumnos: dict):
    id = input('Ingrese Id del Estudiante:\n-> ')
    data = alumnos.get(id, False)
    if (type(data) == dict):
        pass
    elif ((type(data) == bool) and (data == False)):
        print('El estudiante no se encuentra registrado.')


def ListData(alumnos: dict):
    info = []
    for key, value in alumnos.items():  # ? .items() para desestructurar (enumerate)
        info.append(value)
    print(tabulate(info, headers="keys", tablefmt='pretty'))


# -> dataType : para  definir que dato devuelve la func
def ValidateStudent(alumnos: dict, id) -> bool:
    return bool(alumnos.get(id, ''))


def DelStudent(alumnos: dict):
    id = input('Ingrese Nro Id del estudiante:\n-> ')
    if (ValidateStudent(alumnos, id) == True):
        alumnos.pop(id)
        print(ValidateStudent(alumnos, id))
    else:
        print(f'El estudiante con id {id} no esta registrado')


def DelByName(alumnos: dict):
    nombre = input('Ingrese nombre del estudiante:\n-> ')
    for llave, valor in alumnos.items():
        if (nombre in valor['nombre']):
            alumnos.pop(llave)
            break
    ListData(alumnos)


def AddGrades(alumnos: dict):
    notas = {
        'parciales': [],
        'quices': [],
        'trabajos': [],
    }

    id = input('Ingrese Id del estudiante al cual se le añadirán las calificaciones:\n-> ')
    data = alumnos.get(id, False)
    if (type(data) == dict):

        try: 
            numNotas = int(input('Cuantos parciales desea ingresar?\n-> '))

            for i in range(numNotas):
                nota = int(input('Ingrese nota parcial\n-> '))
                notas['parciales'].append(nota)

            numNotas = int(input('Cuantos quices desea ingresar?\n-> '))

            for i in range(numNotas):
                nota = int(input('Ingrese nota quiz\n-> '))
                notas['quices'].append(nota)

            numNotas = int(input('Cuantos trabajos desea ingresar?\n-> '))

            for i in range(numNotas):
                nota = int(input('Ingrese nota del trabajo\n-> '))
                notas['trabajos'].append(nota)
        except ValueError:
            print('Los datos deben ser numéricos')
            AddGrades(alumnos)
        else:
            for clave in alumnos:
                if clave == alumnos[id]['id']:
                        alumnos[id].update({'calificaciones': notas})
            return True
        return True
        

    elif ((type(data) == bool) and (data == False)):
        op = False
        if op != True:
            print('El estudiante aun no esta registrado. Enter para registrarlo.')
            os.system('pause')
            return


