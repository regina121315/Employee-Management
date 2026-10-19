from db import getC

if getC:
    conn = getC()
    cursor = conn.cursor()


def alta():
    nombre = input("ingresa el nombre del empleado: ")
    salario = int(input("Ingresa el salario del empleado: "))
    edad = int(input("Ingresa la edad del empleado: "))
    status = int(input("Status del empleado: "))
    puesto_id = int(input("Puesto del empleado: "))
    cursor.execute(
        "insert into empleados(nombre,salario,edad,status,puesto_id) values (%s,%s,%s,%s,%s)",
        (nombre, salario, edad, status, puesto_id),
    )
    conn.commit()
    print("Empleado Agregado")


def baja():
    id = int(input("Ingresa el id del empleado que desea dar de baja: "))
    t = int(input("Inhabilita al empleado con 0: "))
    cursor.execute("update empleados set status=%s where id=%s", (id, t))
    conn.commit()
    print("Empleado dado de baja")


def login():
    while True:
        cursor.execute(
            "select e.id, e.nombre, u.password from empleados e join usuarios u on e.id = u.id_user;"
        )
        users = cursor.fetchall()
        print(users)
        id = int(input("Ingresa tu ID de usuario: "))
        ps = int(input("Ingresa tu contraseña: "))
        for i in users:
            if i[0] == id:
                if i[2] == ps:
                    menu()
                else:
                    print(f"{id} no existe, intente de nuevo.")
                login()


def actualizacion():
    id = int(input("Ingresa el id del empleado que desea actualizar: "))
    nombre = input("ingresa el nombre del empleado: ")
    salario = int(input("Ingresa el salario del empleado: "))
    edad = int(input("Ingresa la edad del empleado: "))
    status = int(input("Status del empleado: "))
    puesto_id = int(input("Puesto del empleado: "))
    cursor.execute(
        "update empleados set nombre=%s, salario=%s, edad=%s, status=%s, puesto_id=%s where id=%s",
        (nombre, salario, edad, status, puesto_id, id),
    )
    conn.commit()
    print("Empleado Actualizado")


def consult():
    cursor.execute("select * from empleados")
    re = cursor.fetchall()
    for i in re:
        print(i)


def consultP():
    cursor.execute("select AVG(salario) from empleados")
    r = cursor.fetchall()
    for e in r:
        print(e)


def salario():
    cursor.execute(
        "select p.nombre, AVG(e.salario) from empleados e join puestos p on e.id=p.id GROUP BY p.nombre;"
    )
    q = cursor.fetchall()
    for t in q:
        print(t)


def menu():
    while True:
        try:
            print("--- Bienvenido---")
            print("1. Dar de alta a empleados")
            print("2. Dar de baja a empleados")
            print("3. Actualizacion de informacion")
            print("4. Consultar empleados")
            print("5. Promedio total del salario")
            print("6. Promedio salario por puesto")
            print("0. Salir ")
            op = int(input("Selecciona una opcion: "))
            if op == 1:
                alta()
            elif op == 2:
                baja()
            elif op == 3:
                actualizacion()
            elif op == 4:
                consult()
            elif op == 5:
                consultP()
            elif op == 6:
                salario()
            elif op == 0:
                print("Chao")
                break
            else:
                print("Opcion invalida")
        except Exception as e:
            print("Error")


login()
