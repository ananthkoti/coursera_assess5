import matplotlib.pyplot as plt
import numpy as np
x=np.array(["maggi","cacks","bread","kurkure"])
plt.xlabel("sales on Monday")
y=np.array([30,50,70,90])
plt.ylabel("salling item ratio")
plt.bar(x,y , color="r",width=0.4)
plt.title("Soap")
plt.show()