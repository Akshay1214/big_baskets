#!/usr/bin/env python
# coding: utf-8

# In[159]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.bigbasket.com/pc/beauty-hygiene/health-medicine/ayurveda")
driver.maximize_window()
 


# In[160]:


#containers = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div')


# In[161]:


#len(containers)
#print(containers)


# In[162]:


pro_names = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[1]/a')

delivery = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[3]/span/div/p/span[2]')

try:
    pro_price = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[1]/h4/span[2]')
except:
    pro_price = "No Price"
    

dis_price = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[1]/h4/span[1]')

per_dis = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[2]/div[2]/div/div')

try:
    ratings = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[1]/div/span[1]/span/span[1]')
except:
    ratings = "No Ratings"


# In[163]:


names, deli, price, d_price, p_dis, rat = [],[],[],[],[], []

for i in range(len(pro_names)):
    names.append(pro_names[i].text)
    
for i in range(len(delivery)):
    deli.append(delivery[i].text)
    
for i in range(len(pro_price)):
    price.append(pro_price[i].text)

for i in range(len(dis_price)):
    d_price.append(dis_price[i].text)
    
for i in range(len(per_dis)):
    p_dis.append(per_dis[i].text)
    
for i in range(len(ratings)):
    rat.append(ratings[i].text)
    
    


# In[164]:


names


# In[165]:


deli


# In[166]:


price


# In[167]:


d_price


# In[168]:


p_dis


# In[169]:


rat


# In[ ]:


final


# In[178]:


data = {"Names_Of_Product":names, "Delivery_Till":deli, "Original_Price":price, "Discount_Price":d_price, "Discount_Percent":p_dis, "Ratings":rat}


# In[180]:


final_sheet = zip(names, deli, price, d_price, p_dis, rat)


# In[172]:


data = pd.DataFrame()
df = pd.DataFrame({ key:pd.Series(value) for key, value in data.items()})
df


# In[181]:


wb = openpyxl.Workbook()
sheet = wb.active
for i in list(final_sheet):
    sheet.append(i)
    wb.save("Test_Data.csv")


# In[ ]:





# In[ ]:





# In[ ]:




