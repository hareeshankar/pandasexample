import numpy as np
import pandas as pd

# Pandas uses something called a dataframe. It is a
# 2D data structure that can hold multiple data types.
# Columns have labels.

# Series are built on top of NumPy arrays.
# Create a series by first creating a list
list_1 = ['address a', 'address b', 'address c']
# I can define that I want the series indexes to be the
# provided labels
labels = ["Shriram", "Hari", "hemanth"]

ser_1 = pd.Series(data=list_1, index=labels)

print(ser_1["Shriram"])
