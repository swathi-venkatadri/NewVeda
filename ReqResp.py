import urllib2
import urllib

# Specify the url
url = 'http://newveda.freeiz.com/Test.php?Name=Vijay'

# This packages the request (it doesn't make it) 
request = urllib2.Request(url)

# Sends the request and catches the response
response = urllib2.urlopen(request)

# Extracts the response
html = response.read()

if(html.find("Welcome")>=0):
       print "Access Granted"
else:
       print "Access Denied"

# Print it out
#print html 
