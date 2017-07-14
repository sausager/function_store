# -*- coding: utf-8 -*-
import sqlite3
import json
import types
import array
import re
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
# print sys.getdefaultencoding()

config = ['/home/libraxyy/.deepinwine/Deepin-ThunderSpeed/drive_c/Program Files/Thunder Network/Thunder/Profiles/TaskDb.dat']
tables = ['']
global superSpeedTables
superSpeedTables = []
datas = ['']
tempdata = ['']
global newdata
newdata = ''
newdatas = []
global rows
rows = 0

def getTables():
    conn = sqlite3.connect(config[0])
    c = conn.cursor()
    c.execute('SELECT name FROM sqlite_master WHERE type="table"')
    conn.commit()
    tables[0] = c.fetchall()
    pregStr = u'AccelerateTaskMap\d*_superspeed_\S*'
    for table in tables[0]:
        preg = re.compile(pregStr)
        matches = preg.findall(table[0])
        if matches:
            global superSpeedTables
            superSpeedTables = []
            superSpeedTables.append(matches[0])
    c.close()
    conn.close()
    if len(superSpeedTables) != 0:
        getUserData()
    else:
        exit(0)

def getUserData():
    conn = sqlite3.connect(config[0])
    c = conn.cursor()
    for superSpeedTable in superSpeedTables:
        c.execute('SELECT UserData FROM ' + superSpeedTable)
        conn.commit()
        datas[0] = c.fetchall()
        c.close()
        conn.close()
        updateUserData()

def updateUserData():
    conn = sqlite3.connect(config[0])
    c = conn.cursor()
    for data in datas[0]:
        listdata = json.loads(str(data[0]))
        # print str(data[0])
        listdata['Result'] = 0
        listdata = json.dumps(listdata,ensure_ascii=False)
        # print listdata
        global newdata
        newdata = buffer(listdata)
        tempdata[0] = newdata
        global newdatas
        newdatas.append(tempdata)
    for superSpeedTable in superSpeedTables:
        global rows
        rows = c.executemany("UPDATE "+superSpeedTable+" set UserData = ?",newdatas)
        if rows > 0:
            # os.system('xdg-open /usr/local/share/applications/deepin.com.thunderspeed.desktop')
            print 'done'
        else:
            print 'fail'
            exit(0)
        conn.commit()
        conn.close()
        newdatas = []

getTables()
# print newdatas
# print datas
