# Python Example 

#Variables

# _url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
# _key = e141bb5d-cfef-42db-9641-44b779568ea6 #Here you have to paste your primary key
# _maxNumRetries = 10

#[
#  {
#    "faceRectangle": {
#      "left": 68,
#      "top": 97,
#      "width": 64,
#      "height": 97
#    },
#    "scores": {
#      "anger": 0.00300731952,
#      "contempt": 5.14648448E-08,
#      "disgust": 9.180124E-06,
#      "fear": 0.0001912825,
#      "happiness": 0.9875571,
#      "neutral": 0.0009861537,
#      "sadness": 1.889955E-05,
#      "surprise": 0.008229999
#    }
#  }
#]

def get_emotions(fr, s)

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
from tools import binary_to_dictionary

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '1da9dcb20f1a4efc8593b1d79e076ce3',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    body = '{ "url": "https://preview.c9users.io/v_ladimir/urfin_bot/luchok/2.jpg" }'
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

#обработка базы

#d = b'[{"faceRectangle":{"height":426,"left":242,"top":391,"width":426},"scores":{"anger":7.253733E-05,"contempt":0.005009529,"disgust":9.923835E-05,"fear":5.30315765E-06,"happiness":0.213434368,"neutral":0.7774695,"sadness":0.0037772425,"surprise":0.00013225642}}]'
#d1 = b'[{"faceRectangle":{"height":426,"left":242,"top":391,"width":426},"scores":{"anger":7.253733E-05,"contempt":0.005009529,"disgust":9.923835E-05,"fear":5.30315765E-06,"happiness":0.213434368,"neutral":0.7774695,"sadness":0.0037772425,"surprise":0.00013225642}}]'.decode('UTF-8')
#d2 = d1[1:]
#d3 = d2[:-1]

data2 = binary_to_dictionary(data)

fr = []
s = []

for key_1 in "faceRectangle", "scores":
    if key_1 == "faceRectangle":
        for key_2 in "left", "top", "width", "height":
            fr.append(round(data2.get(key_1).get(key_2), 2))          
                        
    if key_1 == "scores":
        for key_2 in ("anger", "contempt", "disgust", "fear",
                     "happiness", "neutral", "sadness", "surprise"):
            s.append(round(data2.get(key_1).get(key_2), 3))
            
print(fr)
print(s)
        
