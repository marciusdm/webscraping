# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from billboard import Helper


# en. process_item will be invoked each time a line from songs table is processed by Scrapy
# pt. O método process_item desta classe é invocado, cda vez que o Scrapy processa uma linha
# da tabela de músicas
class BillboardPipeline:
    last_song = ""
    last_artist = ""
    last_date = ""
    last_sequential = ""

    def _fill_last_song(self, adapter):
        # en. When it is the first occurrence of a song, it is saved in a variable
        # pt. Quando se trata da primeira ocorrência de uma música, é salva em uma variável
        if 'song' in adapter.keys():
            self.last_song = adapter["song"]
        # en. when the song information is taken from the last occurrence
        # pt. quando a informação da música, pego da última ocorrência
        else:
            adapter["song"] = self.last_song

    def _fill_last_artist(self, adapter):
        #####################################################################################
        # en. on item loader, artist  was set as the fourth <td> eleent of the line.        #
        # but when line has only two cells ou when the fourth one is ref we have to retrieve#
        # the last saved artist                                                             #
        #####################################################################################
        # pt. no item loader, o artista foi definido como o quarto elemento <td> da linha   #
        # mas quando ela só possui duas células ou quando a quarta célula for uma referência#
        # então ao pego o último artista salvo                                              #

        if 'artist' in adapter.keys() and not Helper.is_note_or_empty(adapter["artist"][0]):
            print(f"artist: {adapter['artist'][0]} ")
            self.last_artist = adapter["artist"]
        # en: when line is complete, the artist is saved for future use
        # pt: quando a linha está completa, salvo o artista para uso futoro
        else:
            adapter["artist"] = self.last_artist

    def _treat_date_and_sequential(self, adapter):
        # en. eliminates HTML tags and quotes
        # the load_xxx methods always return a list, even when only
        #  one element is returned, but then I only get the first item from the list
        ##############################################################################
        # pt. elimina as tags HTML e aspas
        # os métodos load_xxx sempre retornam uma lista, mesmo quando apenas
        # um elemento é retornado, mas aí eu pego somente o primeiro item da lista
        adapter["date"] = Helper.strip_html_and_quotes(adapter["date"][0])
        if 'sequential_no' in adapter.keys():
            adapter["sequential_no"] = Helper.strip_html_and_quotes(
                adapter["sequential_no"][0])
        if Helper.is_note_or_empty(adapter["date"]):
            # en. adapter["date"] is always the second cell
            # but, if the line is incomplete,the date is in the first
            # so you need to read the date from adapter
            #################################################################
            # pt. adapter["date"] é sempre a segunda célula
            # mas, se a linha está incompleta, a data está na primeira
            # daí é preciso ler a data de adapter
            adapter['date'] = adapter["sequential_no"]
            adapter["sequential_no"] = self.last_sequential
        elif 'sequential_no' in adapter.keys():
            # en. store the current value of the sequential number ...
            # pt. armazeno o valor atual do número sequencial ...
            self.last_sequential = adapter["sequential_no"]
        else:
            # en ... to return it when the information is missing.This occurs from 2012
            # pt ... para retorná-lo, quando a informação estiver ausente.
            # Isto ocorre a partir de 2012
            adapter["sequential_no"] = self.last_sequential
        adapter["sequential_no"] = adapter["sequential_no"]

    def _treat_artist_and_song(self, adapter):
        # en. HTML tags, quotation marks and the character † present when
        # the song is 'song of the year' are stripped off
        #########################################################################
        # pt. elimina-se as tags HTML e aspas, e o caracter † presente quando
        # a música é a 'música do ano'
        adapter["song"] = Helper.strip_html_and_quotes(adapter["song"][0])
        adapter["song"] = Helper.strip_song_of_the_year_mark(adapter["song"])
        adapter["artist"] = Helper.strip_html_and_quotes(adapter["artist"][0])

    # en. converts an English date to dd/mm/yyyy format. The year is read from adapter["year"]
    # e.g.: February 18 to 18/02
    ##################################################################################
    # pt. converte uma data em inglês para formato dd/mm/aaaa. O ano é lido de adapter["year"]
    # ex: February 18 para 18/02
    def _convert_date(self, adapter):
        adapter["date"] = Helper.convert_english_date(adapter["date"], adapter["year"])

    # en. For each line read, an item object is passed to the 'process_item
    # which, when encapsulated by the ItemAdapter, has the following data:
    # adapter["sequential_no"]: first cell
    # adapter["date"]: second cell
    # adapter["song"]: third cell
    # adapter["artist"]: fourth cell
    # adapter["year"]: read directly from a variable in the spider's 'parse' method
    #####################################################################################
    # pt. Para cada linha lida, é passado um objeto item para o 'process_item
    # que ao ser encapsulado pelo ItemAdapter possui os seguintes dados:
    # adapter["sequential_no"]: primeira célula
    # adapter["date"]: segunda célula
    # adapter["song"]: terceira célula
    # adapter["artist"]: quarta célula
    # adapter["year"]: lido diretamente de uma variável no método 'parse' do spider
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter["year"] = adapter["year"][0]
        self._fill_last_song(adapter)
        self._fill_last_artist(adapter)
        self._treat_artist_and_song(adapter)
        self._treat_date_and_sequential(adapter)
        self._convert_date(adapter)
        return item
