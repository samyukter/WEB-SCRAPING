#!/usr/bin/env python
# coding: utf-8

# In[54]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import random


# In[55]:


url='https://www.sfu.ca/computing/people/faculty.html'
s=requests.get(url).text
sou=BeautifulSoup(s,'lxml')


# In[56]:


r=sou.find('div',class_='parsys_column cq-colctrl-lt0 people faculty-list')
rt=r.find_all('div',class_='half')
l=len(rt)
hu=pd.DataFrame()
for re in rt:
    tt=re.find('div',class_='text')
    thu=tt.h4.text.split(",")
    tp=tt.p.text[6:].split("\n")
    row={'Name':thu[0],'Designation':thu[1],'Areas of Interest':tp[0]}
    hu=hu.append(row, ignore_index='false',sort='none')
hu   
   


# In[57]:


ra=random.randint(1,49)
list_url=[]
for re in rt:
   tt=re.find('div',class_='text')
   url12=tt.find('a').get('href')
   list_url.append(url12);
uurlu=list_url[ra-1]   
if "http" in uurlu:
  turl=""+uurlu
else :
  turl="http://www.sfu.ca"+uurlu
print(turl)


# In[58]:


st=requests.get(turl).text
soupp=BeautifulSoup(st,'lxml')


# In[59]:


title=soupp.find('div',class_="title section").div.h1.text
designition=soupp.find('div',class_='parsys_column cq-colctrl-lt0-c0').div.div.p.text
resear=soupp.find('div',class_='parsys_column cq-colctrl-lt0-c1')
rere=resear.find_all('div',class_='text parbase section')
lost_l=[]
for tewe in rere:
    tyui=tewe.div
    for tag in tyui.find_all("li"):
     lost_l.append(tag.text)
print(lost_l)


# In[60]:


hu2=pd.DataFrame()
add_r={'Research Intersests':lost_l}
hu2=hu2.append(add_r, ignore_index='false',sort='none')
hu2

