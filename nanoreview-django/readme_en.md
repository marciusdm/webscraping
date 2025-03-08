[![author](https://img.shields.io/badge/author-Marcius%20D.%20Moraes-green)](https://www.linkedin.com/in/marciusdm) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/marciusdm/portfolio/issues)

<a href="readme.md"> <img src="https://flagsapi.com/BR/flat/32.png" alt="portuguese version of this file" /></a>

# A web-scraping application to collect a list of mobile processors from [NanoReview](https://nanoreview.net/en/soc-list/rating) website 
NanoReview is a website that presents several rankings of mobile and PC processors, as well as laptops, also allowing comparisons between them. On the screenshot below you can see a ranking of mobile processors, which is the focus of this application:

![NanoReview mobile processor home](https://raw.githubusercontent.com/marciusdm/webscraping/refs/heads/main/assets/nanoreview/NanoReviewHome.png)  
It's a cool list but I've missed a form that would allow list only the most recent processors or filter by manufacturer and category. That's why I've created this small application which integrates the [Scrapy](https://scrapy.org) library, running under the hood, with [Django](https://www.djangoproject.com) framework as a front-end.
By opening this app for the first time, an empty list is shown with  a button labeled "Load processors list", whose click activates a script that scrapes the ranking shown above and stores them on a SQLite database. Then, Django reads it and display data as a paginated table, displaying 10 items per page, as shown on the picture below:

![app home page](https://raw.githubusercontent.com/marciusdm/webscraping/refs/heads/main/assets/nanoreview/Home.png "App Home-page")
This table, built with [django-tables2](https://django-tables2.readthedocs.io/en/latest/) compoonent, allows sorting by click on the desired column header.
By clicking on "Define Filters" a filter form becomes visible. There is 4 types of filters:
* Antutu score range;
* Category (flagship,  midrange and Low-end);
* Manufacturer;
* By Announced date.

![Filter](https://raw.githubusercontent.com/marciusdm/webscraping/refs/heads/main/assets/nanoreview/Filter.png "Filter")

Clicking on any processor in the "Model" column opens a page that displays additional details about the processor, just like on the original website, but with less information. At the end of the details page, a link is displayed that goes to the processor's details page on the NanoReview website. The details page is shown below:

![Details page](https://raw.githubusercontent.com/marciusdm/webscraping/refs/heads/main/assets/nanoreview/Detail.png "Processor details")

# How to build and run this app
In order to build and run this app, download the [source code](https://github.com/marciusdm/webscraping/raw/refs/heads/main/nanoreview-django/processorsrankingpage.zip) and follow the steps below:
* Create a Python project using an IDE editor like PyCharm or VsCode or  manually create a virtual environment  using the command below:  
 `python -m venv C:\path\to\new\virtual\environment` (Windows)  
 or  
 `python  -m  venv  /path/to/new/virtual/environment` (Linux or MacOs)
 * Extract the content of the zip file to the root directory of the project or virtual environment
 * On a terminal execute the following command:  
  `pip install -r requirements.txt`
 
   This command will install all needed packages for running the application:
	* [scrapy](https://scrapy.org) 
	* [django](https://www.djangoproject.com)
	* [django-filter](https://django-filter.readthedocs.io/en/stable/)
	* [django-tables2](https://django-tables2.readthedocs.io/en/latest/#)
	* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
	* [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) 
*  navigate to  'processorsrankingpage' folder:  
	`cd processorsrankingpage`   
* Start app:  
 `python manage.py runserver`
 * Open a web browser on the following addres:  
  http://127.0.0.1:8000/mobile_processors/
  * Enjoy it!
