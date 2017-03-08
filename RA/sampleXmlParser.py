import json
import requests
from collections import OrderedDict
from xml.etree.ElementTree import parse
from time import sleep


with open("sample_003.json", mode="r", encoding="utf-8") as fp:
    load_dict = json.load(fp)
    result = OrderedDict(load_dict)
real_result = OrderedDict()


for i, contid in enumerate(result):
    try:
        year = contid[:4]
        month = contid[4:6]
        day = contid[6:8]
        url = "http://news.chosun.com/priv/data/www/news/{}/{}/{}/{}.xml".format(
            year,
            month,
            day,
            contid
        )
        with open("temp.xml", mode="w", encoding="utf-8") as fp:
            r = requests.get(url)
            text = r.text
            fp.write(text)
        tree = parse("temp.xml")
        root = tree.getroot()
        text = root.find("body")\
            .find("page")\
            .find("paragraph")\
            .find("text")\
            .text\
            .strip()
        result[contid]["text"] = text
        if "청계" in result[contid]["title"]:
            print(">>> title detected")
            real_result[contid] = result[contid]
        print(contid, len(text))
        sleep(0.1)
    except:
        print(">> error!")
        print(url)

with open("sample_finish_001.json", mode="w", encoding="utf-8") as fp:
    json.dump(
        result,
        fp,
        ensure_ascii=False,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )

with open("sample_finish_002.json", mode="w", encoding="utf-8") as fp:
    json.dump(
        real_result,
        fp,
        ensure_ascii=False,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )
