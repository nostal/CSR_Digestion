import pickle
import matplotlib.pyplot as plt

with open('scores.pickle', 'rb') as f:
    scores = pickle.load(f)

x = range(1,51)

plt.plot(x, scores)
plt.show()
