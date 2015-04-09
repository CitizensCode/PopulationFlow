
# coding: utf-8

# In[21]:

import pandas as pd
from pandas import DataFrame, Series
import numpy as np

# Make sure the encoding is utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# In[22]:

get_ipython().magic(u'pdb off')


# **Source: **[In-, out- and net-migration estimates, by geographic regions of origin and destination, *Terminated*](http://www5.statcan.gc.ca/cansim/a26?lang=eng&retrLang=eng&id=1110030&paSer=&pattern=&stByVal=1&p1=1&p2=-1&tabMode=dataTable&csid=)

# In[23]:

flowData = pd.read_csv('../TableD_01110030-eng.csv')
flowData.head()


# In[24]:

# Remove unneeded columns
dropCols = ['Geographical classification',
           'Geographical classification.1',
           'Coordinate',
           'Vector']
flowData = flowData.drop(dropCols, axis=1)
flowData.head(10)


# In[25]:

# Filter for only the most recent data
flowData2011 = flowData[flowData['Ref_Date'] == 2011].drop('Ref_Date', axis=1).reset_index(drop=True)
flowData2011.head()


# In[26]:

# Convert that Value column to a numeric data type
flowData2011['Value'] = flowData2011['Value'].convert_objects(convert_numeric=True)


# In[27]:

# Remove all the non-census areas as a first-pass
flowData2011_cma = flowData2011[~flowData2011['GEODEST'].str.contains('Non-census')]
flowData2011_cma = flowData2011_cma[~flowData2011_cma['GEO'].str.contains('Non-census')]
flowData2011_cma.head()


# In[28]:

inMig = flowData2011_cma[flowData2011_cma['MIGMOVE'] == "In-migration"].drop('MIGMOVE', axis=1).reset_index(drop=True)
inMig.head()


# In[30]:

outMig = flowData2011_cma[flowData2011_cma['MIGMOVE'] == "Out-migration"].drop('MIGMOVE', axis=1).reset_index(drop=True)
outMig.head()


# In[46]:

outMigPiv = outMig.pivot('GEO', 'GEODEST', 'Value')
outMigPiv.head()


# In[50]:

import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib')


# In[57]:

from pandas.compat import u
outMigPiv.index = outMigPiv.index.map(u)
outMigPiv.columns = outMigPiv.columns.map(u)
outMigPiv.head()


# In[ ]:



