#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import os, errno

try:
    os.makedirs('./keep')
except OSError as exc: # Python >2.5
    if exc.errno == errno.EEXIST and os.path.isdir(path):
        pass
    else: raise


url = raw_input("\nGive the coursera website url〈( ^.^)ノ--► ") # url of the coursera preview lectures 


html = requests.get(url).text # html of the preview website 
soup = BeautifulSoup(html) # it's soup 
a_lecture = soup.find('a',class_="lecture-link")['href'] # links for the lectures 
secret_html = requests.get(a_lecture).text # the back html page which contains all the links for lectures videos,ppts and pdfs.
soup = BeautifulSoup(secret_html) # soup for the back html page
links = soup.find_all('a') # all links available 

required=[] # all the links for the ppts ,pds and videos 
for link in links:
    if "cloudfront" in link['href']:
        required.append(link['href'])

pdfs=[] # pdfs links for the lectures
for pdf in required:
    if pdf.endswith('pdf'):
        pdfs.append(pdf)

pptxs=[] # pptxs for the lectures
for pptx in required:
    if pptx.endswith('pptx'):
        pptxs.append(pptx)

videos_links=[] # video links for lectures
for link in links:
    if "download.mp4" in link['href']:
        videos_links.append(link['href'])


def unique(seq):
    """
    generates a list of unique elements,\n
    eleminates the similar links
    """
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

pdfs = unique(pdfs) # list of unique pdfs 
pptxs = unique(pptxs) # list of unique pptxs
videos_links = unique(videos_links) # list of unique videos_links 

with open("./keep/pdf_links.txt",'w') as fpdf:	
    for pdf in pdfs:
	    fpdf.write(pdf)
	    fpdf.write("\n")

with open("./keep/pptx_links.txt",'w') as fpptx:
	for ppt in pptxs:
	    fpptx.write(pptx)
	    fpptx.write("\n")

with open("./keep/videos_links.txt",'w') as fvid:
	for vids in videos_links:
	    fvid.write(vids)
	    fvid.write("\n")
