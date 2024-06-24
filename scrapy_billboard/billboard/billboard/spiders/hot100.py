import scrapy
from time import sleep
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join

from billboard.items import BillboardItem


class Hot100Spider(scrapy.Spider):
    name = "hot100"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2012",
 ]

    def parse(self, response,  **kwargs):
        # 3 seconds pause to avoid server overloading
        # pausa de 3 segundos para não sobrecarregar o servidor
        sleep(3)
        # en. extract the year from the page title
        # pt. extrai o o ano a partir do título da página
        year = int(response.css("h1::text").getall()[1][-4:])
        # en. The articles referring to the years below, the table with the song list in first place on Billboard
        # is third and not second on the page
        ###################################################################################################
        # pt. Os artigos referentes aos anos abaixo, a tabela com as relação de músicas em 1º lugar na Billboard
        # é a terceira e não a segunda da página
        years_with_warning = [1966, 1967, 1968, 1969, 1970, 1971, 1974, 1975, 1997]
        chart_history = response.xpath("//table[3]/tbody/tr") if year in years_with_warning \
            else response.xpath("//table[2]/tbody/tr")

        # en. ignore first line
        # pt. igrnora primeira linha
        for week_chart in chart_history[1:]:
            loader = ItemLoader(item=BillboardItem(), selector=week_chart)
            loader.add_css("sequential_no", "td:nth_child(1)")
            if year <= 2011:
                loader.add_css("date", "td:nth_child(2)", TakeFirst())
            else:
                loader.add_css("date", "th::text", TakeFirst())
            loader.add_css("song", "td:nth_child(3)", TakeFirst())
            loader.add_css("artist", "td:nth_child(4)", TakeFirst())
            loader.add_value("year", year)
            yield loader.load_item()

            if(year <2023):
                url_next_year = f"/wiki/List_of_Billboard_Hot_100_number_ones_of_{year+1}"
                url_next_year = response.urljoin(url_next_year)
                yield scrapy.Request(url_next_year, callback=self.parse)
