# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:58:34 2022

@author: JD

using data from :
    https://drive.google.com/file/d/1er9NJTLUA3qnRuyhfzuN0XUsoIC4a-_q/view
    https://www.kaggle.com/datasets/ruchi798/source-based-news-classification


if you want to compile yourself, download the data from those two websites and put
them into a csvs folder in the same directory as this file. This program cleans
the data a little bit, dropping any rows that are formatted very strangely or 
have nan values
"""


import pandas as pd

df = pd.read_csv('data/raw/news.csv',low_memory=False)

df2 = df.iloc[:, :4].dropna() # drop any na values

df2 = df2[(df2['ids'].apply(lambda x: True if x.isnumeric()  else False))] # drop any rows that dont have numbers as ids
df2['ids'] = df2['ids'].apply(lambda x: int(x)) # make all the ids into ints instead of strings
df2 = df2.loc[df2['text'] != '0'] # drop a really strange row with no text and no label

ids = set(df2['ids']) # make an ids set so we dont have duplicate ids

#%%
import pandas as pd

df3 = pd.read_csv('data/raw/news_articles.csv')
df4 = df3[['title', 'text', 'label']]

df4 = df4[df4['title'].apply(lambda x: False if x == 'no title' else True)] # drop any rows taht dont have any title

iter_id=1
newids = []
while(True):
    if(iter_id not in ids):
        newids.append(iter_id)
        iter_id = iter_id+1
    else:
        iter_id = iter_id+1
    if(len(newids) == 2096):
        break;
"end while"

idcol = pd.DataFrame(newids, columns = ['ids'])

df4['ids'] = idcol
df4 = df4.dropna()

combined_data = pd.concat([df2,df4])
combined_data['label'] = combined_data['label'].apply(lambda x: x.upper())

combined_data.to_csv(r'data/input/combinedData.csv', index = False)

    
