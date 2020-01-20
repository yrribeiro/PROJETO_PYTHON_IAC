import pandas as pd
import matplotlib.pyplot as plt
mtr = pd.read_csv("energia.csv")
x = mtr["Ano"]
y = mtr["Energia"]
done = plt.plot(x, y)
plt.show(done)
