import numpy as np
import pickle

from knn import KNN

knn = KNN()

test3String = "./userData/test3.p"
pickle_in = open(test3String,"rb")
test3 = pickle.load(pickle_in)

test4String = "./userData/test4.p"
pickle_in = open(test4String,"rb")
test4 = pickle.load(pickle_in)

train3String = "./userData/train3.p"
pickle_in = open(train3String,"rb")
train3 = pickle.load(pickle_in)

train4String = "./userData/train4.p"
pickle_in = open(train4String,"rb")
train4 = pickle.load(pickle_in)



#print(test3)
#print(test4)
#print(train3)
#print(train4)
#print(test3.shape)
#print(test4.shape)
#print(train3.shape)
#print(train4.shape)

def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    return X

def ReshapeData(set1,set2):
    X = np.zeros((2000,5*2*3),dtype='f')
    Y = np.zeros(2000)
    for row in range(0,1000):
        Y[row] = 3
        Y[row+1000] = 4
        col = 0
        for finger in range(0,5):
            for bone in range(0,2):
                for tipBase in range(0,3):
                    X[row,col] = set1[finger,bone,tipBase,row]
                    X[row+1000,col] = set2[finger,bone,tipBase,row]
                    col = col + 1
    return X, Y

def CenterData(X):
    allXCoordinates = X[:,:,0,:]
    meanValue = allXCoordinates.mean()
    X[:,:,0,:] = allXCoordinates - meanValue
    allXCoordinates = X[:,0,:,:]
    meanValue = allXCoordinates.mean()
    X[:,0,:,:] = allXCoordinates - meanValue
    allXCoordinates = X[0,:,:,:]
    meanValue = allXCoordinates.mean()
    X[0,:,:,:] = allXCoordinates - meanValue
    #exit()
    return X

train3 = ReduceData(train3)
train4 = ReduceData(train4)
test3 = ReduceData(test3)
test4 = ReduceData(test4)

train3 = CenterData(train3)
train4 = CenterData(train4)
test3 = CenterData(test3)
test4 = CenterData(test4)

trainX, trainY = ReshapeData(train3, train4)
testX, testY = ReshapeData(test3, test4)
#print(trainX)
#print(trainY)
#print(trainX.shape)
#print(trainY.shape)
print(testX)
print(testY)
print(testX.shape)
print(testY.shape)

knn.Use_K_Of(15)
knn.Fit(trainX,trainY)

wrongPrediction = 0
for row in range(0,2000):
    prediction = knn.Predict(testX[row])
    actual = testY[row]
    if (prediction != actual):
        wrongPrediction = wrongPrediction + 1
    
print("Wrong Predictions: ", wrongPrediction)
    
#[numItemsTrain, numFeatures] = knn.data.shape
