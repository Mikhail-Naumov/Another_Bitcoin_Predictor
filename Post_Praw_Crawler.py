{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 37,
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
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "#do I want to update from a preexisting csv?\n",
    "update = False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "def epoch_to_date(epoch_time):\n",
    "    return dt.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')\n",
    "\n",
    "def date_to_epoch(df_date):\n",
    "    pattern = '%Y-%m-%d %H:%M:%S'\n",
    "    return int(time.mktime(time.strptime(df_date, pattern)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "if update==True:\n",
    "    #imports previous csv\n",
    "    df = pd.read_csv('./Data/Reddit_PushShift.csv',index_col=0)    \n",
    "    \n",
    "    #finds 24h before most recent value\n",
    "    ls_date = date_to_epoch(df.sort_values('date',ascending=False).iloc[0].date)-86400 \n",
    "    #reassigns df to df before 24h before last update\n",
    "    #as to assume there may have been changes to 24h posts\n",
    "    df = df[df['date'] > epoch_to_date(ls_date)]\n",
    "\n",
    "    #uses request to fine date before NOW and after (24h before)Last value\n",
    "    def rq(use):\n",
    "        return requests.get(\"https://api.pushshift.io/reddit/search/submission/\"+\n",
    "             \"?subreddit=Bitcoin&size=500&\"+\n",
    "             \"is_video=False&\"\n",
    "             \"before={}&after={}\".format(use,ls_date))\n",
    "    \n",
    "else:\n",
    "    df = pd.DataFrame()\n",
    "    def rq(use):\n",
    "        return requests.get(\"https://api.pushshift.io/reddit/search/submission/\"+\n",
    "             \"?subreddit=Bitcoin&size=500&\"+\n",
    "             \"is_video=False&\"\n",
    "             \"before={}\".format(use))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searching Dates before 2018-08-19 17:05:37\n",
      "Searching Dates before 2018-08-17 15:42:33\n"
     ]
    }
   ],
   "source": [
    "use = round(time.time())\n",
    "init = True\n",
    "n_ls = []\n",
    "\n",
    "while (init or len(r.json()['data'])>0):\n",
    "    init = False\n",
    "    print('Searching Dates before {}'.format(epoch_to_date(use)))\n",
    "    r = rq(use)\n",
    "    #pushshifts limit is 200r/min\n",
    "    # @ 1.5 sec, we are under 100r/min\n",
    "    time.sleep(1.5)\n",
    "\n",
    "    if (len(r.json()['data'])==0 or ls_date>use): break\n",
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
    "    df = df.append(pd.DataFrame(n_df))\n",
    "\n",
    "    use = date_to_epoch(n_ls[-1]['date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('./Data/Reddit_PushShift.csv')"
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
