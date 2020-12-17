import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

class FirebaseData():

    def __init__(self):
        self.configuration = {
            'apiKey': os.getenv('APIKEY'),
            'authDomain': os.getenv("AUTHDOMAIN"),
            'databaseURL': os.getenv("DATABASEURL"),
            'storageBucket': os.getenv("STORAGEBUCKET"),
        }

        self.initialize()

    def initialize(self):

        try:
            self.firebase = pyrebase.initialize_app(self.configuration)
            self.database = self.firebase.database()
        except Exception as e:
            print(str(e))
            return False



    def getall_data(self):
        data = self.database.child('users').get()
        for keys, values in data.items():
            print(keys)


    def Set(self, name, data):
        result = self.database.child('users').child(name).set(data)
        return result


if __name__ == '__main__':
    obj = FirebaseData()


