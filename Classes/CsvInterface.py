import csv
import pandas as pd
import time
import json

class CsvInterface:

    def writeSauces(self, event_id,event, sauces):
        data = pd.read_csv('Sauzen.csv')
        currTime = time.time()
        print(currTime)
        print(data['Event'].values)
        print(sauces)
        sauces = json.dumps(sauces)
        new_row = [event_id,event, currTime, str(sauces)]
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