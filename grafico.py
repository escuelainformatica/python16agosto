import matplotlib.pyplot as plt
import numpy as np   # rapido
import pandas as pd  # potencia


plt.rcdefaults()

fig, ax = plt.subplots()   # figura, y el eje


people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim') # tupla ()

y_pos = np.arange(len(people))   # 0,1,2,3,4

performance = 3 + 10 * np.random.rand(len(people)) # numpy un ndarray (performance ndarray)




ax.barh(y_pos, performance) # creo una barra horizontal


ax.set_yticks(y_pos)
ax.set_yticklabels(people)
# ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('etiqueta y')
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()


# array= [1,2,3]      array*3 = [3,6,9]













