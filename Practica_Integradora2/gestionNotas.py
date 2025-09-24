alumnos = {60902 : "Rodolfo Fernandez",61654 : "Luis Gomez",61852: "Andrea Pereira", 61754 : "Juan Cruz Gonzales"}
materias = [["Ciencias", 0, 0,0 ],["Historia",0 ,0 ,0],["Geografia",0 ,0 ,0 ],["Matematica",0 ,0 ,0 ],["Fisica",0 ,0 ,0 ]]
notasFinales = [["Rodolfo Fernandez",0],["Luis Gomez",0],["Andrea Pereira",0],["Juan Cruz Gonzales",0]]
materiasCargadas = []
def pedirNotas(materias):
    for materia in materias:
        while True:
            nota1 = int(input(f"Ingrese Nota 1 para {materia[0]}: "))
            if 0 <= nota1 <= 10:
                break
            print("Ingrese una nota valida entre 0 y 10")
        materia[1] = nota1

        while True:
            nota2 = int(input(f"Ingrese Nota 2 para {materia[0]}: "))
            if 0 <= nota2 <= 10:
                break
            print("Ingrese una nota valida entre 0 y 10")
        materia[2] = nota2
        promedio = (nota1 + nota2) / 2
        materia[3] = promedio
for i in alumnos:
    print(f"Legajo = {i} Nombre = {alumnos[i]}")
    materiasAlumno = [
        ["Ciencias", 0, 0, 0],
        ["Historia", 0, 0, 0],
        ["Geografia", 0, 0, 0],
        ["Matematica", 0, 0, 0],
        ["Fisica", 0, 0, 0]
    ]
    pedirNotas(materiasAlumno)
    materiasCargadas.append([alumnos[i], materiasAlumno])
for alumno, materias in materiasCargadas:
    print(f"Alumno {alumno}")
    for materia in materias:
        print(materia)

