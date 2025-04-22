import pandas as pd 

class Fil_reader:
    """
    Gjør datasettets innhold leselig og manipulert
    """
    
    def __init__(self, fil):

        self.df = pd.read_csv(fil, encoding = "utf-8-sig", delimiter = "\t") #Skiprows må sees ann, latin1 kan være bedre encoding
        self.rader = self.df.columns
        for rad in self.rader:
            self.df[rad] = pd.to_numeric(self.df[rad], errors = "coerce")
