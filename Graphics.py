import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data = 'Excel.xlsx'
df = pd.read_excel(data)

print(df.head())

campos = df[['Duración (ms)','Magnitud2 (p.u)']]
print(campos)
y = campos['Magnitud2 (p.u)']
x = campos['Duración (ms)']
#pd.core()
a= df.iloc[:,2]
b= []
"""for i in len(a):
    if a>0.4:
        t = a[i]
        b.append(t)
        len(b)
"""
df.query("'Magnitud2 (p.u)'>0.4")
#z = campos.plot.scatter(x='Duración (ms)', y='Magnitud2 (p.u)', color='k')
plt.plot(x,y,'ko')
plt.axhline(y=0.4,xmin=0, xmax=1, color='c')
plt.show()