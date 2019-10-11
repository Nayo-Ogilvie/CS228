import numpy as np
import pickle

from knn import KNN

knn = KNN()

test0String = "./userData/Lee_test0.p"
pickle_in = open(test0String,"rb")
test0 = pickle.load(pickle_in)

train0String = "./userData/Lee_train0.p"
pickle_in = open(train0String,"rb")
train0 = pickle.load(pickle_in)

test1String = "./userData/Thissell_test1.p"
pickle_in = open(test1String,"rb")
test1 = pickle.load(pickle_in)

test2String = "./userData/Thissell_test2.p"
pickle_in = open(test2String,"rb")
test2 = pickle.load(pickle_in)

train1String = "./userData/Thissell_train1.p"
pickle_in = open(train1String,"rb")
train1 = pickle.load(pickle_in)

train2String = "./userData/Thissell_train2.p"
pickle_in = open(train2String,"rb")
train2 = pickle.load(pickle_in)

test3String = "./userData/Ogilvie_test3.p"
pickle_in = open(test3String,"rb")
test3 = pickle.load(pickle_in)

test4String = "./userData/Warren_test4.p"
pickle_in = open(test4String,"rb")
test4 = pickle.load(pickle_in)

train3String = "./userData/Ogilvie_train3.p"
pickle_in = open(train3String,"rb")
train3 = pickle.load(pickle_in)

train4String = "./userData/Warren_train4.p"
pickle_in = open(train4String,"rb")
train4 = pickle.load(pickle_in)

test5String = "./userData/Boland_test5.p"
pickle_in = open(test5String,"rb")
test5 = pickle.load(pickle_in)

test6String = "./userData/Boland_test6.p"
pickle_in = open(test6String,"rb")
test6 = pickle.load(pickle_in)

train5String = "./userData/Boland_train5.p"
pickle_in = open(train5String,"rb")
train5 = pickle.load(pickle_in)

train6String = "./userData/Boland_train6.p"
pickle_in = open(train6String,"rb")
train6 = pickle.load(pickle_in)

test7String = "./userData/Mardis_test7.p"
pickle_in = open(test7String,"rb")
test7 = pickle.load(pickle_in)

test8String = "./userData/Mardis_test8.p"
pickle_in = open(test8String,"rb")
test8 = pickle.load(pickle_in)

train7String = "./userData/Mardis_train7.p"
pickle_in = open(train7String,"rb")
train7 = pickle.load(pickle_in)

train8String = "./userData/Mardis_train8.p"
pickle_in = open(train8String,"rb")
train8 = pickle.load(pickle_in)

test9String = "./userData/Childs_test9.p"
pickle_in = open(test9String,"rb")
test9 = pickle.load(pickle_in)

train9String = "./userData/Childs_train9.p"
pickle_in = open(train9String,"rb")
train9 = pickle.load(pickle_in)



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

def ReshapeData(set1,set2,set3,set4,set5,set6,set7,set8,set9,set10):
    X = np.zeros((20000,5*2*3),dtype='f')
    Y = np.zeros(20000)
    for row in range(0,1000):
        Y[row] = 0
        Y[row+1000] = 0
        Y[row+2000] = 1
        Y[row+3000] = 1
        Y[row+4000] = 2
        Y[row+5000] = 2
        Y[row+6000] = 3
        Y[row+7000] = 3
        Y[row+8000] = 4
        Y[row+9000] = 4
        Y[row+10000] = 5
        Y[row+11000] = 5
        Y[row+12000] = 6
        Y[row+13000] = 6
        Y[row+14000] = 7
        Y[row+15000] = 7
        Y[row+16000] = 8
        Y[row+17000] = 8
        Y[row+18000] = 9
        Y[row+19000] = 9
        col = 0
        for finger in range(0,5):
            for bone in range(0,2):
                for tipBase in range(0,3):
                    X[row,col] = set1[finger,bone,tipBase,row]
                    X[row+1000,col] = invertX(tipBase, set1[finger,bone,tipBase,row])
                    X[row+2000,col] = set2[finger,bone,tipBase,row]
                    X[row+3000,col] = invertX(tipBase, set2[finger,bone,tipBase,row])
                    X[row+4000,col] = set3[finger,bone,tipBase,row]
                    X[row+5000,col] = invertX(tipBase, set3[finger,bone,tipBase,row])
                    X[row+6000,col] = set4[finger,bone,tipBase,row]
                    X[row+7000,col] = invertX(tipBase, set4[finger,bone,tipBase,row])
                    X[row+8000,col] = set5[finger,bone,tipBase,row]
                    X[row+9000,col] = invertX(tipBase, set5[finger,bone,tipBase,row])
                    X[row+10000,col] = set6[finger,bone,tipBase,row]
                    X[row+11000,col] = invertX(tipBase, set6[finger,bone,tipBase,row])
                    X[row+12000,col] = set7[finger,bone,tipBase,row]
                    X[row+13000,col] = invertX(tipBase, set7[finger,bone,tipBase,row])
                    X[row+14000,col] = set8[finger,bone,tipBase,row]
                    X[row+15000,col] = invertX(tipBase, set8[finger,bone,tipBase,row])
                    X[row+16000,col] = set9[finger,bone,tipBase,row]
                    X[row+17000,col] = invertX(tipBase, set9[finger,bone,tipBase,row])
                    X[row+18000,col] = set10[finger,bone,tipBase,row]
                    X[row+19000,col] = invertX(tipBase, set10[finger,bone,tipBase,row])
                    col = col + 1
    return X, Y

def invertX(tipBase, set):
    #print(set)
    if (tipBase == 0):
        set = 0 - set
    #print("change: ", set)
    return set

def CenterData(X):
    allXCoordinates = X[:,:,0,:]
    meanValue = allXCoordinates.mean()
    X[:,:,0,:] = allXCoordinates - meanValue
    allXCoordinates = X[:,:,1,:]
    meanValue = allXCoordinates.mean()
    X[:,:,1,:] = allXCoordinates - meanValue
    allXCoordinates = X[:,:,2,:]
    meanValue = allXCoordinates.mean()
    X[:,:,2,:] = allXCoordinates - meanValue
    #exit()
    return X

train0 = ReduceData(train0)
test0 = ReduceData(test0)
train1 = ReduceData(train1)
train2 = ReduceData(train2)
test1 = ReduceData(test1)
test2 = ReduceData(test2)
train3 = ReduceData(train3)
train4 = ReduceData(train4)
test3 = ReduceData(test3)
test4 = ReduceData(test4)
train5 = ReduceData(train5)
train6 = ReduceData(train6)
test5 = ReduceData(test5)
test6 = ReduceData(test6)
train7 = ReduceData(train7)
train8 = ReduceData(train8)
test7 = ReduceData(test7)
test8 = ReduceData(test8)
train9 = ReduceData(train9)
test9 = ReduceData(test9)


train0 = CenterData(train0)
test0 = CenterData(test0)
train1 = CenterData(train1)
train2 = CenterData(train2)
test1 = CenterData(test1)
test2 = CenterData(test2)
train3 = CenterData(train3)
train4 = CenterData(train4)
test3 = CenterData(test3)
test4 = CenterData(test4)
train5 = CenterData(train5)
train6 = CenterData(train6)
test5 = CenterData(test5)
test6 = CenterData(test6)
train7 = CenterData(train7)
train8 = CenterData(train8)
test7 = CenterData(test7)
test8 = CenterData(test8)
train9 = CenterData(train9)
test9 = CenterData(test9)

trainX, trainY = ReshapeData(train0, train1, train2, train3, train4, train5, train6, train7, train8, train9)
testX, testY = ReshapeData(test0, test1, test2, test3, test4, test5, test6, test7, test8, test9)
#print(trainX)
#print(trainY)
#print(trainX.shape)
#print(trainY.shape)
#print(testX)
#print(testY)
#print(testX.shape)
#print(testY.shape)

knn.Use_K_Of(50)
knn.Fit(trainX,trainY)

wrongPrediction = 0
for row in range(0,1000):
    prediction = knn.Predict(testX[row])
    actual = testY[row]
    if (prediction != actual):
        wrongPrediction = wrongPrediction + 1
        print(str(actual) + " " + str(prediction))
    
print("Wrong Predictions: ", wrongPrediction)

pickle.dump(knn, open('userData/classifier.p', 'wb'))

    
#[numItemsTrain, numFeatures] = knn.data.shape