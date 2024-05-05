import pymongo
import time
import json

class DBInterface:


    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mydatabase"]
        self.collection = self.db["mycollection"]
        self.sauces = self.db["mysauces"]
        
    def extract_Events(self):
        cursor = self.collection.find({})
        names = []
        event_ids = []
        last_event_id = -1
        for doc in cursor:
            name = doc.get("Event")
            event_id = doc.get("Event_ID")
            if name:
                names.append(name)
                event_ids.append(event_id)
            if  int(event_id) > last_event_id:
                last_event_id = int(event_id)
        return event_ids, names, last_event_id
    
    def write_Event(self, event_id, event_name, sauces):
        curr_time = time.time()
        data = {"Event_ID" : event_id, "Event": event_name, "Time": curr_time, "Sauces": str(json.dumps(sauces))}
        self.collection.insert_one(data)

    def replace_Event(self, event_id, event_name, sauces):
        filter = {"Event_ID" : event_id, "Event": event_name}
        print(filter)
        update = {"$set": {"Sauces": str(json.dumps(sauces))}}
        self.collection.update_one(filter, update)

    def search_Event(self, event_name, event_id):
        result = self.collection.find_one({"$and": [{"Event": event_name}, {"Event_ID": event_id}]})
        if result:
            print("Event found:")
            return result["Sauces"]
        else:
            print("Event not found.")

    def extract_sauces(self):
        cursor = self.sauces.find({})
        sauces = []
        for doc in cursor:
            sauceName = doc.get("name")
            sauces.append(sauceName)
        return sauces
    
    def add_sauce(self, sauce_name):
        self.sauces.insert_one({'name': sauce_name})


