
# coding: utf-8

# In[1]:

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib')

# Make sure the encoding is utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Will be used to address character encoding later due to French names
from pandas.compat import u


# In[2]:

get_ipython().magic(u'pdb off')


# **Source: **[In-, out- and net-migration estimates, by geographic regions of origin and destination, *Terminated*](http://www5.statcan.gc.ca/cansim/a26?lang=eng&retrLang=eng&id=1110030&paSer=&pattern=&stByVal=1&p1=1&p2=-1&tabMode=dataTable&csid=)

# In[3]:

flowData = pd.read_csv('../TableD_01110030-eng.csv')
flowData.head()


# In[4]:

# Convert place names to unicode
flowData['GEO'] = flowData['GEO'].map(u)
flowData['GEODEST'] = flowData['GEODEST'].map(u)
flowData.head()


# In[5]:

# Remove unneeded columns
dropCols = ['Geographical classification',
           'Geographical classification.1',
           'Coordinate',
           'Vector']
flowData = flowData.drop(dropCols, axis=1)
flowData.head(10)


# In[6]:

# Rename columns
flowData = flowData.rename(columns={"GEO": "Origin", "GEODEST": "Destination"})


# In[7]:

# Filter for only the most recent data
flowData2011 = flowData[flowData['Ref_Date'] == 2011].drop('Ref_Date', axis=1).reset_index(drop=True)
flowData2011.head()


# In[8]:

# Convert that Value column to a numeric data type
flowData2011['Value'] = flowData2011['Value'].convert_objects(convert_numeric=True)


# In[9]:

# Remove all the non-census areas so we can geocode the cities that qualify as CMAs
flowData2011_cma = flowData2011[~flowData2011['Destination'].str.contains('Non-census')]
flowData2011_cma = flowData2011_cma[~flowData2011_cma['Origin'].str.contains('Non-census')]
flowData2011_cma.head()


# In[10]:

outMig = flowData2011_cma[flowData2011_cma['MIGMOVE'] == "Out-migration"].drop('MIGMOVE', axis=1).reset_index(drop=True)
outMig.head()


# In[11]:

outMigPiv = outMig.pivot('Origin', 'Destination', 'Value')
outMigPiv.head()


# In[12]:

# Since there is such a range in values, let's put this on a log scale
log_scale = lambda x: np.log10(x)
outMigPivLog = outMigPiv.applymap(log_scale).replace([np.inf, -np.inf], 0)


# In[13]:

sns.heatmap(outMigPivLog)


# In[ ]:

sns.clustermap(outMigPivLog)


# In[ ]:



