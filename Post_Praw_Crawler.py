import json
import pandas as pd
import numpy as np
import requests
import time
import datetime as dt
import gc

#do I want to update from a preexisting csv?
update = False
#Which subreddit?
subreddit = 'Bitcoin'

def epoch_to_date(epoch_time):
    return dt.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')

def date_to_epoch(df_date):
    pattern = '%Y-%m-%d %H:%M:%S'
    return int(time.mktime(time.strptime(df_date, pattern)))

def rq(moving_date):
    # generates a request asking: before 'moving_date'
    # if update. requests asks: before 'moving' and after 'last_date'
    if update==False:
        r = requests.get("https://api.pushshift.io/reddit/search/submission/"+
             "?subreddit={}&size=500&is_video=False&before={}".format(subreddit,moving_date))
    else:
        r =  requests.get("https://api.pushshift.io/reddit/search/submission/"+
             "?subreddit={}&size=500&is_video=False&before={}&after={}".format(subreddit,moving_date,last_date))
    return r


#here we import the previous dataset to know 'until when do we update', which is defined as 'last_date'
if update==True:
    #imports previous csv
    df_0 = pd.read_csv('./Data/Reddit_{}_PushShift.csv'.format(subreddit),index_col=0)    
    
    #last date = 48h (2 days) before time of last post
    last_date = date_to_epoch(df_0.date.max())-(86400 * 2)
    
    #remakes df, to allow 48 hours overlap 
    df_0 = df_0[df_0['date'] > epoch_to_date(last_date)]


init = True
df = pd.DataFrame()
moving_date = round(time.time())

#for testing
#moving_date = 1494113957 #may 5th
#moving_date = 1494200357 #may 7th


while (init or len(r.json()['data'])>0):
    init = False
    n_ls = []
    t0=time.time()
    
    print('Searching Dates before {}'.format(epoch_to_date(moving_date)))
    r = rq(moving_date)
    #requesting: pushshifts limit is 200r/min
     
    #time.sleep(1.5)
    #at 1.5 sec, we are under 100r/min
    
    if len(r.json()['data'])==0:
        print('fin') #end of datastream
        break

    for sub in r.json()['data']:
        n_dic = {}
        n_dic['date'] = epoch_to_date(sub['created_utc'])
        n_dic['author'] = sub['author']
        n_dic['comments'] = sub['num_comments']
        n_dic['score'] = sub['score']
        n_dic['title'] = sub['title']
        n_dic['url'] = sub['url']
        n_ls.append(n_dic)
    df = df.append(pd.DataFrame(n_ls))

    #moving search window
    moving_date = date_to_epoch(df.date.min())
    dur=round(time.time()-t0)
    print('Search took {} seconds\n'.format(dur))
    
    #shaves time if needed
    if dur > 1.5:
        time.sleep(1.5)

if update:
    df = df.append(df_0).sort_values('date',ascending=True)
df.to_csv('./Data/Reddit_{}_PushShift.csv'.format(subreddit))