import requests
import pickle
from bs4 import BeautifulSoup
import json
import os
import tqdm
import urllib3
urllib3.disable_warnings()

import requests

# PASTE YOUR COOKIES AND HEADER AFTER LOGGING IN
cookies = {
    '_ga': 'GA1.3.794809885.1597750562',
    'csrftoken': 'FkifHVf0m8O4Cz2VshHIwBnBpqs3h4T3AzaHP4PU9XwdBvRDUqGUz4AduYprC8ar',
    'sessionid': 'uornea2tf1gfqtae5o6yhus9764v9m77',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://shiksha.iiit.ac.in/asgn/app/ta/questions/list/29/',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8,pa;q=0.7',
}

headers1 = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://shiksha.iiit.ac.in/asgn/app/ta/answers/list/1545/',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8,pa;q=0.7',
}

response = requests.get('http://shiksha.iiit.ac.in/asgn/app/ta/answers/list/1545/', headers=headers, cookies=cookies, verify=False)

# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')

my = soup.findAll("a", {'class': 'button small'}) # list of all submission
a = my[-67:] ### Last 67 questions
# print(len(a))

# MAKE REQUIRED FOLDERS
os.makedirs('Q1', exist_ok=True)
os.makedirs('Q2', exist_ok=True)
os.makedirs('Q3', exist_ok=True)

dirs = ['Q1', 'Q2', 'Q3'] # folders for the questions
ext = ['pdf', 'ipynb', 'pdf'] # question extensions - pdf, ipynb, jpg, png etc.

for idx, i in tqdm.tqdm(enumerate(a), total=len(a)):
    val = i['href'].split('/')[-2]
    # print(idx, val)
    url = 'http://shiksha.iiit.ac.in/asgn/app/grade/view/{}/'.format(val)
    resp = requests.get(url, headers=headers1, cookies=cookies, verify=False)
    sp = BeautifulSoup(resp.text, 'lxml')
    s = sp.findAll("div", {"class": "small-8 medium-9 column"})
    # print(s[2])
    for j, ff in enumerate(s[2].findAll('li')):
    	q_no = ff.text.strip().split(" ")[1] ### Question number
    	file_url = ff.findAll('a')[0]['href']

	    r = requests.get('http://shiksha.iiit.ac.in' + file_url, stream = True)
	    #download started
	    with open('{}/{:03d}_{}.{}'.format(dirs[j], idx, val, ext[q_no]), 'wb') as f:
	        for chunk in r.iter_content(chunk_size = 1024*1024):
	            if chunk:
	                f.write(chunk)