
import sys
import os
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score,confusion_matrix
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier


class Training:

    def train(algo):


        if algo==1:
            alg=MultinomialNB()
        elif algo==2:
            alg=MLPClassifier()
        elif algo==3:
            alg=LinearSVC()
        else:
            alg=RandomForestClassifier()
            
        
        df = pd.read_csv("Dataset.csv")
        y_train = df['Label']
        del df['Label']
        del df['Sno']
    
        X = df
        y = y_train

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        clf = alg

        clf.fit(X_train, y_train)

        predicted = clf.predict(X_test)

        accuracy = accuracy_score(y_test, predicted)*100

        precision = precision_score(y_test, predicted, average="macro")*100

        recall = recall_score(y_test, predicted, average="macro")*100

        fscore = f1_score(y_test, predicted, average="macro")*100

        print("%=",accuracy,precision,recall,fscore)

        return (accuracy,precision,recall,fscore)




if __name__ == "__main__":

    #Training.train(1)
    
    #Training.train(2)
    Training.train(3)
    #Training.train(4)
