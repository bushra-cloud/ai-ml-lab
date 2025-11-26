import numpy as np 
import pandas as pd 
Series_A=pd.Series([10,20,30,40,50])
Series_B=pd.Series([40,50,60,70,80,])
items_common=pd.Series(list(set(Series_A)^(set(Series_B))))
print("items commo to both Series A and B:\n",items_common.tolist())
print("sum of Series A:",Series_A.sum())
print("find mean of Series B:",Series_B.mean())
print("find mode of Series B:",Series_B.mode())
print("smallest element of Series A:",Series_A.max())