import csv

class Animals():
    def __init__(self, userInput):
        self.userInput = userInput
        
    def getData(self):
        try:
            with open(f"./data/{self.userInput}.csv") as f:
                test = csv.reader(f)
                for row in test:
                    if row[0] != "name":
                        print(f"{row[0]} is a{row[1]} year old{row[2]}")
        except:
            print(f"Sorry, we don't have any {self.userInput} here.")
            

animal1 = Animals("dogs")
animal1.getData()