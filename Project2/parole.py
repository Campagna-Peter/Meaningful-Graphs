from matplotlib import scale
from seaborn.categorical import barplot
from seaborn.utils import ci
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
sns.set()

df = pd.read_csv("parole-dataset.csv")

index_values = df[(df['INTERVIEW DECISION'] == '*')].index
index_values2 = df[(df['INTERVIEW DECISION'] == '**********')].index

df.drop(index_values, inplace = True)
df.drop(index_values2, inplace = True)

df['INTERVIEW DECISION'] = df['INTERVIEW DECISION'].replace(['PAROLED', 'GRANTED', 'REINSTATE', 'OR EARLIER', 'OPEN DATE'],'GRANTED')
df['INTERVIEW DECISION'] = df['INTERVIEW DECISION'].replace(['RCND&HOLD;', 'RCND&RELSE;', 'NOT GRANTD', 'DENIED'],'NOT GRANTED')

grouped_data = df.groupby(['RACE / ETHNICITY','INTERVIEW DECISION'])

x = []
y = []

#Loop through the grouped data
#The key is the (race/ethnicity, interview decision) pair
#The item contains all rows that fall under that category.  We just want a count (specifically, the length of the list)
for key,item in grouped_data:
    x.append(str(key))
    y.append(len(item))

plt.barh(x, y)
plt.ylabel("Race & Decision Status")
plt.xlabel("Count")
plt.show()

grouped_data = df.groupby(['SEX','INTERVIEW DECISION'])

x = []
y = []

#Loop through the grouped data
#The key is the (sex, interview decision) pair
#The item contains all rows that fall under that category.  We just want a count (specifically, the length of the list)
for key,item in grouped_data:
    x.append(str(key))
    y.append(len(item))


plt.barh(x, y)
plt.ylabel("Sex & Decision Status")
plt.xlabel("Count")
plt.show()

grouped_data = df.groupby(['PAROLE BOARD INTERVIEW TYPE','INTERVIEW DECISION'])

x = []
y = []

#Loop through the grouped data
#The key is the (interview type, interview decision) pair
#The item contains all rows that fall under that category.  We just want a count (specifically, the length of the list)
for key,item in grouped_data:
    x.append(str(key))
    y.append(len(item))


plt.barh(x, y)
plt.ylabel("Interview Type & Decision Status")
plt.xlabel("Count")
plt.show()