# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from billboard import Helper

class BillboardPipeline:
    last_song = ""
    last_artist = ""
    last_date = ""
    last_sequential = ""
    def _fill_last_song(self, adapter):
        # en. When it is the first occurrence of a song, it is saved in a variable
        # pt. Quando se trata da primeira ocorrência de uma música, é salva em uma variável
        if 'song' in adapter.keys() and adapter["song"] != "":
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

        if 'artist' in adapter.keys() and (adapter["artist"] != ""):
            self.last_artist = adapter["artist"]
        # en: when line is complete, the artist is saved for future use
        # pt: quando a linha está completa, salvo o artista para uso futoro
        else:
            adapter["artist"] = self.last_artist

    def _fill_list_sequential(self, adapter):
        # and not Helper.is_note_or_empty([adapter["date"]])
        if 'sequential_no' in adapter.keys():
                self.last_sequential = adapter["sequential_no"]
        else:
            adapter["sequential_no"] = self.last_sequential

    def _take_first(self, adapter):
        for item in adapter.keys():
            adapter[item]=adapter[item][0]

    def _treat_date(self, adapter):
        if adapter["date"]== "":
            # en. adapter["date"] is always the second cell
            # but, if the line is incomplete,the date is in the first
            # so you need to read the date from adapter
            #################################################################
            # pt. adapter["date"] é sempre a segunda célula
            # mas, se a linha está incompleta, a data está na primeira
            # daí é preciso ler a data de adapter
            adapter['date'] = adapter["sequential_no"]
            adapter["sequential_no"] = self.last_sequential
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
        self._take_first(item)
        self._fill_last_song(adapter)
        self._fill_last_artist(adapter)
        self._treat_date(adapter)
        self._fill_list_sequential(adapter)
        return item
