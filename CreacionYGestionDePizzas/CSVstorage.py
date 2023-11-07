import csv

class CSVstorage:

    def __init__(self, file):
        self.file = file

    def save(self, data):
        with open(self.file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def load(self):
        with open(self.file, "r") as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data