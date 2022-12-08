import csv
import arrow
import pandas as pd


class GeneratorCSV:

    def __init__(self):
        self.date = arrow.utcnow()
        self.year = str(self.date.year)
        self.month = str(self.date.month)
        self.day = str(self.date.day)

    def create_csv(self, values: list):
        with open(f'{self.year}{self.month}{self.day}toprapspoti.csv', 'w') as file:
            df = pd.DataFrame(values)
            df.to_csv(f'{self.year}{self.month}{self.day}toprapspoti.csv', index=False, header=False)
