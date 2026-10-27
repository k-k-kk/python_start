# 从这个网站上获取数据，记得命令行参数1要输入歌手名
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()


response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent = 2))