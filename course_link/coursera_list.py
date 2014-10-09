#!/usr/bin/env python
# coding=utf-8

######################################################
#
# course_list - get the list of videos and also download
# written by Arindam Pradhan (arindampradhan10@gmail.com)
# inspired by Benjamin Gleitzman (gleitz@mit.edu)
#
######################################################

import requests
from bs4 import BeautifulSoup
import os, errno,sys
import re
import argparse

def unique(seq):
    """
    generates a list of unique elements,\n
    eleminates the similar links
    """
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def course_item(soup):
    """
    Gets the course items and lectures for the coursebase
    """
    course_list_html = soup.find('div',class_='course-lectures-list')
    topic_html = course_list_html.find_all('div',class_='course-item-list-header expanded')

    view = []
    for topics in topic_html:
        top_html = str(topics.find('h3'))
        TAG_RE = re.compile(r'<[^>]+>')
        topic = TAG_RE.sub('', top_html).replace('\xc2\xa0','').replace(' ','')
        ul_html = topics.findNextSibling('ul')
        li_html = ul_html.find_all('li',class_="unviewed")
        count = len(li_html)
        ob = (count,topic)
        view.append(ob)
    return view

def build_scrape(soup,course_lecture,course_name):
    """
    Gets the url links for the video lectures,
    pptxs and pdfs...\n and store them in pdfs,
    videos_links and pptxs.
    """
    links = soup.find_all('a') # all links available

    required = [] # all the links for the pptxs ,pdfs and videos

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


    pdfs = unique(pdfs) # list of unique pdfs 
    pptxs = unique(pptxs) # list of unique pptxs
    videos_links = unique(videos_links) # list of unique videos_links

    # question2 = raw_input("Do you want it in an organised folder way? (Y/N)")
    question2 = "y"
    if question2.lower() is 'yes' or 'y': 
    ## get the urls for all the things
        with open("./{0}/pdf_links.txt".format(course_name),'w') as fpdf:
            for pdf in pdfs:
                fpdf.write(pdf)
                fpdf.write("\n")

        with open("./{0}/pptx_links.txt".format(course_name),'w') as fpptx:
            for ppt in pptxs:
                fpptx.write(pptx)
                fpptx.write("\n")

        with open("./{0}/videos_links.txt".format(course_name),'w') as fvid:
            for vids in videos_links:
                fvid.write(vids)
                fvid.write("\n")

        try:
            os.mkdir('./{0}/vids'.format(course_name))
            os.mkdir('./{0}/pdf'.format(course_name))
            os.mkdir('./{0}/pptx'.format(course_name))
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

        count=0
        for cours in course_lecture:
            os.mkdir('./{0}/vids/{1}'.format(course_name,cours[1]))
            os.mkdir('./{0}/pptx/{1}'.format(course_name,cours[1]))
            os.mkdir('./{0}/pdf/{1}'.format(course_name,cours[1]))
            
            count = count + cours[0] # index of the starting course of the week
            flag = cours[0] + count # flag - count = number of courses in that week

            # cours[0] is the number of urls in that week
            with open("./{0}/pdf/{1}/pdf_links.txt".format(course_name,cours[1]),'w') as fpdf:
                for pdf in pdfs[count:flag]:
                    fpdf.write(pdf)
                    fpdf.write("\n")

            with open("./{0}/pptx/{1}/pptx_links.txt".format(course_name,cours[1]),'w') as fpptx:
                for pptx in pptxs[count:flag]:
                    fpptx.write(pptx)
                    fpptx.write("\n")

            with open("./{0}/vids/{1}/videos_links.txt".format(course_name,cours[1]),'w') as fvid:
                for vids in videos_links[count:flag]:
                    fvid.write(vids)
                    fvid.write("\n")
    # question3 = raw_input("Do you want to download the videos?")

def get_parser():
    parser = argparse.ArgumentParser(description='generate your coursera vids,ppts and pdfs in an organised way!!')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
                        help='the question to answer')
    parser.add_argument('-a','--all', help='generate all the urls in a folder structure',
                        action='store_true')
    parser.add_argument('-v','--vid', help='give vid links only',
                        action='store_true')
    parser.add_argument('-s', '--structure', help='generate the folder structure',
                        action='store_true')
    parser.add_argument('-n','--num-links', help='number of urls or vids found', default=1, type=int)
    parser.add_argument('-v','--version', help='displays the current version of howdoi',
                        action='store_true')
    return parser

def ineed_link():
    """
    takes the argument or questions for a url to get the 
    information.
    """
    try:
        url = sys.argv[1]
        if url is None:
            url = raw_input("\nGive the coursera website url〈( ^.^)ノ--► ") # url of the coursera preview lectures 
    except IndexError:
        url = raw_input("\nGive the coursera website url〈( ^.^)ノ--► ") # url of the coursera preview lectures 
        if url is None:
            url = raw_input("\nGive the coursera website url〈( ^.^)ノ--► ") # url of the coursera preview lectures 



    html = requests.get(url).text # html of the preview website 
    soup = BeautifulSoup(html) # it's soup 
    course_lecture = course_item(soup) # course lecture preview

    course_name = url.split("/")[3]
    os.makedirs('./{0}'.format(course_name)) # creating base folder

    a_lecture = soup.find('a',class_="lecture-link")['href'] # links for the lectures 
    secret_html = requests.get(a_lecture).text # the back html page which contains all the links for lectures videos,ppts and pdfs.
    soup = BeautifulSoup(secret_html) # soup for the back html page
    build_scrape(soup,course_lecture,course_name)

if __name__ == '__main__':
    ineed_link()
    