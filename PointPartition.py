import pandas as pd
from tabulate import tabulate

class PointPartition:
    def __init__(self, partition, error):
        self.df = pd.DataFrame({"Partition": partition})
        self.error = error

    def __str__(self):
        return "Partition: {}\nError: {}\nLines: {}".format(tabulate(self.df, headers='keys', tablefmt='psql'),
                                                            self.error, self.df.shape[0])

    def fitPoints(self):
        fitted = self.df['Partition'].map(lambda pts: pts.df if pts.n == 1 else pts.bestLine().fitPoints(pts.df['x']))
        return pd.concat(list(fitted))


