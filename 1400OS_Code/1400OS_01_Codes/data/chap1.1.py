import scipy as sp 
import matplotlib.pyplot as plt

def error(f,x,y) :
    return sp.sum((f(x)-y)**2)


data = sp.genfromtxt("web_traffic.tsv",delimiter = "\t")
x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
plt.scatter(x,y)
plt.title("Web traffic data")
plt.xlabel("Time")
plt.ylabel("Hits/Hr")
plt.xticks([w*7*24 for w in range(10)] , [ 'week %i ' %w for w in range(10)])
plt.autoscale(tight=True)


fp1 , residuals , rank , sv , rcond = sp.polyfit(x,y,1,full=True)
print("Model parameters : %s" %fp1)
fp2 = sp.polyfit(x,y,2)

f1 = sp.poly1d(fp1)
print(error(f1,x,y))
f2 = sp.poly1d(fp2)

fx = sp.linspace(0,x[-1],1000)
plt.plot (fx , f2(fx) , linewidth = 4)
plt.legend(["d = %i" % f2.order] , loc = "upper left")

plt.grid()
plt.show()
#print (data[:10])
#print(data.shape)