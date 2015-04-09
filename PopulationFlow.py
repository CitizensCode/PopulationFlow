
# coding: utf-8

# In[5]:

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# In[6]:

get_ipython().magic(u'pdb off')


# **Source: **[In-, out- and net-migration estimates, by geographic regions of origin and destination, *Terminated*](http://www5.statcan.gc.ca/cansim/a26?lang=eng&retrLang=eng&id=1110030&paSer=&pattern=&stByVal=1&p1=1&p2=-1&tabMode=dataTable&csid=)

# In[7]:

flowData = pd.read_csv('../TableD_01110030-eng.csv')
flowData.head()


# In[8]:

dropCols = ['Geographical classification',
            'Geographical classification.1',
            'Coordinate']
flowData = flowData.drop(dropCols, axis=1)
flowData.head(10)


# In[9]:

# Filter for only the most recent data
flowData2011 = flowData[flowData['Ref_Date'] == 2011].drop('Ref_Date', axis=1).reset_index(drop=True)
flowData2011.head()


# In[10]:

flowData2011['Value'] = flowData2011['Value'].convert_objects(convert_numeric=True)


# In[11]:

flowData2011_cma = flowData2011[~flowData2011['GEODEST'].str.contains('Non-census')]
flowData2011_cma = flowData2011_cma[~flowData2011_cma['GEO'].str.contains('Non-census')]
flowData2011_cma


# In[ ]:



