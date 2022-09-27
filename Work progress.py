# Work progress analysis project
# Ver: 0 .0 .1

import csv
import pandas as pd
import numpy as np
from Write_csv import *


months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre','Noviembre', 'Diciembre']
en, fe, ma, ab, may, jun, jul, ag, se, oc, no, dic = list(range(1,32)), list(range(1,29)), list(range(1,32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32)), list(range(1, 31)), list(range(1, 32))

mes_to_work = input('Que mes quieres editar? ')

with open(mes_to_work, 'a', newline='') as file:
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

work_df = pd.read_csv(mes_to_work)

def work_analisys(df):
    if work_df['Month'][0] == 'Agosto':
        print('           ############ Work progress analisys ############           ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('1.) The average transcriptions for ' + str(work_df['Month'][0]) + ' is ' + str((int(round(np.average(work_df['Transcriptions']),0))))+'.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('2.) Total transcriptions in ' + str(work_df['Month'][0]) +' is ' +str(np.sum(work_df['Transcriptions'])) +' of ' + str(1890*np.count_nonzero(work_df['Transcriptions']))+'.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('3.) The objective of the month was surpased with ' + str(np.sum(work_df['Transcriptions'])-1890*np.count_nonzero(work_df['Transcriptions'])) + ' transcriptions.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('4.) The revenue for ' + str(work_df.Month[0]) + ' is ' + str(round((np.sum(work_df['Transcriptions'])-1890*np.count_nonzero(work_df['Transcriptions']))*0.028,2)) +'€.')      
    else:
        print('           ############ Work progress analisys ############           ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('1.) The average transcriptions for ' + str(work_df['Month'][0]) + ' is ' + str((int(round(np.average(work_df['Transcriptions']),0))))+'.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('2.) Total transcriptions in ' + str(work_df['Month'][0]) +' is ' +str(np.sum(work_df['Transcriptions'])) +' of ' + str(2227*np.count_nonzero(work_df['Transcriptions']))+'.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('3.) The objective of the month was surpased with ' + str(np.sum(work_df['Transcriptions'])-2227*np.count_nonzero(work_df['Transcriptions'])) + ' transcriptions.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('4.) The revenue for ' + str(work_df.Month[0]) + ' is ' + str(round((np.sum(work_df['Transcriptions'])-2227*np.count_nonzero(work_df['Transcriptions']))*0.028,2)) +'€.')
work_analisys(work_df)
if input('Quieres introducir un nuevo mes? (Si/No) ') == 'Si':
    new_month(input('Introduzca el nuevo mes: '))
else:
    pass