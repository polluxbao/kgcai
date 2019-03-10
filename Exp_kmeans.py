from KGCkMeans import *
import matplotlib.pyplot as plt
from numpy import *

ind = [[1.0, 1.0],
       [1.5, 2.0],
       [3.0, 4.0],
       [5.0, 7.0],
       [3.5, 5.0],
       [4.5, 5.0],
       [3.5, 4.5]]

n = len(ind)

print('Individual  Variable1  Variable2')
for i in range(n):
    print('    %d         %0.1f        %0.1f' % (i + 1, ind[i][0], ind[i][1]))

k = 0
while k < 2 or k >= n:
    k = eval(input('Input k (2~%d): ' % n))
print('k = ', k)

x_org, y_org = [], []
for i in range(n):
    x_org.append(ind[i][0])
    y_org.append(ind[i][1])

plt.scatter(x_org, y_org)
plt.show()

input('Press ENTER to show result of Euclidean Distance Method...')

print('\n\n')
print('Euclidean Distance Method :')
print('=' * 20)
myCentroids, clustAssing = kMeans(mat(ind), k, distEclud, firstCent)

print('\nmyCentroids:\n', myCentroids)
print(myCentroids[:, 0])
print(myCentroids[:, 1])

print('\nclustAssing:\n', clustAssing)


xx=myCentroids[:, 0].tolist()
yy=myCentroids[:, 1].tolist()
x=list(eval(str(xx).replace('[','').replace(']','')))
y=list(eval(str(yy).replace('[','').replace(']','')))
print('x=',x)
print('y=',y)
plt.scatter(x_org, y_org)
plt.scatter(x, y,s=None,c='r')
plt.show()
input('Press ENTER to show result of Manhattan Distance Method...')

print('\n\n')
print('Manhattan Distance Method :')
print('=' * 20)
myCentroids, clustAssing = kMeans(mat(ind), k, distManh, randCent)

print('\nmyCentroids:\n', myCentroids)
print('\nclustAssing:\n', clustAssing)

xx=myCentroids[:, 0].tolist()
yy=myCentroids[:, 1].tolist()
x=list(eval(str(xx).replace('[','').replace(']','')))
y=list(eval(str(yy).replace('[','').replace(']','')))
print('x=',x)
print('y=',y)
plt.scatter(x_org, y_org)
plt.scatter(x, y,s=None,c='r')
plt.show()
