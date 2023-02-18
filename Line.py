import pandas as pd

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def fitPoints(self, pts):
        x_vals = pts.df['x']
        df = pd.DataFrame({'x': x_vals, 'y': x_vals.map(lambda x: self.a * x + self.b)})
        return df

