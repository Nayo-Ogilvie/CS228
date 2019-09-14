import numpy as np
import pickle

class READER:
    def __init__(self):
        self.pickle_in = open("./userData/gesture2.p","rb")
        self.gestureData = pickle.load(self.pickle_in)
        print(self.gestureData)