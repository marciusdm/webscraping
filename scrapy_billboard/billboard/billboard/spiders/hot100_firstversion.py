import scrapy
from time import sleep
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join

from billboard.items import BillboardItem


class Hot100Spider_old(scrapy.Spider):
    name = "hot100old"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1959",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1960",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1961",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1962",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1963",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1964",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1965",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1966",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1967",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1968",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1969",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1970",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1971",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1972",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1973",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1974",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1975",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1976",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1977",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1978",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1979",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1980",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1981",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1982",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1983",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1984",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1985",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1986",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1987",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1988",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1989",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1990",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1991",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1992",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1993",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1994",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1995",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1996",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1997",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1998",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1999",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2000",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2001",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2002",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2003",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2004",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2005",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2006",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2007",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2008",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2009",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2010",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2011",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2012",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2013",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2014",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2015",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2016",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2017",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2018",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2019",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2020",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2021",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2022",
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2023"    ]

    def parse(self, response):
        sleep(3)
        year = int(response.css("h1::text").getall()[1][-4:])
        # Os artigos referentes aos anos, a tabela com as relação de músicas em 1º lugar na Billboard
        # é a terceira e não a segunda da página
        years_with_warning = [1966, 1967, 1968, 1969, 1970, 1971, 1974, 1975, 1997]
        chart_history = response.xpath("//table[3]/tbody/tr") if year in years_with_warning \
            else response.xpath("//table[2]/tbody/tr")

        # ignore first line
        for week_chart in chart_history[1:]:
            loader = ItemLoader(item=BillboardItem(), selector=week_chart)
            loader.add_css("sequential_no", "td:nth_child(1)::text")
            if year <= 2011:
                loader.add_css("date", "td:nth_child(2)", TakeFirst())
            else:
                loader.add_css("date", "th::text", TakeFirst())
            loader.add_css("song", "td:nth_child(3)", TakeFirst())
            loader.add_css("artist", "td:nth_child(4)", TakeFirst())
            loader.add_value("year", year)
            yield loader.load_item()
