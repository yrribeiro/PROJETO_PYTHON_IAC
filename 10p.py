import pandas as pd
import matplotlib.pyplot as plt
mtr = pd.read_csv("energia.csv")
anos = mtr[0:10]
x = anos["Ano"]
y = anos["Energia"]
done = plt.plot(x, y)
plt.show(done)

