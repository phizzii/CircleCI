# importing relevant modules
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

integration_dataset_df = pd.read_csv("continuous_integration_dataset.csv")

fig, axes = plt.subplots(figsize=(12,8))
plt.scatter(integration_dataset_df['X'],integration_dataset_df['Y'], s=100)
plt.plot(integration_dataset_df['X'], 1.7770*integration_dataset_df['X']+10.6138, linestyle=':', color='red')  #1.7770 × X + 10.6138
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.tight_layout()
plt.show()