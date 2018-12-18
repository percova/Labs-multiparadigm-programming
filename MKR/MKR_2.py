#!/usr/bin/env python
# coding: utf-8

# In[169]:


import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt


# In[170]:


df = pd.read_excel("Series.xlsx")
 
df = df[14:]
df.columns = ['1','Percent','2']
df = df.drop('1',1)
df = df.drop('2',1)
df = df.reset_index()
df.Percent = pd.to_numeric(df['Percent'], errors='coerce')


# In[171]:


series = []
for i in range(1,df.shape[0]):
    series.append(df['Percent'][i]-df['Percent'][i-1])  
series = pd.Series(series)


# In[172]:


points = []

dict_len = int(len(series)/20.)

num = sts.kstest(np.array(series),'uniform',[series.min(),series.max()])[1]
begin = series.min()
end = series.max()
series = series.sort_values()

if num>0.5:
    points = [[]]
    base = int(series.shape[0]/dict_len)
    extra = series.shape[0]%dict_len
    curr = 0
    print(base,extra)
    for i in range(series.shape[0]):
        if curr<extra:
            if len(points[-1])<base+1:
                points[-1].append(series[i])
            else:
                points.append([])
                points[-1].append(series[i])
                curr+=1
        
        else:
            if len(points[-1])<base:
                points[-1].append(series[i])
            else:
                points.append([])
                points[-1].append(series[i])
                curr+=1
    points.insert(0,points[0][0])
    for i in range(1,len(points)+1):
        if i==len(points)-1:
            points[i] = points[i][-1]
        else:
            points[i] = (points[i][-1]+points[i+1][0])/2
    for i in range(dict_len):
        points[i] = ['chr(65+i)',points[i],points[i+1]]
else:
    points = []
    step = (end-begin)/float(dict_len)
    for i in range(dict_len):
        points.append([chr(65+i),begin+step*i,begin+step*(1+i)])
    


# In[173]:


print(points)


# In[163]:


new_series = []
for i in range(len(series)):
    for j in range(len(points)):
        if series[i]>=points[j][1] and series[i]<=points[j][2]:
            new_series.append(points[j][0])
            break
print(new_series)


# In[164]:


lists = []
for i in range(dict_len):
    lists.append(chr(65+i))
matrix = pd.DataFrame(columns = lists,index= lists,data=0,dtype=float)
for i in range(1,len(new_series)): 
    matrix[new_series[i]][new_series[i-1]]+=1
for i in range(matrix.shape[0]):
    sum_ =0 
    for j in range(matrix.shape[0]):
        sum_+=matrix[chr(65+j)][chr(65+i)]
    for j in range(matrix.shape[0]):
        matrix[chr(65+j)][chr(65+i)]=matrix[chr(65+j)][chr(65+i)]/float(sum_)
print(matrix)


# In[165]:


def forecast1(string):
    result = ''
    max_ = 0
    for i in range(matrix.shape[1]):
            if matrix[matrix.columns[i]][string]>max_:
                result = matrix.columns[i]
                max_= matrix[matrix.columns[i]][string]
    return result

print(forecast1(new_series[-9]),new_series[-8])
print(forecast1(new_series[-8]),new_series[-7])
print(forecast1(new_series[-7]),new_series[-6])
print(forecast1(new_series[-6]),new_series[-5])
print(forecast1(new_series[-5]),new_series[-4])
print(forecast1(new_series[-4]),new_series[-3])
print(forecast1(new_series[-3]),new_series[-2])
print(forecast1(new_series[-2]),new_series[-1])


# In[166]:


lists2 = []
for i in range(dict_len):
    for j in range(dict_len):
        lists2.append(str(chr(65+i))+str(chr(65+j)))
        
matrix = pd.DataFrame(columns = lists,index= lists2,data=0.,dtype=float)
for i in range(2,len(new_series)):
    matrix[new_series[i]][new_series[i-2]+new_series[i-1]]+=1

for i in range(matrix.shape[0]):
    sum_ =0. 
    for j in range(matrix.shape[1]):
        sum_+=matrix[matrix.columns[j]][matrix.index[i]]
    for j in range(matrix.shape[1]):
        matrix[matrix.columns[j]][matrix.index[i]]=matrix[matrix.columns[j]][matrix.index[i]]/float(sum_)
matrix=matrix.fillna(0)
print(matrix)


# In[167]:


print(forecast1(new_series[-10]+new_series[-9]),new_series[-8])
print(forecast1(new_series[-9]+new_series[-8]),new_series[-7])
print(forecast1(new_series[-8]+new_series[-7]),new_series[-6])
print(forecast1(new_series[-7]+new_series[-6]),new_series[-5])
print(forecast1(new_series[-6]+new_series[-5]),new_series[-4])
print(forecast1(new_series[-5]+new_series[-4]),new_series[-3])
print(forecast1(new_series[-4]+new_series[-3]),new_series[-2])
print(forecast1(new_series[-3]+new_series[-2]),new_series[-1])


# In[ ]:





# In[ ]:




