
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("A:\TERM 4\CAB214\CA2\house_data.csv")

sns.heatmap(df.corr(), annot=True)
plt.show()