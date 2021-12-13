

import os
import sys
import pandas as pd
from googleapiclient.discovery import build
from pprint import pprint



api="AIzaSyBXYw_iE-GAobVn1L83BiyBg7KioYnk8wY"
cid="21uh28Z77Xg,PvYhZT99g1s"
y=build('youtube','v3',developerKey=api)




def extract(a):
    """this function is used to extract the data such as video Id, Title, Date of Publish, View, Likes and Dislikes
       Required parameter : pass a single string value containing all video id (for ex. "id1,id2,..")
       Returns: tuple containing lists of above data
    """
    vid=[]
    title=[]
    dop=[]
    vc=[]
    l=[]
    
    try:
        st1=y.videos().list(part="snippet,statistics,contentDetails",id=a).execute()
    except Exception : 
        return "API not connected to server. Please check internet connectivity"
    for i in range(0,len(st1['items'])):
        vid.append(st1['items'][i]['id'])
        title.append(st1['items'][i]['snippet']['title'])
        dop.append(st1['items'][i]['snippet']['publishedAt'].split('T')[0])
        vc.append(st1['items'][i]['statistics']['viewCount'])
        l.append(st1['items'][i]['statistics']['likeCount'])
        
    return vid,title,dop,vc,l




def tocsv(a,name):
    head=['Video_id','Title','Date_of_publishment','views_count','likes']
    try:
        b=extract(a)
    except Exception:
        return "API not connected to server. Please check internet connectivity"
    if os.path.isfile('{}.csv'.format(name)):
        df=pd.read_csv('{}.csv'.format(name),index_col=[0])
        mm=dict(zip(head,b))
        m1=pd.DataFrame(mm)
        df=pd.concat([df,m1],ignore_index=True)
        df.to_csv('{}.csv'.format(name))
        return "data added successfully"
    else:
        try:
            mm=dict(zip(head,b))
        except (ValueError,Exception):
            return "data not found from video"
        m1=pd.DataFrame(mm,index=None)
        m1.to_csv('{}.csv'.format(name))
        return "csv successfully created"
        
            
            


# In[67]:


##g=['a','b','c']
##u=[1,2,3]
##
##j=dict(zip(g,u))
##
##
### In[69]:
##
##
##pd.DataFrame([j])
##
##
### In[79]:
##
##
##head=['Video_id','Title','Date_of_publishment','views_count','likes']
##
##
### In[81]:


##jn=dict(zip(head,b))
##
##
### In[82]:
##
##
##pd.DataFrame(jn)
##
##
### In[ ]:
##
##
##
##
