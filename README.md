# Old-tweets-fetch
Selenium is used in python to fetch tweets.

Installation - Selenium
Download the webdriver for either Chrome of Firefox into the system. That browser should be preinstalled on the system.
Once downloaded, copy the path of the file so that it can be used in the script.
If the client doesnot have a displat, you will have to run a virtual display manually using xvfb, etc. Or you can use the python package for virtual display - pyvirtualdisplay as demonstrated in the script - selonline.py . I tested the script on an EC2 instance in AWS. 
In any case downloading the suitable webdriver depending upon the system and os specifications is essential. 

Usage - 
For a local machine with a display, use sel.py . Change only the lines 3-8 as per your requirements. 
It fetches tweets from those range of days and writes the tweet and its details into a csv file(';' as delimiter).
