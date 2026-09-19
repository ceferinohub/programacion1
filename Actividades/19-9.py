Alumnos = ["Juan", "Maria", "Pedro", "Ana", "Luis"] #pero yo quiero saber si esos estan o no estan regular ?

#¿ Que dictamina si un alumno esta o no esta regular ?

#Necesitamos tener las 4 notas alumnos para poder determinar si estan regulares o no.

#Y saber el % de asistencia de cada alumno.

alumnos = [{"nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90 }, 
           {"nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60 }, 
           {"nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95 },
           {"nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85 }]

for i in alumnos:
    nombre = i["nombre"]
    notas = i["notas"]
    asistencia = i["asistencia"]
    todaslasnotas = 0
    for j in notas:
        if j >=6:
            todaslasnotas=todaslasnotas+1
        promedionotas=sum(notas)/len(notas)
        if todaslasnotas==len(notas) and promedionotas >= 6 and asistencia >= 75:
            print(nombre, "esta regular")
        else:
            print(nombre, "no esta regular")
        
    

    
        
        
