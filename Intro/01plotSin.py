import numpy as np
import matplotlib.pyplot as plt
# data
x=np.arange(0,6,0.1)
y1=np.sin(x)
y2=np.cos(x)
# Drawing Graph
plt.plot(x,y1, label="sin")
plt.plot(x,y2, linestyle="--", label="cos") # plot dash line
plt.xlabel("x") # x label
plt.ylabel("y") # y label
plt.title('sin & cos' )# title
plt.legend()
plt.show()
