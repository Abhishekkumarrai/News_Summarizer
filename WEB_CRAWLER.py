
# coding: utf-8

# In[1]:


import requests
r=requests.get("https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html")


# In[4]:


print(r.text[0:1000])


# In[5]:


from bs4 import BeautifulSoup


# In[6]:


soup=BeautifulSoup(r.text,'html.parser')


# In[7]:


results=soup.find_all('span',attrs={'class':'short-desc'})


# In[8]:


len(results)


# In[9]:


results[0:4]


# In[10]:


first_res=results[0]
first_res


# In[11]:


first_res.find('strong')


# In[12]:


first_res.find('strong').text


# In[13]:


first_res.find('strong').text[0:-1]


# In[15]:


first_res.find('strong').text[0:-1] + ' 2017'


# In[16]:


first_res.contents


# In[17]:


first_res.contents[0]


# In[18]:


first_res.contents[1]


# In[19]:


first_res.contents[1][1:-2]


# In[20]:


first_res.contents[2]


# In[25]:


first_res.contents[2].text[1:-1]


# In[26]:


first_res.contents[2]


# In[27]:


first_res.find('a')['href']


# In[31]:


records=[]
for result in results:
    date=result.find('strong').text[0:-1] + ' 2017'
    lie=result.contents[1][1:-2]
    exp=result.contents[2].text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie,exp,url))


# In[32]:


len(records)


# In[33]:


records[0:5]


# In[35]:


import pandas as pd


# In[37]:


df=pd.DataFrame(records,columns=['date','lie','exp','url'])


# In[38]:


df


# In[39]:


df.to_csv('sample crawl data',index=False,encoding='utf-8')

