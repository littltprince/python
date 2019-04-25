#encoding:utf-8
from selenium import webdriver
import os
import subprocess
import traceback
import logging
from PIL import Image
import time

r=webdriver.Chrome()
url="http://admin.test.shaoziketang.com/"
r.get(url)
r.implicitly_wait(5)
r.add_cookie({'username':'root', 'password':'a123456'})
r.add_cookie({'cookie': "UM_distinctid=16a351f763953-0e019b1090d63b-3c644d0e-100200-16a351f763ac1; Hm_lvt_383c00e895880226fe046f022e80a701=1555377135,1555664914,1555669417,1555928180; XSRF-TOKEN=eyJpdiI6ImFNNjlzMmF3WEkxUEtEVE15a01RclE9PSIsInZhbHVlIjoiVU1MemI5U0dtWWFMR0lsM0xLZU5Fa0Zmd3U3d1M4N0VMY09zTTVxSzROQTYySkdVbW1BbU5oQ2ZiaEZEdGliUSIsIm1hYyI6IjQ3NDgzNDBkNzFkNWE0ZDU0NzRkNzAzYzQ4ZThhYTA0ZGQzMTg5ODk1ZGQzMjA4NGVjOWIwOTI1ZTMxNGE2ZTMifQ%3D%3D; laravel_session=eyJpdiI6InV5OWpRUUJVOFBubEFpRVVWbytteVE9PSIsInZhbHVlIjoiVVB0eXlqZEdOVG9SWmhWUDdWVlkwM2tCclN0dnhGRlpLZkNQMFwvcFoxXC95XC9scDExeUVjV1g0dGJoSzd6bEwyOSIsIm1hYyI6IjI5ZmJhY2UzYTY0NGUyMGI3ZjlmZTllYTk3ZjRmNWM2ZDEyY2M0MjdmM2NjZDhhNzEzZjk3ZTI0NWRjOTc2ZTMifQ%3D%3D"})
time.sleep(3)
# r.find_element_by_name("username").send_keys("root")
# r.find_element_by_name("password").send_keys("a123456")
r.refresh()
