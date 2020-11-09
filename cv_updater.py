#!/usr/bin/env python
# coding: utf-8

# In[1]:


# %load sele.py
#!/usr/bin/env python

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
from selenium import webdriver
import threading


# In[2]:


profile = webdriver.FirefoxProfile()
user_agent = 'barebuh'


profile.set_preference("general.useragent.override", user_agent)
browser = webdriver.Firefox(profile,executable_path='/home/maksimka/web/geckodriver')
browser.get('https://hh.ru/applicant/resumes?from=header_new')                                               
print('Now authorisate')                                                        
print('Ready?<y/n>')                                                            
while input() != 'y':               
    print('<y/n>')



# In[3]:


answers = browser.find_elements_by_class_name('applicant-resumes-action')
button = answers[1]
print(len(answers))


# In[4]:




def update_resume():
    browser.refresh();
    answers = browser.find_elements_by_class_name('applicant-resumes-action')
    res = 0
    for button in answers:
        if len(button.find_elements_by_class_name('applicant-resumes-update-button_disabled')):
            continue
        try:
            button_prop = button.find_element_by_tag_name('span').find_element_by_tag_name('button')
            button.click()
            res = datetime.datetime.today()
            break
        except:
            pass
    return res

def alarm():
    for i in range(10):
        time.sleep(1)
        get_ipython().system('paplay --volume=20000 /home/maksimka/Music/beep_sounds/beep-02.wav')



# In[ ]:





# In[5]:


def parser():
    global need_to_update
    global should_sleep 
    while True:
        with update:
            update.wait_for(lambda : need_to_update)
        t = datetime.datetime.today()
        res = update_resume()
        if res != 0:
            print('Updated ', res)
            print('pause 1:20')
            with wake_up:
                i = wake_up.wait_for(lambda:not should_sleep, timeout = 4800+60) # ждем 4 часа / 3 ( 3 резюме)
                should_sleep = True
        else:
            print('Error ', datetime.datetime.today(), 'sleep 30 min')
            with wake_up:
                i = wake_up.wait_for(lambda:not should_sleep, timeout = 30*60)
                should_sleep = True


# In[6]:


def command_listener():
    while True:
        global need_to_update
        global should_sleep 
        s = input() 
        if s == 'upd':
            need_to_update = True
            with update:
                update.notifyAll()
        elif s == 'wait':
            need_to_update = False
        elif s == 'wake':
            with wake_up:
                should_sleep = False
                wake_up.notifyAll()
        else:
            print('Unknown command, try again')


# In[ ]:


import threading
need_to_update = False
should_sleep = True 
update = threading.Condition()
wake_up = threading.Condition()

listener = threading.Thread(target=command_listener)                                    
parser_th = threading.Thread(target=parser)                                    
listener.start()                                                                
parser_th.start() 
listener.join()
parser_th.join()


# In[ ]:





# In[ ]:




