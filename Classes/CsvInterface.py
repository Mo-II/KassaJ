import csv
import pandas as pd
import time

class CsvInterface:

    def writeSauces(self, event_id, sauces):
        data = pd.read_csv('Sauzen.csv')
        currTime = time.time()
        print(currTime)
        print(data['Event'].values)
        new_row = [event_id, currTime, str(sauces)]
        print(new_row)
        with open('Sauzen.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)

        file.close


#bolognese
#carbonnara
#porcini
#arrabiata
#tomaat
#tomatensaus_met_groentjes

