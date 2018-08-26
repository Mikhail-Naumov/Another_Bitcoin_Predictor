{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import time\n",
    "import datetime as dt\n",
    "import gc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#do I want to update from a preexisting csv?\n",
    "update = False\n",
    "#Which subreddit?\n",
    "subreddit = 'Bitcoin'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def epoch_to_date(epoch_time):\n",
    "    return dt.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')\n",
    "\n",
    "def date_to_epoch(df_date):\n",
    "    pattern = '%Y-%m-%d %H:%M:%S'\n",
    "    return int(time.mktime(time.strptime(df_date, pattern)))\n",
    "\n",
    "def rq(moving_date):\n",
    "    #generates a request before 'moving_date'\n",
    "    #if update. requests before 'moving' and after 'last_date'\n",
    "    if update==False:\n",
    "        r = requests.get(\"https://api.pushshift.io/reddit/search/submission/\"+\n",
    "             \"?subreddit={}&size=500&is_video=False&before={}\".format(subreddit,moving_date))\n",
    "    else:\n",
    "        r =  requests.get(\"https://api.pushshift.io/reddit/search/submission/\"+\n",
    "             \"?subreddit={}&size=500&is_video=False&before={}&after={}\".format(subreddit,moving_date,last_date))\n",
    "    return r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "if update==True:\n",
    "    #imports previous csv\n",
    "    df_0 = pd.read_csv('./Data/Reddit_{}_PushShift.csv'.format(subreddit),index_col=0)    \n",
    "    #finds 24h before most recent value\n",
    "    last_date = date_to_epoch(df_0.date.max())-(86400 * 2)#how many days ago do we want to overwrite?\n",
    "    #reassigns df to df before 24h before last update\n",
    "    #as to assume there may have been changes to 24h posts\n",
    "    df_0 = df_0[df_0['date'] > epoch_to_date(last_date)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "moving_date = round(time.time())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searching Dates before 2017-05-03 02:30:55\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'n_dic' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-655c456256f5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     29\u001b[0m     \u001b[0mmoving_date\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdate_to_epoch\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdate\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     30\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 31\u001b[1;33m     \u001b[1;32mdel\u001b[0m \u001b[0mn_ls\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mn_dic\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     32\u001b[0m     \u001b[0mgc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcollect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     33\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'n_dic' is not defined"
     ]
    }
   ],
   "source": [
    "#Starts as 'now', but moves with iteration\n",
    "init = True\n",
    "#df = pd.DataFrame()\n",
    "\n",
    "while (init or len(r.json()['data'])>0):\n",
    "    init = False\n",
    "    n_ls = []\n",
    "    \n",
    "    print('Searching Dates before {}'.format(epoch_to_date(moving_date)))\n",
    "    t0=time.time()\n",
    "\n",
    "    r = rq(moving_date)\n",
    "    #pushshifts limit is 200r/min\n",
    "    # @ 1.5 sec, we are under 100r/min\n",
    "    time.sleep(1.5)\n",
    "\n",
    "    for sub in r.json()['data']:\n",
    "        n_dic = {}\n",
    "        n_dic['date'] = epoch_to_date(sub['created_utc'])\n",
    "        n_dic['author'] = sub['author']\n",
    "        n_dic['comments'] = sub['num_comments']\n",
    "        n_dic['score'] = sub['score']\n",
    "        n_dic['title'] = sub['title']\n",
    "        n_dic['url'] = sub['url']\n",
    "        n_ls.append(n_dic)\n",
    "    df = df.append(pd.DataFrame(n_ls))\n",
    "\n",
    "    #moving search window\n",
    "    moving_date = date_to_epoch(df.date.min())\n",
    "    \n",
    "    t1=time.time()\n",
    "    print('Search took {} seconds\\n'.format(round(t1-t0)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "if update:\n",
    "    df = df.append(df_0).sort_values('date',ascending=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#df.to_csv('./Data/Reddit_{}_PushShift.csv'.format(subreddit))\n",
    "df.to_csv('./Data/Reddit_PushShift.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
