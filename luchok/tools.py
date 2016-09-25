def save_fs(final_state):
# Запись конечных состояний
    fout = open("final_state.txt", "w")     # w - write
    print(final_state, file = fout)
    fout.close   
    
def read_fs():
    fin = open("final_state.txt", "r")       # r - read
    x = fin.read()
    return x
    
def binary_to_dictionary(binary):
# binary = b'[{...}}]'
    b1 = binary.decode('UTF-8') # декодируем
    b2 = b1[1:]                 # удаляем первый символ
    b3 = b2[:-1]                # удаляем последний символ
    return eval(b3)             # преобразуем в словарь


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

def get_emotions(path):
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
        path_file = "https://preview.c9users.io/v_ladimir/urfin_bot/luchok/" + path 
        body = str( dict( url = path_file ) )
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return binary_to_dictionary(data)



#file_path = 'photo/file_49.jpg'  
#data = get_emotions(file_path)
#print(data)
