{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import time\n",
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "#do I want to update from a preexisting csv?\n",
    "update = True\n",
    "#Which subreddit?\n",
    "subreddit = 'Bitcoin'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
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
    "             \"?subreddit={}&size=500&\"+\n",
    "             \"is_video=False&\"\n",
    "             \"before={}\".format(subreddit,moving_date))\n",
    "    else:\n",
    "        r =  requests.get(\"https://api.pushshift.io/reddit/search/submission/\"+\n",
    "             \"?subreddit={}&size=500&\"+\n",
    "             \"is_video=False&\"\n",
    "             \"before={}&after={}\".format(subreddit,moving_date,last_date))\n",
    "    return r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "if update==True:\n",
    "    #imports previous csv\n",
    "    df_0 = pd.read_csv('./Data/Reddit_{}_PushShift.csv'.format(subreddit),index_col=0)    \n",
    "    #finds 24h before most recent value\n",
    "    last_date = date_to_epoch(df_0.date.max())-86400 \n",
    "    #reassigns df to df before 24h before last update\n",
    "    #as to assume there may have been changes to 24h posts\n",
    "    df_0 = df_0[df_0['date'] > epoch_to_date(last_date)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "moving_date 2018-08-24 16:45:22\n",
      "last_date 2018-08-18 14:35:45\n",
      "500\n",
      "\n",
      "moving_date 2018-08-18 14:36:24\n",
      "last_date 2018-08-18 14:35:45\n",
      "500\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Starts as 'now', but moves with iteration\n",
    "moving_date = round(time.time())\n",
    "init = True\n",
    "n_ls = []\n",
    "df = pd.DataFrame()\n",
    "\n",
    "while (init or len(r.json()['data'])>0):\n",
    "    init = False\n",
    "    print('Searching Dates before {}'.format(epoch_to_date(moving_date)))\n",
    "    print(len(r.json()['data']))\n",
    "    print()\n",
    "    \n",
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
    "    moving_date = date_to_epoch(df.date.min())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "if update:\n",
    "    df = df.append(df_0).sort_values('date',ascending=True)\n",
    "df.to_csv('./Data/Reddit_{}_PushShift.csv'.format(subreddit))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [default]",
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
