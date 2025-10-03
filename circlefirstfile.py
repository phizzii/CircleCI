# importing relevant modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

integration_dataset_df = pd.read_csv("continuous_integration_data_pipeline_dataset.csv")

fig, axes = plt.subplots(figsize=(12,8))
plt.scatter(integration_dataset_df['X'],integration_dataset_df['Y'], s=100)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.tight_layout()
plt.show()