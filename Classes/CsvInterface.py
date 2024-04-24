import csv
import pandas as pd
import time

class CsvInterface:

    def writeSauces(self, event_id, sauces):
        data = pd.read_csv('Sauzen.csv')
        currTime = time.time()
        print(currTime)
        print(data['Event ID'].values)
        # Check if event ID already exists
        if event_id in data['Event ID'].values:
            # Update quantities for existing entries
            for sauce_name, quantity in sauces.items():
                quantity = int(quantity)
                if quantity > 0:
                    # Update quantity for existing sauce in the event
                    data.loc[(data['Event ID'] == event_id) & (data['Sauce'] == sauce_name), 'Quantity'] += quantity
        else:
            # Add new rows for sauces in the event
            for sauce_name, quantity in sauces.items():
                    # Get sauce name based on sauce ID  # You need to implement this method
                    new_row = {'Event ID': event_id, 'Event': 'test', 'Time': currTime, 'Sauce': sauce_name, 'Quantity' : quantity} #Hier heb ik test gezet, maar daar zou de eventID moeten staan
                    data = data.append(new_row, ignore_index=True)

        # Write updated data back to CSV
        data.to_csv('Sauzen.csv', index=False)

        # Event, Time, Sauce, Quantity



#bolognese
#carbonnara
#porcini
#arrabiata
#tomaat
#tomatensaus_met_groentjes