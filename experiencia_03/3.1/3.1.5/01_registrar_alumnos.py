curso = []
counter = 0
while counter < 30:
    if counter == 29:
        print('No hay mas cupos en este curso')

    alumno = {}
    alumno['name'] = input('Ingrese el nombre del alumno: ')
    alumno['address'] = input('Ingrese la dirección del alumno: ')
    alumno['phone'] = input('Ingrese el teléfono del alumno: ')
    curso.append(alumno)

    choice = input('Desea agregar otro alumno (s/n): ')
    if choice == 'n':
        break

for alumno in curso:
    print()
    print(f'Nombre: {alumno["name"]}')
    print(f'Dirección: {alumno["address"]}')
    print(f'Teléfono: {alumno["phone"]}')
    
        