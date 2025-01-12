
import pickle


def predict(data):

    
    clf = pickle.load( open( "model.sav", "rb" ) )

    
    predicted = clf.predict([data])

    print(predicted[0])
    return predicted[0]

    

if __name__ == '__main__':
    predict([22.0, 98.0, 180.0, 1.0, 11.0, 11.0])

