# Work progress analysis project
# Ver: 0 .0 .1

import csv
import pandas as pd
import numpy as np
#import 'Write csv.py'


months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre','Noviembre', 'Diciembre']
en, fe, ma, ab, may, jun, jul, ag, se, oc, no, dic = list(range(1,32)), list(range(1,29)), list(range(1,32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32))

with open('Progress.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    dias = int(input('Cuantos dias vas a introducir? '))
    for i in range(1,dias+1):
        mes = input("Introduce un mes: ")
        mes = mes.capitalize()
        if mes in months:
            dia = int(input("Introduce el dia: "))
            if dia in range(1,32):
                tran = int(input("Introduce el numero de transcripciones: "))
            else:
                dia = int(input("Los meses tienen hasta 31 dias, por favor introduzca de nuevo el dia! "))
                tran = int(input("Introduce el numero de transcripciones: "))
        else:
            mes = input("Introduce un mes valido por favor! ")
            mes = mes.capitalize()      
            dia = int(input("Introduce el dia: "))
            if dia in range(1,32):
                tran = int(input("Introduce el numero de transcripciones: "))
            else:
                dia = int(input("Los meses tienen hasta 31 dias, por favor introduzca de nuevo el dia! "))
                tran = int(input("Introduce el numero de transcripciones: "))   
        writer.writerow([dia, mes, tran])
