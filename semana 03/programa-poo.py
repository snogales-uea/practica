class DiaClima:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

    def mostrar(self):
        print(self.dia, " ",  self.temperatura)

class SemanaClima:
    def __init__(self, dias):
        self.dias = dias

    def promedio(self):
        suma = 0
        for dia in self.dias:
            suma += dia.temperatura

        print("promedio", suma / len(self.dias))

dias_semana = ["Lunes","Martes","Mircoles","Jueves","Viernes","Sabado","Domingo" ]
dias_temeratura = []
for dia in dias_semana:
    temp = float(input(f"Ingrese la temperatura para {dia}: "))
    diaClima = DiaClima(dia, temp)
    #diaClima.mostrar()
    dias_temeratura.append(diaClima)

semana_semana = SemanaClima(dias_temeratura)
semana_semana.promedio()