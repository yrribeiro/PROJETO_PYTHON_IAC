import pandas as pd
import matplotlib.pyplot as plt
plt.title("Medição da energia gasta no Instituto de Computação")
mtr = pd.read_csv("energia.csv")
anos = mtr[0:10]
x = anos["Ano"]
y = anos["Energia"]
plt.subplots_adjust(bottom=0.15)
plt.xlabel("ANO")
plt.ylabel("RESULTADO")
plt.grid(True)
plt.plot(x, y)
plt.xticks(x, x, rotation='vertical')
plt.show()
