#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json

class Spider(Spider):  # 元类 默认的元类 type
	def getDependence(self):
		return ['py_ali']
	def getName(self):
		return "YYDS"
	def init(self,extend=""):
		self.ali = extend[0]
		print("============YYDS============".format(extend))
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"热门":"-1",
			"华语电影":"18",
			"大陆剧":"15",
			"华语综艺":"24"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})

		result['class'] = classes
		return result
	def homeVideoContent(self):
		result = {
			'list':[]
		}
		return result
	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		form = {
			'limit': 24,
			'skip': int(pg) * 0 - 1,
			'keyword': '',
			'category_id': tid,
		}
		rsp = self.post("https://cmn.yydshd.com/api/posts",data=form)
		jo = json.loads(rsp.text)
		vodList = jo['data']['list']
		videos = []
		for vod in vodList:
			name = vod['title']
			pic = vod['cover']
			sid = vod['id']
			suffix = ''
			if vod['is_vip'] == 1:
				suffix = '会员 '
			mark = suffix
			try:
				mark = suffix + ' ' + vod['tags'][0]['title'] + ' ' + vod['subtitle']
				pass
			except Exception as e:
				pass
			videos.append({
				"vod_id":sid,
				"vod_name":name,
				"vod_pic":pic,
				"vod_remarks":mark
			})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def detailContent(self,array):
		header = {
			'user-agent': 'okhttp-okgo/jeasonlzy'
		}
		tid = array[0]
		result = {}
		id = 'ysysxy'
		key = 'kl132408'
		url = 'http://43.143.123.112:8182/zdytv/yyds/info.php?id={}&key={}&vid={}'.format(id, key, tid)
		rsp = self.fetch(url,headers=header)
		vodInfo = json.loads(rsp.text)
		videos = []
		name = vodInfo['title']
		pic = vodInfo['pic']
		mark = vodInfo['update']
		vod = {
			"vod_id":tid,
			"vod_name":name,
			"vod_pic":pic,
			"type_name":"",
			"vod_year":'',
			"vod_area":'',
			"vod_remarks":mark,
			"vod_actor":'',
			"vod_director":'',
			"vod_content":vodInfo['content']
		}
		playList = vodInfo['list']
		tmpLink = ''
		for play in playList:
			if 'aliyundrive' in play['link']:
				tmpLink = play['link']
				break
		vod['vod_play_from'] = 'AliYun原画$$$AliYun'
		newArray = [tmpLink]
		rs = self.ali.detailContent(newArray)
		vod['vod_play_url'] = rs['list'][0]['vod_play_url']
		result = {
			'list':[
				vod
			]
		}
		return result

	def searchContent(self,key,quick):		
		result = {}
		form = {
			'limit': 24,
			'skip': 0,
			'keyword': key,
			'category_id': -1,
		}
		rsp = self.post("https://cmn.yydshd.com/api/posts",data=form)
		jo = json.loads(rsp.text)
		vodList = jo['data']['list']
		videos = []
		for vod in vodList:
			name = vod['title']
			pic = vod['cover']
			sid = vod['id']
			suffix = ''
			if vod['is_vip'] == 1:
				suffix = '会员 '
			mark = suffix
			try:
				mark = suffix + ' ' + vod['tags'][0]['title'] + ' ' + vod['subtitle']
				pass
			except Exception as e:
				pass
			videos.append({
				"vod_id":sid,
				"vod_name":name,
				"vod_pic":pic,
				"vod_remarks":mark
			})
		result = {
			'list':videos
		}
		return result

	config = {
		"player": {},
		"filter": {}
	}
	header = {
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
	}
	def playerContent(self,flag,id,vipFlags):		
		return self.ali.playerContent(flag,id,vipFlags)
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]