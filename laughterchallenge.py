import pafy
from BeautifulSoup import BeautifulSoup
import urllib2
import sys

def fetchLinks():
	
	#All the markup that'll be parsed for links
	response = urllib2.urlopen("https://www.youtube.com/show/thegreatindianlaughterchallenge/videos?sort=da&view=8&flow=list")
	
	#print soup	
	soup = BeautifulSoup(response)	
	found_links = []
	return_links = []
	numFound = 0
	
	for link in soup.findAll('a'):
		linkTitle = str(link.get('title'))
		testSlug = "The Great Indian Laughter Challenge - Season"
		if(testSlug in linkTitle):
			numFound+=1	
			print str(numFound) +" - link found - "+linkTitle+ '\n'+(link.get('href'))
			found_links.append(link.get('href'))
		
	for link in found_links:
		link="https://www.youtube.com"+link
		return_links.append(link)

	return return_links


def dlVideo(url_list):

	for url in url_list:
		video = pafy.new(url)
		best = video.getbest()
		print video.title+"_"+best.resolution+"_"+best.extension 
		
		dlPath = "vids/"+best.title+"_"+best.resolution+"_"+best.extension
		best.download(quiet=False, filepath=dlPath)

if __name__ == "__main__":
	a = fetchlinks()
	print a
	dlVideo(a) #download videos
	
