dias_semana = ["Lunes","Martes","Mircoles","Jueves","Viernes","Sabado","Domingo" ]
dias_temeratura = []
suma = 0

for dia in dias_semana:
    temp = float(input(f"Ingrese la temperatura para {dia}: "))
    suma += temp
    dias_temeratura.append(temp)

print("promedio", suma / len(dias_semana))