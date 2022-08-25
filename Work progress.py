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
        dia = input("Introduce el dia: ")
        if dia in range(1,32):
            mes = input("Introduzca el mes: ")
        else:
            dia = input("Por favor introduzca un numero de 1 a 31: ")
        if mes in months:
            tran = input("Introduce el numero de transcripciones: ")
        else:
            mes = input("Por favor introduzca un mes valido! ")
            tran = tran = input("Introduce el numero de transcripciones: ")    
        writer.writerow([dia, mes, tran])
