import matplotlib.pyplot as plt
import numpy as np

times=['1','2','3','4','5','6','7','8']
cell1=[66.7, 73.3, 64.4, 44.4, 77.8, 77.8, 75.6, 88.9]
nucleus1=[26.7, 22.2, 22.2, 15.6, 22.2, 33.3, 26.7, 28.9]
index=np.arange(len(times))

bar_width=0.2
alpha=0.5

abc1=plt.bar(index-bar_width/2,cell1,width=bar_width,color='r',alpha=0.5,label='cell')
abc2=plt.bar(index+bar_width/2,nucleus1,width=bar_width,color='c',alpha=0.5,label='nucleus')

plt.xticks(index,times)
plt.title('cell imaging')
plt.ylabel('diameter (um)')
plt.xlabel('cell number')
plt.ylim([15,90])
plt.legend()
plt.grid(True, axis='y',linestyle='--')
plt.show()

rate=[26.7/66.7, 22.2/73.3, 22.2/64.4, 15.6/44.4, 22.2/77.8, 33.3/77.8, 26.7/75.6, 28.9/88.9]
bar_width=0.2
alpha=0.5

abc1=plt.bar(index,rate,width=bar_width,color='g',alpha=0.5,label='ratio')

plt.xticks(index,times)
plt.title('cell imaging')
plt.ylabel('nucleus/cell')
plt.xlabel('cell number')
plt.legend()
plt.grid(True, axis='y',linestyle='--')
plt.show()
