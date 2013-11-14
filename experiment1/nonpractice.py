from __future__ import division
import pickle

with open('prediction.pickle', 'rb') as f:
    prediction = pickle.load(f)

with open('testingLabel.pickle', 'rb') as f:
    testingLabel = pickle.load(f)

print type(prediction)
print type(testingLabel)

count = 0
for i in range(len(prediction)):
    if prediction[i] != testingLabel[i]:
        count += 1

print count/len(prediction)

print 3//4



