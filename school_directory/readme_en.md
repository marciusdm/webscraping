[![author](https://img.shields.io/badge/author-Marcius%20D.%20Moraes-green)](https://www.linkedin.com/in/marciusdm) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/marciusdm/portfolio/issues)

<a href="readme.md"> <img src="https://flagsapi.com/BR/flat/32.png" alt="portugues version of this file" /></a>

# A web-scraping application to collect data from the website [https://www.schooldirectory.org/](https://www.schooldirectory.org/)
Based on a request from the Upwork website to scrape school counselor data from the [School Directory](https://www.schooldirectory.org/) website , a project was created using the [Scrapy](https://scrapy.org/) library (Click [here](https://medium.com/@marciusdellano/introduction-to-web-scraping-using-the-scrapy-tool-e0138dd95080) to read an introductory article about Scrapy). Scrapy works with the concept of 'spiders' that allow it to analyze the source code of each page and extract the desired information using CSS or XPath selectors. It is also possible to extract links and navigate through them. First, the website's home page is accessed, where there is a section called "Browse by Cities", as shown in the figure below:
![School Directory home page](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_home.png?raw=true)
There is a list of states or regions (the state of California was split into two regions: north and south), each containing a link that accesses the list of cities by state, which is shown below:
 ![cities by region](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_browse_by_cities.png?raw=true)
   
The spider then collects and accesses the links for each city, which display a list of schools per city:
![Schools from Palo Alto, CA](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_schools_by_city.png?raw=true)
In this step, the links for each school are collected. This list displays 10 schools per page. If the city in question has more than 10 schools, a pager is displayed:
![pager](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_next_page.png?raw=true)
The spider captures and accesses the link contained in the item defined by >>. After obtaining the links for all the schools, the pages for each of them are accessed, and then we collect the data from the "College Counseling info" section:
  ![ 'college counseling info' section](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_college_counseling.png?raw=true)
Here, the name, email, position and phone number are extracted and a CSV file is generated with the following fields:
-   state_region
-   city
-   school
-   first_name
-   middle_name
-   last_name,
-   job_title,
-   mail
-   phone

# How to run this application 
* Download the [source code](https://github.com/marciusdm/webscraping/raw/refs/heads/main/school_directory/counselinginfo.zip) 
* Create an virtual environment with an IDE python, such as PyCharm ou VsCode; or even manually, by uing this command:   
  `python -m venv <path_to_venv>`  
 and extract the contentes of the downloaded file to the root directory of the virtual environment 
* Install the Scrapy library through the command:  
 `pip install scrapy`
* navigate to the *counselinginfo* directory:  
   `cd counselinginfo`
* run the following command in order to extract the school counselors list:  
  `scrapy crawl academics -o counselors.csv:csv `

This list will be located in a file called 'counselors.csv' in the same directory where the command was run.
