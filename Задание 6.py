import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, jo = plt.subplots()
x = np.linspace(0, 2 * np.pi,100)
line, = jo.plot(x,np.sin(x))
def update(frame):
  line.set_ydata(np.sin(x + frame/10))
  return line,

an = FuncAnimation(
    fig=fig,
    func=update,
    frames=30,
    interval=30,
    blit=True
)
plt.title('Анимация')
plt.show()