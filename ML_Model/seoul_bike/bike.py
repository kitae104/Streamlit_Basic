import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/SeoulBikeData.csv', encoding='unicode_escape')
df.head()