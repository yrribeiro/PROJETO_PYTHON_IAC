import pandas as pd
import matplotlib.pyplot as plt
plt.title("USE OF RENEWABLE ENERGY THROUGH TIME")
mtr = pd.read_csv("energia.csv")
anos = mtr[0:30]
x = anos["Ano"]
y = anos["Energia"]
# plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("ANO")
plt.ylabel("ENERGIA")
plt.grid(True)
plt.plot(x, y)
plt.xticks(x, x, rotation='vertical')
plt.show()