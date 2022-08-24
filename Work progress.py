# Work progress analysis project
# Ver: 0 .0 .1

import csv
import pandas as pd
import numpy as np

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre','Noviembre', 'Diciembre']
en, fe, ma, ab, may, jun, jul, ag, se, oc, no, dic = list(range(1,32)), list(range(1,29)), list(range(1,32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32))

with open('Progress.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Day', 'Month', 'Transcriptions'])
    for i in range(1,5):
        dia = input("Introduce el dia: ")
        mes = input("Introduce el mes: ")
        tran = input("Introduce el numero de transcripciones: ")
        w.writerow([dia, mes, tran])
    