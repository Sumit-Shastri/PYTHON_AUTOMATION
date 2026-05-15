from email.mime import image

import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://images.panda.org/assets/images/pages/welcome/orangutan_1600x1000_279157.jpg")
i = Image.open(BytesIO(r.content))

fp = open("img.jpg", 'wb')
i.save(fp)
fp.close()
