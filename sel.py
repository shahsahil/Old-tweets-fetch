#Pre-requisites - selenium installed , correct location to webdriver 

path_to_driver = "C:\\Users\\Sahil\\Documents\\chromedriver"
start = datetime.date(2016,9,25) #start date
end = datetime.date(2016,9,28) #end date
query = 'trump'
toptweets=True
num =100 #approx number of tweets required per day


import os
import time
import codecs
import re
import datetime
from selenium import webdriver

def fetch(start,end,num,query, driver, file, toptweets):
	
	if(toptweets):
		url = 'https://twitter.com/search?q='+query+'%20since%3A'+start+'%20until%3A'+end+'&src=typd'
	else:
		latest = "f=tweets&"
		url = 'https://twitter.com/search?'+latest+'q='+query+'%20since%3A'+start+'%20until%3A'+end+'&src=typd'
	driver.get(url)

	for i in range(int(num/12)):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1.5)
		#print(i)
	print()
	
	#scraping for tweets 
	details = driver.find_elements_by_class_name('original-tweet')
	file.write("text,time,name,userid,retweet,fav")
	for i in range(len(details)):
		#print(i)
		text = details[i].find_element_by_class_name('tweet-text').text
		text = re.sub("(\n|;)", " ", text)
		timestamp = details[i].find_element_by_class_name('tweet-timestamp').get_attribute('title')
		name = details[i].get_attribute('data-name')
		userid = details[i].get_attribute('data-screen-name')
		rt = int(details[i].find_element_by_class_name('ProfileTweet-action--retweet').find_element_by_class_name('ProfileTweet-actionCount').get_attribute('data-tweet-stat-count'))
		fav = int(details[i].find_element_by_class_name('ProfileTweet-action--favorite').find_element_by_class_name('ProfileTweet-actionCount').get_attribute('data-tweet-stat-count'))
		file.write(('\n"%s";%s;"%s";"%s";%d;%d'%(text,timestamp,name,userid,rt,fav)))
	print(timestamp, " - ", len(details))

def wrapperfetch(start,end,num,query,driver, file, toptweets):
	inc=datetime.timedelta(days=1)
	while start<end:
		fetch(str(start),str(start+inc), num,query,driver, file, toptweets)
		start += inc
	

driver = webdriver.Chrome(path_to_driver)


file = codecs.open("out.csv", "w+", "utf-8")

wrapperfetch(start,end,num,query,driver, file, toptweets)