#!/usr/bin/env python3
#By Dx55

import requests
import shutil

#Download function
def download():
        x = str(input("Link\n"))
        y = str(input("Name\n"))
        
        r = requests.get(x, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open(str(y + ".jpg"), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
#Loop
while True:
    download()
    if input("Un'altra?") == 'n':
        break
