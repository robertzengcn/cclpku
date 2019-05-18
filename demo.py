# -*- coding: utf-8 -*-
import re
import urllib, urllib2, sys
import ssl
import json
import pandas as pd

class Demo(object):

        def __init__(self):
            self.filename='./corpus.txt'
            #改成自己的token https://ai.baidu.com/tech/nlp_basic/lexical
            self.token='24.aaee6a87b34413d9fec1e82d46391261.2592000.1560762472.282335-16283946'
            self.csvres=[]
        def handlefile(self):
            try:
                fp = open(self.filename,'r')
                line=fp.readline()
                self.handline(line)
                cnt=1
                while line:
                    # print("Line {}: {}".format(cnt, line.strip()))
                    line = fp.readline()
                    cnt+=1
                    self.handline(line)
            finally:
                fp.close()

        def handline(self,line):
            regex = ur"\[走\](.*?)\s"
            line=line.decode("utf-8")
            searchObj = re.search(regex, line, re.M|re.I)
            if searchObj:

                # print "searchObj.group(1) : ", searchObj.group(1)
                self.sendtoapi(searchObj.group(1),line)
            else:
                print "Nothing found!!"

        def sendtoapi(self,str,originline):
            str=str.encode("utf-8")
            url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token='+self.token
            headers = {"Content-Type": "application/json"}
            formate ={
                "text": str
            }
            data = json.dumps(formate)
            request = urllib2.Request(url, data=data, headers=headers)
            response = urllib2.urlopen(request)
            if response:
                text = json.loads(response.read())
                res=text.get("items")
                if res:
                    list=[]
                    list.append(originline.encode("utf-8"))
                    list.append(str)
                    for values in text["items"]:
                        pres=values["item"]+"("+values["pos"]+")"
                        pres=pres.encode("utf-8")
                        list.append(pres)
                    self.csvres.append(list)

        def savetoCsv(self):
            save = pd.DataFrame(self.csvres)
            save.to_csv('./result.csv', index=False, header=False)







testDemo = Demo()

testDemo.handlefile()

testDemo.savetoCsv()


