import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
SSID= []
PASS= []
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        SSID.append(i)
        if results=='':
            PASS.append( '')    
        PASS.append(results)   
        
    except IndexError:
        pass
for x,y in zip(SSID,PASS):
    print(x,' ', *y)