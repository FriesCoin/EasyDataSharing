import json
import math
import os, sys
home = os.path.join(os.path.dirname(__file__))+ "/"
f = open(home + "data.json", 'r')
datas = json.load(f)
f.close()
basicInfo = {"name": "","to": "","data": {}}
AlertsSize = 0
def getFrom(reader,author,id,ValueId):
    data = datas["data"][id]
    if data["name"] == author:
        if data["to"] == reader:
            return data["data"][ValueId]
def Updates():
    global AlertsSize
    if AlertsSize < datas["Alerts"]:
        AlertsSize = datas["Alerts"]
        return True
    if AlertsSize == datas["Alerts"]:
        return False
def UpdateValue():
    global datas
    f = open(home + "data.json", 'r', encoding = 'utf-8')
    datas = json.load(f)
    f.close()
def Alert():
    datas["Alerts"] += 1
def IdFromAuthor(author):
    return datas["authors"][author]
def UpdateData(author,reader,ValueId,Value,id=-1):
    global datas
    if id == -1:
        datas["data"].extend(basicInfo)
        id = datas.index(basicInfo)
        datas["data"][id]["name"] = author
        datas["data"][id]["to"] = reader
        datas["data"][id]["data"][ValueId] = Value
        f = open(home + "data.json", 'w+')
        f.truncate(0)
        f.seek(0)
        f.write(datas)
        f.close()
        Alert()
        return id
    if id != 0:
        datas = datas["data"][id]["data"][ValueId] = Value
        Alert()
        return