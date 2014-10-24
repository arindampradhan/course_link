course_link
===========

Generate coursera videos,pdfs and pptx urllist from preview in an organised way...

Requirements
============
* wget or curl (command line tool) 
* The product only works for privew courses.
* You will need to give the course preview url 
* eg-> https://class.coursera.org/nlp/lecture/preview

Features :
==========

* Compatible with Python 2 (2.7+).
* creates a structured format for videos,pptx and pdfs
* Simply select your week and use wget no the folder to download the weeks videos.


Installation
============
	$ python setup.py install


For Current use :p
===============
cd course_link
python coursera_list.py
Give the coursera website url〈( ^.^)ノ--► https://class.coursera.org/nlp/lecture/preview







The order in which the folder get stored


	.
	└── Coursename
	    └── vids
			├── week 1
				└── urls.txt
			├── week 2
			├── ...
			└── weeks n
				└── urls.txt
	    └── pdfs
			├── week 1
			├── week 2
			├── ...
			└── weeks n
	    └── pptx
			├── week 1
			├── week 2
			├── ...
			└── weeks n
				└── urls.txt


Then simply run:

* Go to any week folder:

		$ cd vids/week1 
		$ wget -i vids_urls.txt

* To download the week videos ,pdf or pptx go to the corresponding folder and simply run 


* If you want to download all the vids at a time the urls in to parent folder correspond to all the urls...


TODO
======
Commands not working correctly...

Command
=======
	crlink

Usage
=====
simply type

	crlink <url of the coursera course preview>
	or
	crlink
	Give the coursera website url〈( ^.^)ノ--► https://class.coursera.org/nlp/lecture/preview



