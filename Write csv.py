import csv

with open('Progress.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Day', 'Month', 'Transcriptions'])
    f.close()