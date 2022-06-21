import logging

import urllib.request
import json
import ast
import azure.functions as func


def clean_dict(d):
    for key, value in d.iteritems():
        if isinstance(value, list):
            clean_list(value)
        elif isinstance(value, dict):
            clean_dict(value)
        else:
            newvalue = value.strip()
            d[key] = newvalue

def clean_list(l):
    for index, item in enumerate(l):
        if isinstance(item, dict):
            clean_dict(item)
        elif isinstance(item, list):
            clean_list(item)
        else:
            l[index] = item.strip()


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

# Prepare the header so our beloved api won't refuse our query    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
    headers = {'User-Agent': user_agent}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')


    dubizzleQuery = req.params.get('dubizzleQuery')
    if not dubizzleQuery:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            dubizzleQuery = req_body.get('dubizzleQuery')

    if dubizzleQuery: 
        apiReq = urllib.request.Request(dubizzleQuery, data, headers)
        with urllib.request.urlopen(apiReq) as response:
            mybytes = response.read()
        mystr = mybytes.decode(encoding="utf-8").replace('\n', '')
        start = mystr.find("points:") + len ("points:")
        end = mystr.find("});",start)
        points = mystr[start:end]
#        logging.warn("so far")
        print("we have came this far")
        # converting string to json
#        logging.warn ("points:"+points.replace("'","\"")+"\n\n\n")
#        logging.warn("cleansed finished")
#        dumps = json.dumps(points)
#        logging.info ("points dumps:"+dumps)
#        jsonObject = json.loads(dumps)
#        for key in jsonObject:
#            value = jsonObject[key]
#            print("The key and value are ({}) = ({})".format(key, value))
#        logging.info ("oeeeeeergg")
#        final_dictionary = json.loads(ast.literal_eval(points))
  
        # printing final result
        return func.HttpResponse(points)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
