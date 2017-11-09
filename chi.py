import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


figuur = plt.figure()
ax1 = figuur.add_subplot(2,1,2)


def animatie(i):
    test_bestand = open('sample.file.txt', 'r').read() #lees en opent bestand txt bestand
    lines = test_bestand.split('\n')
    xas = []
    yas = []
    for line in lines:
        if len (line) > 1: #trim away
            x, y = line.split(',')
            xas.append(x)
            yas.append(y)			
    ax1.clear()		
    ax1.plot(xas, yas)
	
	
ani = animation.FuncAnimation(figuur, animatie, interval=1000)
plt.show()
