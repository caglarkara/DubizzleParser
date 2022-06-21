import re

import urllib.request

import sys
print (sys.path)

print ("Carreara120k")


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"

values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')


testUrl = "https://dubai.dubizzle.com/motors/used-cars/porsche/carrera/?site=2&s=MT&rc=140&c1=1530&c2=1534&c3=&price__gte=&price__lte=120000&year__gte=&year__lte=&kilometers__gte=&kilometers__lte=&seller_type=OW&buyer_market=&keywords=&is_basic_search_widget=0&is_search=1&places=&places__id__in=&auto_agents=&auto_agent__id__in=&added__gte=&motors_trim="

#fp = urllib.request.urlopen("https://raw.githubusercontent.com/caglarkara/DubizzleParser/main/samples/carrera120K")
#fp = urllib.request.urlopen(testUrl)
#mybytes = fp.read()
req = urllib.request.Request(testUrl, data, headers)
with urllib.request.urlopen(req) as response:
   mybytes = response.read()


#mystr = mybytes.decode("utf8")
mystr = mybytes.decode(encoding="utf-8").replace('\n', '')

#fp.close()
#mapListingsData = re.search(r"(?<=mapListingsData = ).*?(?=}];)", req_body).group(0).replace('\\','')+'}]'
    

print("CALL TO URL Successful")

print(mystr)
     
print ("ALOOO")
#m = re.search('(?<=abc)def', 'abcdef')
#print(m.group(0))

#req_body = mystr.decode(encoding="utf-8").replace('\n', '')

if mystr:
	start = mystr.find("points:") + len ("points:")
	end = mystr.find("});",start)
	print("Points decode success")
	print (start)
	print (end)
	points = mystr[start:end]
	print(points)
else:
	print ("Error")

      
#    if points:
 #       return func.HttpResponse(f"{points}")
 #   else:
 #       return func.HttpResponse(
 #            "Please pass a valid html on the request body",
 #            status_code=400
 #       )