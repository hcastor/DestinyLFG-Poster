import re
from robobrowser import RoboBrowser
from datetime import datetime, timedelta

browser = RoboBrowser(history=True)
browser.open("http://destinylfg.net")

addMyGroup = browser.select('#new')

form = browser.get_form(class_='form-horizontal panel-body')

form['region'].value  = 'northamerica'
form['platform'].value  = 'ps4'
form['gamertag'].value  = 'YOUR USERNAME'
form['level'].value  = 31
form['event'].value  = 'strikes-nightfall-weekly'
form['notes'].value  ='#lfm 30+ add USERNAME will not reply on here.'

startTime = datetime.now()
endTime = datetime.now()

browser.submit_form(form)
print 'post'

while(1):
  if(endTime - startTime > timedelta(seconds=30)):
    print 'post'
    startTime = datetime.now()
    endTime = datetime.now()
    browser.submit_form(form)
    wait = False
  else:
    endTime = datetime.now()