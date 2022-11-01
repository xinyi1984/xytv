#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import requests

class Spider(Spider):
	def getDependence(self):
		return ['py_ali']
	def getName(self):
		return "py_yiso"
	def init(self,extend):
		self.ali = extend[0]
		print("============py_yiso============")
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		return result
	def homeVideoContent(self):
		result = {}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		return result
	header = {
		"User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36",
		"Referer": "http://ali.freepan.net/"
	}
	def detailContent(self,array):
		return self.ali.detailContent(array)

	def searchContent(self,key,quick):
		url = "http://ali.freepan.net/?q={0}&from=ali".format(key)
		vodList = requests.get(url=url, headers=self.header, verify=False).json()["data"]["list"]
		videos = []
		for vod in vodList:
			videos.append({
				"vod_id": vod["url"],
				"vod_name": vod["fileInfos"][0]["fileName"],
				"vod_pic": "https://inews.gtimg.com/newsapp_bt/0/13263837859/1000",
				"vod_remarks": vod['gmtCreate']
			})
		result = {
			'list':videos
		}
		return result

	def playerContent(self,flag,id,vipFlags):
		return self.ali.playerContent(flag,id,vipFlags)

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]