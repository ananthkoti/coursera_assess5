import numpy
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
y=[100,90,80,70,60,50,40,30,20,70,65,56,45,88]

mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
myline=numpy.linspace(1,22,100)

plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()