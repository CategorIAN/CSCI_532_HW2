import pandas as pd
from tabulate import tabulate

class PointPartition:
    def __init__(self, partition, error):
        self.df = pd.DataFrame({"Partition": partition})
        self.error = error

    def __str__(self):
        return "Partition: {}\nError: {}".format(tabulate(self.df, headers='keys', tablefmt='psql'), self.error)

