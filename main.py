import csv

class Animals():
    def __init__(self, user_input):
        self.user_input = user_input
        
    def getData(self):
        try:
            with open(f"./data/{self.user_input}.csv") as f:
                animal_data = csv.reader(f)
                for row in animal_data:
                    if row[0] != "name":
                        print(f"{row[0]} is a{row[1]} year old{row[2]}")
        except:
            print(f"Sorry, we don't have any {self.user_input} here.")
            

animal1 = Animals("dogs")
animal1.getData()