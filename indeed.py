#!/usr/bin/env python
# coding: utf-8

# In[84]:


driver  = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.naukri.com/data-scientist-jobs?k=data%20scientist')


# In[88]:


import pandas as pd


# In[85]:


jobs = driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')#elements for post name
company = driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')#elements for company name


# In[86]:


title = []
for i in range(len(jobs)):
    title.append(jobs[i].text)


# In[89]:


data = pd.DataFrame(title)


# In[90]:


company_ = []
for i in range(len(company)):
    company_.append(company[i].text)


# In[91]:


data['company'] = company_


# In[92]:


data.to_csv('Job List.csv',index=False)
data

driver.close()


# In[ ]:




