import ConfigParser
import sys
import time
import logging
import os
import urllib2

logfile=os.path.join(os.getcwd(),'monitor.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG,)

def log(msg):
	logging.info("\t" + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) + "\t" + msg)

def monitor(urls):	
	for each_url, content in urls.iteritems():
		content_found = False
		website_status = ''
		response_code=None
		start_time = time.time()
		url = ''
		try:
			url = urllib2.urlopen(each_url)
		except urllib2.HTTPError, e:
			response_code = e.getcode()
		except urllib2.URLError, e:
			response_code = 400
		else:
			response_code = url.getcode()
		elapsedTime = time.time()-start_time
		
		if response_code == 200:			
			website_status = 'UP'
			if content in str(url.read()):
				content_found = True
		if response_code in range(400, 600):
			website_status = 'DOWN'

		log("WEB URL: %s SearchKey:%s WEBURL STATUS:%s CONTENT FOUND:%s Time Taken:%s seconds"%(each_url, content, website_status, content_found, elapsedTime))

if __name__ == '__main__':
	interval=''
	testurls = dict()
	try:
		config = ConfigParser.ConfigParser()
		config.read(os.path.join(os.getcwd(),'configuraton.cfg'))
		interval = int(config.get('settings', 'interval'))
		testurls = eval(config.get('settings', 'testurls'))
	except:
		print "Exception raised when reading configuration file, check the contents in the config file, or config file doesnot exist"
		sys.exit(1)

	counter = 1
	while True and len(testurls) > 0:
		print("Monitor Websites Iteration:%s"%counter)
		try:
			monitor(testurls)
			print "waiting for %s seconds before checking the statuses of urls again"%interval	
			time.sleep(interval)
		except KeyboardInterrupt:
			print "Program exited because of keyboard interpurt"
			sys.exit(1)
		counter = counter + 1
	print "No urls to monitor, so exiting the program"