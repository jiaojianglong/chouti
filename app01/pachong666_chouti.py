#!/user/bin/env python
# -*-coding:utf-8-*-
# coding:utf-8
import bs4
import urllib2
from bs4 import BeautifulSoup
import urlparse
import re
class UrlManager(object):
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	def add_new_url(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self,urls):
		if urls is  None or len(urls)==0:
			return
		for url in urls :
			self.add_new_url(url)

	def has_new_url(self):
		return len(self.new_urls)!=0

	def get_new_url(self):
		url = self.new_urls.pop()
		self.old_urls.add(url)
		return url
#下载器
class HtmlDownloader(object):
	def download(self,url):
		if url is None:
			return None
		response = urllib2.urlopen(url)

		if response.getcode() !=200:
			return None
		return response.read()

#解析器
class HtmlParser(object):
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		urls = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
		if urls is None or len(urls)==0 :
			return None
		for url in urls :
			new_url = url['href']
			new_full_url = " http://baike.baidu.com" +new_url
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self,page_url,soup):
		new_data = {}
		new_data['url'] = page_url
		title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
		new_data['title'] = title_node.get_text()
		summary_node = soup.find("div",class_="para")
		new_data["summary"]=summary_node.get_text()
		return new_data

	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont, "html.parser",from_encoding = "utf-8")
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data


class HtmlOutPut(object):
	def __init__(self):
		self.datas = []

	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)
	def output_html(self):
		fout = open('output.html',"w")
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")

		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>" %data['url'])
			fout.write("<td>%s</td>" %data['title'].encode('utf8'))
			fout.write("<td>%s</td>" %data['summary'].encode('utf8'))
			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		fout.close()




class SpiderMain():
	def __init__(self):
		self.urls = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.outputer = HtmlOutPut()
	#主要运行逻辑
	def craw(self,root_rul):
		#将入口函数添加到待爬取列表中
		self.urls.add_new_url(root_url)
		count = 1
		#主循环  判断待爬取列表中是否有 url
		while self.urls.has_new_url():
			try:
				#从待爬取列表中获得一个新 url
				new_url = self.urls.get_new_url()
				print "craw %d:%s" %(count,new_url)

				#将获取到的url传给下载器 下载网页
				html_cont = self.downloader.download(new_url)

				#将下载到的网页和 网页的url 传递给解析器 解析返回 新的 url 列表 和 数据
				new_urls,new_data = self.parser.parse(new_url,html_cont)
				#将返回的新url列表添加到待爬取列表中
				self.urls.add_new_urls(new_urls)
				#输出解析得到的有用数据
				self.outputer.collect_data(new_data)
				if count==10 :
					break
				count +=1
			except:
				print "craw failed"
		self.outputer.output_html()

#程序入口
if __name__ == '__main__':
	#添加爬取入口url
	root_url =' http://baike.baidu.com/view/36272.htm'
	#实例化
	obj_spider = SpiderMain()
	#运行函数
	obj_spider.craw(root_url)