import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

times=['first','second','third']
control1=[1.362, 1.219, 1.171]
a=[1.861, 1.700, 1.691]
b=[1.690, 1.664, 1.601]
c=[1.641, 1.522, 1.466]
index=np.arange(len(times))

bar_width=0.2
alpha=0.5

abc1=plt.bar(index-bar_width,control1,width=bar_width,color='r',alpha=0.5,label='control')
abc2=plt.bar(index,a,width=bar_width,color='c',alpha=0.5,label='a')
abc3=plt.bar(index+bar_width,b,width=bar_width,color='b',alpha=0.5, label='b')
abc4=plt.bar(index+bar_width*2,c,width=bar_width,color='black',alpha=0.5,label='c')

#plt.figure(figsize=(10, 16))
#plt.plot(control1,a,b,c)
plt.xticks(index+bar_width,times)
plt.title('cytotoxicity test')
plt.ylabel('cell viability (%)')
plt.xlabel('times')
plt.ylim([1.10,1.900])
plt.legend()
plt.grid(True, axis='y',linestyle='--')
plt.show()

###
label=['control','100%','95%','90%','85%','80%','75%']
control2=[0.973, 0.820, 0.721]
d0=[1.320,1.179,1.146]
d1=[1.313,1.184,1.116]
d2=[1.267,1.113,1.019]
d3=[1.302,1.104,1.028]
d4=[1.167,0.993,0.942]
d5=[1.187,0.906,0.875]

first=[0.973,1.320,1.313,1.267,1.302,1.167,1.187]
second=[0.820,1.179,1.184,1.113,1.104,0.993,0.906]
third=[0.721,1.146,1.116,1.019,1.028,0.942,0.875]

plt.plot(label,first)
plt.plot(label,second)
plt.plot(label,third)
plt.title('serial dilution test')
plt.ylabel('cell viability (%)')
plt.xlabel('concentration')
plt.grid(True,linestyle='--')
plt.show()