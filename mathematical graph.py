from matplotlib import pyplot

x = [i for i in range(-500, 500)]
y = [i ** 2 for i in x]

pyplot.plot(x,y)
pyplot.show()