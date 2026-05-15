# Find any image URL online
# Download and save it locally as a .jpg file

import requests
from PIL import Image
from io import BytesIO

img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZDRlIg4IOm_hpNUnMwogV7DQ-d6TXwH7fDA&s"

r = requests.get(img_url)
i = Image.open(BytesIO(r.content))

fp = open("monkey.jpg", 'wb')
i.save(fp)
fp.close()