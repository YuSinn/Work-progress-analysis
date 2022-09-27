import csv

def new_month(month):
    with open(month, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Day', 'Month', 'Transcriptions'])
        f.close()