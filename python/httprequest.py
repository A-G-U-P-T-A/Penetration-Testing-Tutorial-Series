#creating a simple http client....
import http.client #one of the packages that helps perform http requests.
#creating HTTPConnection() object.
h = http.client.HTTPConnection("www.wikipedia.com")
h.request("GET", "/")
#requesting response
data = h.getresponse()
#printing the status code, version and headers for the response received.
print("Code : "+str(data.status))
print("Version : "+str(data.version))
print(data.headers)
#printing the message body/html received from the response
#its encoded in utf-8 format so need to decode and display it...
body = data.readlines()

for i in body:
	print(i.decode('utf-8'))
#so we are done here and lets test the code now......
