# coding=utf-8
# !/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json
import re
import difflib
import urllib

class Spider(Spider):  # 元类 默认的元类 type
    def getName(self):
        return "Alist"

    def init(self, extend=""):
        print("============{0}============".format(extend))
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):
        result = {}
        cateManual = {
            "菊花盘": "https://pan.142856.xyz/OneDrive",
            "触光云盘": "https://pan.ichuguang.com",
            "小孟资源": "https://8023.haohanba.cn",
            "资源小站": "https://960303.xyz",
            "轻弹浅唱": "https://g.xiang.lol",
            "小兵组网盘视频": "https://pan.ichuguang.com"
        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name': k,
				"type_flag": "1",
                'type_id': cateManual[k]
            })
        result['class'] = classes
        if (filter):
            result['filters'] = self.config['filter']
        return result

    def homeVideoContent(self):
        result = {
            'list': []
        }
        return result

    ver = ''
    baseurl = ''
    def getVersion(self, gtid):
        param = {
            "path": '/'
        }
        if gtid.count('/') == 2:
            gtid = gtid + '/'
        baseurl = re.findall(r"http.*://.*?/", gtid)[0]
        ver = self.fetch(baseurl + 'api/public/settings', param)
        vjo = json.loads(ver.text)['data']
        if type(vjo) is dict:
            ver = 3
        else:
            ver = 2
        self.ver = ver
        self.baseurl = baseurl

    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        if tid.count('/') == 2:
            tid = tid + '/'
        nurl = re.findall(r"http.*://.*?/", tid)[0]
        if self.ver == '' or self.baseurl != nurl:
            self.getVersion(tid)
        ver = self.ver
        baseurl = self.baseurl
        if tid.count('/') == 2:
            tid = tid + '/'
        pat = tid.replace(baseurl,"")
        param = {
            "path": '/' + pat
        }
        if ver == 2:
            rsp = self.postJson(baseurl + 'api/public/path', param)
            jo = json.loads(rsp.text)
            vodList = jo['data']['files']
        elif ver == 3:
            rsp = self.postJson(baseurl + 'api/fs/list', param)
            jo = json.loads(rsp.text)
            vodList = jo['data']['content']
        videos = []
        for vod in vodList:
            if ver == 2:
                img = vod['thumbnail']
            elif ver == 3:
                img = vod['thumb']
            if len(img) == 0:
                if vod['type'] == 1:
                    img = "http://img1.3png.com/281e284a670865a71d91515866552b5f172b.png"
            if pat != '':
                aid = pat + '/'
            else:
                aid = pat
            if vod['type'] == 1:
                tag = "folder"
                remark = "文件夹"
            else:
                size = vod['size']
                if size > 1024 * 1024 * 1024 * 1024.0:
                    fs = "TB"
                    sz = round(size / (1024 * 1024 * 1024 * 1024.0), 2)
                elif size > 1024 * 1024 * 1024.0:
                    fs = "GB"
                    sz = round(size / (1024 * 1024 * 1024.0), 2)
                elif size > 1024 * 1024.0:
                    fs = "MB"
                    sz = round(size / (1024 * 1024.0), 2)
                elif size > 1024.0:
                    fs = "KB"
                    sz = round(size / (1024.0), 2)
                else:
                    fs = "KB"
                    sz = round(size / (1024.0), 2)
                tag = "file"
                remark = str(sz) + fs
            aid = baseurl + aid + vod['name']
            videos.append({
                "vod_id":  aid,
                "vod_name": vod['name'],
                "vod_pic": img,
                "vod_tag": tag,
                "vod_remarks": remark
            })
        result['list'] = videos
        result['page'] = 1
        result['pagecount'] = 1
        result['limit'] = 999
        result['total'] = 999999
        return result

    def detailContent(self, array):
        id = array[0]
        if self.ver == '' or self.baseurl == '':
            self.getVersion(id)
        ver = self.ver
        baseurl = self.baseurl
        fileName = id.replace(baseurl, "")
        dir = re.findall(r"(.*)/", fileName)[0].replace(baseurl, "")
        dirparam = {
            "path": '/' + dir,
            "password": "",
            "page_num": 1,
            "page_size": 100
        }
        vod = {
            "vod_id": fileName,
            "vod_name": dir,
            "vod_pic": '',
            "vod_tag": '',
            "vod_play_from": "播放",
        }
        if ver == 2:
            drsp = self.postJson(baseurl + 'api/public/path', dirparam)
            djo = json.loads(drsp.text)
            dList = djo['data']['files']
        elif ver == 3:
            drsp = self.postJson(baseurl + 'api/fs/list', dirparam)
            djo = json.loads(drsp.text)
            dList = djo['data']['content']
        playUrl = ''
        for tempd in dList:
            if 'mp4' in tempd['name'] or 'mkv' in tempd['name'] or 'TS' in tempd['name'] or 'flv' in tempd['name'] or 'rmvb' in tempd['name'] or 'mp3' in tempd['name'] or 'flac' in tempd['name'] or 'wav' in tempd['name']:
            # 开始匹配视频
                # 视频名称 name
                name = tempd['name']
                # 视频链接 url
                fname = re.findall(r"(.*)/", fileName)[0] + '/' + name
                url = baseurl + fname
                # 开始找字幕 subt
                vname = re.findall(r"(.*)\.", tempd['name'])[0]
                vstr = re.findall(r"\'name\': \'(.*?)\'", str(dList))
                if len(vstr) == 2:
                    suball = vstr
                else:
                    suball = difflib.get_close_matches(vname, vstr, len(dList), cutoff=0.8)
                for sub in suball:
                    if sub.endswith(".ass") or sub.endswith(".srt"):
                        subt = '@@@' + baseurl + dir + '/' +sub
                ifsubt = 'subt' in locals().keys()
                if ifsubt is False:
                    playUrl = playUrl + '{0}${1}#'.format(name, url)
                else:
                    playUrl = playUrl + '{0}${1}{2}#'.format(name, url, subt)
        vod['vod_play_url'] = playUrl
        result = {
            'list': [
                vod
            ]
        }
        return result

    def searchContent(self, key, quick):
        result = {
            'list': []
        }
        return result

    def playerContent(self, flag, id, vipFlags):
        result = {}
        ifsub = '@@@' in id
        if ifsub is True:
            ids = id.split('@@@')
            if self.ver == '' or self.baseurl == '':
                self.getVersion(ids[1])
            ver = self.ver
            baseurl = self.baseurl
            fileName = ids[1].replace(baseurl, "")
            vfileName = ids[0].replace(baseurl, "")
            param = {
                "path": '/' + fileName,
                "password": "",
                "page_num": 1,
                "page_size": 100
            }
            vparam = {
                "path": '/' + vfileName,
                "password": "",
                "page_num": 1,
                "page_size": 100
            }
            if ver == 2:
                rsp = self.postJson(baseurl + 'api/public/path', param)
                jo = json.loads(rsp.text)
                vodList = jo['data']['files'][0]
                subturl = vodList['url']
                vrsp = self.postJson(baseurl + 'api/public/path', vparam)
                vjo = json.loads(vrsp.text)
                vList = vjo['data']['files'][0]
                url = vList['url']
            elif ver == 3:
                rsp = self.postJson(baseurl + 'api/fs/get', param)
                jo = json.loads(rsp.text)
                vodList = jo['data']
                subturl = vodList['raw_url']
                vrsp = self.postJson(baseurl + 'api/fs/get', vparam)
                vjo = json.loads(vrsp.text)
                vList = vjo['data']
                url = vList['raw_url']
            if subturl.startswith('http') is False:
                head = re.findall(r"h.*?:", baseurl)[0]
                subturl = head + subturl
            if url.startswith('http') is False:
                head = re.findall(r"h.*?:", baseurl)[0]
                url = head + url
            urlfileName = urllib.parse.quote(fileName)
            subturl = subturl.replace(fileName, urlfileName)
            urlvfileName = urllib.parse.quote(vfileName)
            url = url.replace(vfileName, urlvfileName)
            result['subt'] = subturl
        else:
            if self.ver == '' or self.baseurl == '':
                self.getVersion(id)
            ver = self.ver
            baseurl = self.baseurl
            vfileName = id.replace(baseurl, "")
            vparam = {
                "path": '/' + vfileName,
                "password": "",
                "page_num": 1,
                "page_size": 100
            }
            if ver == 2:
                vrsp = self.postJson(baseurl + 'api/public/path', vparam)
                vjo = json.loads(vrsp.text)
                vList = vjo['data']['files'][0]
                url = vList['url']
            elif ver == 3:
                vrsp = self.postJson(baseurl + 'api/fs/get', vparam)
                vjo = json.loads(vrsp.text)
                vList = vjo['data']
                url = vList['raw_url']
            if url.startswith('http') is False:
                head = re.findall(r"h.*?:", baseurl)[0]
                url = head + url
            urlvfileName = urllib.parse.quote(vfileName)
            url = url.replace(vfileName, urlvfileName)
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = url
        result["header"] = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        return result

    config = {
        "player": {},
        "filter": {}
    }
    header = {}

    def localProxy(self, param):
        return [200, "video/MP2T", action, ""]