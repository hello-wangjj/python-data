#-*-coding:utf-8-*-
# 抓取百度贴吧“http://tieba.baidu.com/p/1000000000”至“http://tieba.baidu.com/p/1000000009”这10个页面并以1000000000.html~1000000009.html这样的文件名保存到本地硬盘上
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
for i in range(1000000000, 1000000010):
    url = 'http://tieba.baidu.com/p/'
    url += str(i)
    print(url)
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    with open(str(i) + '.html', 'wb') as f:
        f.write(response.read().decode('utf-8'))
        f.close()
