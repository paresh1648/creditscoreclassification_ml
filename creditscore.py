# import numpy as np
import pandas as pd
import plotly.express as px

df=pd.read_csv("train.csv")
df["Credit_Score"].value_counts()
print(df.isnull().sum())
#vv-----Here No NULL Value has been found in this dataset, So we can proceed easily here-------vv
fig = px.box(df, 
             x="Occupation",  
             color="Credit_Score", 
             title="Credit Scores Based on Occupation", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
# print(fig.show())