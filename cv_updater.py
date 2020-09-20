#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium                                                                 
from time import sleep                                                          
                                                                                
from contextlib import closing                                                  
from selenium.webdriver import Firefox # pip install selenium                   
from selenium.webdriver.support.ui import WebDriverWait                         
from selenium.webdriver.common.keys import Keys                                 
from selenium.webdriver import ActionChains                                     
from selenium.common.exceptions import NoSuchElementException                   
from selenium.webdriver.support import expected_conditions as EC                
from selenium.webdriver.common.by import By                                     
from selenium.common.exceptions import TimeoutException                         
import pause
import datetime
import time                                                        


# In[2]:


# use firefox to get page with javascript generated content                     
#https://thequestion.ru/account/256980/konstantin-lyaifer                       
# print('Hello, please wait...')                                                  
# browser = selenium.webdriver.Firefox(executable_path='/home/maksimka/web/geckodriver')
# user_agent = 'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'


# browser.set_preference("general.useragent.override", user_agent)
from selenium import webdriver
                                    
profile = webdriver.FirefoxProfile()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'


profile.set_preference("general.useragent.override", user_agent)
browser = webdriver.Firefox(profile,executable_path='/home/maksimka/web/geckodriver')
browser.get('https://hh.ru/applicant/resumes?from=header_new')                                               
print('Now authorisate')                                                        
print('Ready?<y/n>')                                                            
while input() != 'y':               
    print('<y/n>')


# In[21]:


answers = browser.find_elements_by_class_name('applicant-resumes-action')
button = answers[1]
print(len(answers))


# In[25]:


def update_resume():
    try:
        browser.refresh();
        answers = browser.find_elements_by_class_name('applicant-resumes-action')
        button = answers[1]
        answers = browser.find_elements_by_class_name('applicant-resumes-action')
        button_prop = answers[1].find_element_by_tag_name('div').find_element_by_tag_name('span').find_element_by_tag_name('button')
    except NoSuchElementException:
         try:
            button_prop = answers[1].find_element_by_tag_name('span').find_element_by_tag_name('button')
            button.click()
            return datetime.datetime.today()
         except :
            return 0
    return 0


# In[26]:


def alarm():
    #while True:
    for i in range(10):
        time.sleep(1)
        get_ipython().system('paplay --volume=20000 /home/maksimka/Music/beep_sounds/beep-02.wav')


# In[ ]:





# In[ ]:


t = datetime.datetime.today()
start = datetime.datetime(t.year,t.month,t.day,10,0)
if t.hour > 10:
    start = t
pause.until(start)
while True:
    res = update_resume()
    if res != 0:
        print('Updated ', res)
        start = res + datetime.timedelta(hours=4,minutes=2)
        if start > datetime.datetime(t.year,t.month,t.day,23,55): 
            start = datetime.datetime(t.year,t.month,t.day,10,0) + datetime.timedelta(days=1)
        print('pause until ', start)
        pause.until(start)
    else:
        print('Error ', datetime.datetime.today(), 'sleep 30 min')
        time.sleep(30*60)


