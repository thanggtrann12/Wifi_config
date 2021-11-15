import urllib.request
flag= False
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

if connect() :  flag = True
else : flag = False