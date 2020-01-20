import pandas as pd
import matplotlib.pyplot as plt
mtr = pd.read_csv("energia.csv")
mtr.boxplot()
plt.show()