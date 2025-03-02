import logging
from time import sleep
import re
import scrapy
from scrapy.loader import ItemLoader

from counselinginfo.Helper import Helper
from counselinginfo.items import CounselinginfoItem

from counselinginfo import settings


class AcademicsSpider(scrapy.Spider):
    name = "academics"
    allowed_domains = ["www.schooldirectory.org"]
    start_urls = ["https://www.schooldirectory.org"]

    def parse(self, response, **kwargs):
        state_links=response.xpath(
            settings.STATEREGION_LINK_SELECTOR
        ).getall()
        for link in state_links[4:5]:
            #Browse states
            sleep(2)
            yield scrapy.Request(link, callback=self.parse_location)

    def parse_location(self, response,  **kwargs):
        state_name = response.xpath(settings.STATE_SELECTOR).get()
        city_links = response.xpath(settings.CITY_LINK_SELECTOR).getall()
        for link in city_links:
            sleep(2)
            # Browse cities by state
            yield scrapy.Request(link,callback=self.parse_city,
                                 cb_kwargs={'state': state_name})
        pass

    def parse_city(self, response,**kwargs):
        school_links=response.xpath(settings.SCHOOL_LINK_SELECTOR).getall()
        location_data = response.cb_kwargs
        location_data["city"] = response.xpath(settings.CITY_SELECTOR).get()
        for link in school_links:
            sleep(2)
            # browse schools by city
            yield scrapy.Request(link, callback=self.parse_school, cb_kwargs=location_data)
        sleep(3)
        next_page = response.xpath(settings.NEXT_PAGE_LIST_OF_SCHOOLS)
        if len(next_page) > 0:
            url_next_page = next_page.get()
            if url_next_page != "#":
                sleep(2)
                # navigate through paginators
                yield scrapy.Request(url_next_page, callback=self.parse_city, cb_kwargs=response.cb_kwargs)


    def parse_school(self, response, **kwargs):
        school = response.xpath(settings.SCHOOL_SELECTOR).get()
        location_data = response.cb_kwargs
        cc_board = response.xpath(settings.COLLEGE_COUNSELING_SECTION_SELECTOR)
        if len(cc_board) == 0:
            logging.warning(f"School {school} has no information abount counseling members")
        # scrap college counseling info
        for member in cc_board:
            loader = ItemLoader(item=CounselinginfoItem(), selector=cc_board)
            loader.add_value("state_region",location_data['state'])
            loader.add_value("city",location_data['city'])
            loader.add_value('school',school.replace("\n"," - "))
            first_name, middle_name, last_name, job_title,mail, phone = Helper.tokenize(member.get())
            loader.add_value("first_name",first_name)
            loader.add_value("middle_name",middle_name)
            loader.add_value("last_name",last_name)
            loader.add_value("job_title",job_title)
            loader.add_value("mail",mail)
            loader.add_value("phone",phone)
            yield loader.load_item()


'''
Extract the following information:
First Name
Middle Name
Last Name
Email
Job Title
Any other relevant fields available in the directory
'''
