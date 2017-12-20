import matplotlib;matplotlib.use('agg');from function import *;
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(versicolor_petal_length)
plt.show()
print(versicolor_petal_length)
matplotlib.pyplot.savefig('htmlapp/static/image/plot.svg')