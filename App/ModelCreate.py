
import sys
import os
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier


class Training:

    def train():


        alg=RandomForestClassifier()
            
        
        df = pd.read_csv("Dataset.csv")
        y_train = df['Label']
        del df['Label']
        del df['activity_level']
        del df['BMI_tags']
        del df['calories_to_maintain_weight']
        del df['Sno']
    
        X = df
        y = y_train

        
        clf = alg

        clf.fit(X, y)

        with open('model.sav', 'wb') as f:
            pickle.dump(clf,f)



if __name__ == "__main__":

    Training.train()
