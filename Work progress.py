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
    if dias > 0:
        for i in range(1,dias+1):
            mes = input("Introduce el mes: ")
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
                    dia = int(input("Los meses tienen hasta 31 dias, por favor introduzca de nuevo el dia! -> "))
                    tran = int(input("Introduce el numero de transcripciones: ")) 
            print('~~~ \n ~~~\n~~~')  
            writer.writerow([dia, mes, tran])
    else:
        pass

work_df = pd.read_csv('Progress.csv')

def work_analisys(df):
    print('           ############ Work progress analisys ############           ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('1.) The average transcriptions for ' + str(work_df['Month'][0]) + ' is ' + str(np.average(work_df['Transcriptions'])))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('2.) Total transcriptions in ' + str(work_df['Month'][0]) +' is ' +str(np.sum(work_df['Transcriptions'])) +' of ' + str(1890*np.count_nonzero(work_df['Transcriptions'])))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('3.) The objective of the month was surpased with ' + str(np.sum(work_df['Transcriptions'])-1890*np.count_nonzero(work_df['Transcriptions'])) + ' transcriptions')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('4.) The revenue for ' + str(work_df.Month[0]) + ' is ' + str(round((np.sum(work_df['Transcriptions'])-1890*np.count_nonzero(work_df['Transcriptions']))*0.028,2)) +'€')      
work_analisys(work_df)