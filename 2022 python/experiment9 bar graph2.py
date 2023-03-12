import matplotlib.pyplot as plt
import numpy as np

times=['1','2','3','4','5','6']
cell1=[122.2, 77.8, 77.8, 53.3, 53.3, 77.8]
nucleus1=[28.9, 22.2, 24.4, 22.2, 15.6, 24.4]
index=np.arange(len(times))

bar_width=0.2
alpha=0.5

abc1=plt.bar(index-bar_width/2,cell1,width=bar_width,color='r',alpha=0.5,label='cell')
abc2=plt.bar(index+bar_width/2,nucleus1,width=bar_width,color='c',alpha=0.5,label='nucleus')

plt.xticks(index,times)
plt.title('cell imaging')
plt.ylabel('diameter (um)')
plt.xlabel('cell number')
plt.ylim([10,125])
plt.legend()
plt.grid(True, axis='y',linestyle='--')
plt.show()

rate=[28.9/122.2, 22.2/77.8, 24.4/77.8, 22.2/53.3, 15.6/53.3, 24.4/77.8]
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