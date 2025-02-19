import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# إنشاء بيانات عشوائية
x = np.linspace(0, 10, 100)
y = np.sin(x)

# رسم البيانات
plt.plot(x, y, label="Sin(x)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Graph of Sin(x)")
plt.legend()
plt.show()
