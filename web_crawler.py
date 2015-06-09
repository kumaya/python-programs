# program to return all traversed urls from a baseurl
import re
import urlparse
import urllib

# baseurl = "http://python.org"
baseurl = "http://google.com"

visited = []
htmltext = urllib.urlopen(baseurl).read()

link_re = re.compile(r'href="(.*?)"')

links_list = link_re.findall(htmltext)

count = 0
for link in links_list:
	if not link in visited:
		res = urlparse.urljoin(baseurl, link)
		visited.append(res)
		print "\t", res

print "Total sites crawled from baseurl: ", len(visited)