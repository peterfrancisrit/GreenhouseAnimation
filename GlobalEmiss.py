# Global emissions animation

# import packages
import pandas as pd
import numpy as np

# read the data
data = pd.read_csv('emission data.csv',index_col=0)
data = data.T


# Remove world
data = data.drop(['World','EU-28'],axis=1)


# normalize
from sklearn.preprocessing import normalize
data = pd.DataFrame(normalize(data),columns=data.columns,index=data.index)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Harry Ritchie'), bitrate=1000)

def update_bar(num, data):
	plt.cla()
	plt.bar(data.columns,data.iloc[num,:])
	plt.title("Year {}".format(data.index[num]))
	plt.xticks(rotation=90,fontsize=5)
	plt.ylim([0,1.5])
	ax = plt.axes()
	ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
	for i,j in enumerate(data.iloc[num,:]):
		if j > 0:
			plt.annotate(data.columns[i],xy=(data.columns[i],j))

fig,_ = plt.subplots(figsize=(15,8))
hist = plt.bar(data.columns,data.iloc[0,:])
plt.title("Year {}".format(data.index[0]))
plt.xticks(rotation=90,fontsize=5)
plt.ylim([0,1])
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))


animation_ = animation.FuncAnimation(fig, update_bar, len(data),fargs=(data, ))

animation_.save('emission.mp4', writer=writer)
print("COMPLETE")