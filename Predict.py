import matplotlib.pyplot as plt
import numpy as np

from knn import KNN

knn = KNN()

knn.Load_Dataset('iris.csv')
#print(knn.data[:,0:2])
#print(knn.target)

x = knn.data[:,0:1].flatten()
y = knn.data[:,1:2].flatten()

#trainXx = knn.data[::2,0:1].flatten()
#trainXy = knn.data[::2,1:2].flatten()
#0:2
trainX = knn.data[::2,1:3]
trainY = knn.target[::2]
#print(trainX[0])
#print(trainY)
#x = [0,1,2,3,4,5]
#y = [0,1,2,3,4,5]
#co = [0,0,0,1,1,1]
#print(x)
#0:2
testX = knn.data[1::2,1:3]
testY = knn.target[1::2]

#print(testX)
#print(testY)

knn.Use_K_Of(15)
knn.Fit(trainX,trainY)
[numItemsTrain, numFeatures] = knn.data.shape
#for i in range(0,numItems/2):
#    actualClass = testY[i]
#    prediction = knn.Predict(testX[i,0:2])
#    print(actualClass, prediction)

#plt.figure()
#plt.scatter(x,y,c=knn.target)
#plt.show()

colors = np.zeros((3,3),dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5,1,0.5]
colors[2,:] = [0.5,0.5,1]

plt.figure()
[numItems, numFeatures] = knn.data.shape
for i in range(0,numItems/2):
    itemClass = int(trainY[i])
    currColor = colors[itemClass,:]
    plt.scatter(trainX[i,0],trainX[i,1],facecolor=currColor,edgecolor='black',s=50,lw=2)
correctCount = 0
for i in range(0,numItemsTrain/2):
    itemClass = int(testY[i])
    currColor = colors[itemClass,:]
    prediction= int( knn.Predict( testX[i,:] ) )
    edgeColor = colors[prediction,:]
    if (itemClass == prediction):
        correctCount = correctCount + 1
    plt.scatter(testX[i,0],testX[i,1],facecolor=currColor,edgecolor=edgeColor,s=50,lw=2)
#print(correctCount)
acc = int((float(correctCount) / (numItemsTrain/2)) * 100)
print("accuracy: " + str(acc) + "%")
#plt.scatter(trainX[:,0:1].flatten(),trainX[:,1:2].flatten(),c=trainY)
#plt.scatter(testX[:,0:1].flatten(),testX[:,1:2].flatten(),c=testY)
plt.show()