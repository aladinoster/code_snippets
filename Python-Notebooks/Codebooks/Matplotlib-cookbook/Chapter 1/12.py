import matplotlib.pyplot as plot

data = [5., 25., 50., 20.]

plot.barh(range(len(data)), data)
plot.show()
