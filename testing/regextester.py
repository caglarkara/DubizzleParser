import re

import urllib.request

print ("Carreara120k")

fp = urllib.request.urlopen("https://raw.githubusercontent.com/caglarkara/DubizzleParser/main/samples/carrera120K")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
     
print ("ALOOO")

#    req_body = req.get_body().decode(encoding="utf-8").replace('\n', '')
#    points = re.search(r"(?<=points: ).*?(?=}];)", req_body).group(0).replace('\\','')+'}]'

      
#    if points:
 #       return func.HttpResponse(f"{points}")
 #   else:
 #       return func.HttpResponse(
 #            "Please pass a valid html on the request body",
 #            status_code=400
 #       )