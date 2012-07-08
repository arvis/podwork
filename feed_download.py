import feedparser
import urllib2
#<guid isPermaLink="true">http://inessential.com/2002/09/01.php#a2</guid>
import time
import os

class FeedDownloader(object):
	"""Feeds dowload class"""
	def __init__(self):
		pass


	def check_file_exists(self, file_path):
		if os.path.isfile(file_path):
			return True

	def dowload_file(self, file_link,file_name):
		out_dir="out/"

		try:
		#if file exsists it means it is already downloaded
			if self.check_file_exists(out_dir+file_name):
				return

			response = urllib2.urlopen(file_link)
			output = open(out_dir+file_name,'wb')
			output.write(response.read())
			output.close()
		except urllib2.HTTPError, e:
			print e.code
		except urllib2.URLError, e:
			print e.args


	def get_file_name(self,file_link):
		# TODO: if last char is slash, remove it
		file_name = file_link.split('/')[-1]

		print file_name
		return "%s.mp3" % file_name


	def get_podcasts(self,pod_link):
		f=feedparser.parse(pod_link)
		return f["items"]

	def dowload_podcasts(self,pod_link):
		feed_data=self.get_podcasts(pod_link)

		for pod_link in feed_data:
			file_link=pod_link.link
			file_name=self.get_file_name(file_link)

			if file_name!="":
				#file_name="tmp_name_"+str(time.time())
				self.dowload_file(file_link,file_name)



if __name__ == '__main__':
	dd=FeedDownloader()
	dd.dowload_podcasts("http://127.0.0.1:8000/latest/feed/")




