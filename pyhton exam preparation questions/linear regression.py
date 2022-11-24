import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,33,45,66,87,45,34,23,98,99,65,67]

slope,intercept,r,p,std_err=stats.linregress(x,y)

def myfunc(x):
    return slope*x+intercept

mymodel = list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()

