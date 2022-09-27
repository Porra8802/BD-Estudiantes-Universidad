import procesamiento_db as modulo

while True:
    print("")
    print("___Estudiantes___")
    print("1. Registar Alumno")
    print("2. Listar Alumno")
    print("3. Buscar Alumno")
    print("4. Actualizar Carrera Alumno")
    print("5. Eliminar Alumno")
    print("6. Cerrar Sistema")
    print("__"*10)
    opcion=int(input("Elige una opción (1-6): ").strip())
    print("__"*10)
    print("")

    if opcion==1:
        print("___Datos del Alumno___")
        nom=input("Nombre: ").strip().capitalize()
        ape=input("Apellido: ").strip().capitalize()
        car=input("Carrera: ").strip().capitalize()
        edad=int(input("Edad: ").strip())
        res=modulo.register_alumn(nom, ape, car, edad)
        if res==1:
            print("Hubo un error")
        else:
            print("__¡Alumno Inscrito Exitosamente!__")
        
    elif opcion==2:
        print("___Listado de los Alumnos___")
        res=modulo.list_alumns()
        print(res)

    elif opcion==3:
        print("___Buscar un Alumno___")
        id_alumn=int(input("ID del Alumno: ").strip())
        res=modulo.get_alumn_by_id(id_alumn)
        if res==1:
            print("Hubo un error")
        elif res==():
            print("__No existe un alumno con ese ID__")
        else:
            print(res)
    
    elif opcion==4:
        print("__Actualizar carrera de un Alumno___")
        id_alumn=int(input("ID del Alumno: ").strip())
        res=modulo.get_alumn_by_id(id_alumn)
        if res==1:
            print("Hubo un error")
        elif res==():
            print("__No existe un alumno con ese ID__")
        else:
            carr=input("Ingresa nueva carrera: ").strip().capitalize()
            res=modulo.update_carreer_alumn(carr, id_alumn)
            if res==1:
                print("Hubo un error al actualizar")
            else:
                print("__Carrera actualizada con exito__")

    elif opcion==5:
        print("__Eliminar un Alumno___")
        id_alumn=int(input("ID del Alumno: ").strip())
        res=modulo.get_alumn_by_id(id_alumn)
        if res==1:
            print("Hubo un error")
        elif res==():
            print("__No existe un alumno con ese ID__")
        else:
            res=modulo.delete_alumn_by_id(id_alumn)
            if res==1:
                print("Hubo un error al eliminar")
            else:
                print("__Alumno eliminado con exito__")

    elif opcion==6:
        print("__Sistema Cerrado__")
        break
    
    else:
        print("Ha habido un error, por favor intentalo nuevamente")


        