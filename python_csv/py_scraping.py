#!/usr/bin/env python
# coding: utf-8

# In[98]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://en.wikipedia.org/wiki/Comma-separated_values"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
soup


# In[56]:


results = soup.find('table', {'class':'wikitable'})
results.find_all()


# In[100]:


col_names = []
for i in results.find_all('th'):
    col_names.append(i.contents[0].strip())
rows = []
for i in results.find_all('tr'):
    row = []
    for j in i.find_all('td'):
        if len(j.contents) == 0:
            row.append(' ')
        else: 
            a = j.contents[0]
            row.append(a.strip())
        print(row)
    rows.append(row)
    
rows = rows[1:]
df = pd.DataFrame(rows, columns = col_names)
df


# In[103]:


df.to_csv('/Users/julia/st2195_assignment_2/python_csv/python_code.csv')


# In[ ]:




