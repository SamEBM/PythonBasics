# Obtener la segunda mejor calificación de una lista de alumnos de la forma
# [['Samuel', 9.0],['Eduardo', 8.0],['Benitez', 8.0],['Miranda', 7.0]]
# Se debe imprimir el nombre de la(s) persona(s) que tengan la segunda peor calificación en orden alfabetico
# Output del ejemplo: 
# Benitez
# Eduardo

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    newlist = [x[1] for x in students]
    scores = set(newlist)
    newlist = list(scores)
    newlist.sort()
    print(newlist)

    secondScore = newlist[1]
    print(secondScore)

    final = [x for x in students if secondScore == x[1]]
    print(final)

    final.sort()
    for x in final:
        print(x[0])