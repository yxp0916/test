from matplotlib import pyplot

# pyplot.plot([5,6,7,8],[7,3,8,3],'r',linewidth=5,label='Line one')
# pyplot.plot([2,3,4,5],[3,4,5,6],'y',linewidth=3,label='Line two')

# pyplot.scatter([5,6,7,8], [7,3,8,3] ,color='b',label='Line One')
# pyplot.scatter([2,5,3,9], [5,3,2,7] ,color='r',label='Line Two')

pyplot.bar([2,4,6,8], [7,3,8,3] ,color='b',label='Line One')
pyplot.bar([1,3,5,7], [6,7,2,6] ,color='r',label='Line Two')

pyplot.title('title')
pyplot.ylabel('Y zhou')
pyplot.xlabel('X zhou')

pyplot.legend()

# pyplot.grid(True,color='k')

pyplot.show()