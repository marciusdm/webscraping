[![author](https://img.shields.io/badge/author-Marcius%20D.%20Moraes-green)](https://www.linkedin.com/in/marciusdm) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/marciusdm/portfolio/issues)

<a href="readme_en.md"> <img src="https://flagsapi.com/US/flat/32.png" alt="versão em inglês deste arquivo" /></a>

# Uma aplicação de web-scraping para coletar dados do site https://www.schooldirectory.org/
Com base em um solicitação do site Upwork para coletar dados de conselheiros escolares a partir do site [School Directory](https://www.schooldirectory.org/),
foi criado um projeto utilizando a biblioteca [Scrapy](https://scrapy.org) (Clique [aqui](https://medium.com/@marciusdellano/introdu%C3%A7%C3%A3o-ao-web-scraping-utilizando-ferramenta-scrapy-65d7a845d2a2)   para ler um artigo introdutório sobre o Scrapy). O Scrapy trabalha com o conceito de 'aranhas' que permitem analisar o código-fonte de cada página e extrair as informações desejadas usando seletores CSS ou XPath e também é possível extrair links e navegar por eles.
Primeiramente, é acessada a página inicial do site, em que há uma seção denominada "Browse by Cities" (Navegar por cidades), conforme figura abaixo:


![página inicial](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_home.png?raw=true)
Nela há uma lista de estados ou regiões (o estado da California foi dividido em duas regiões: norte e sul) , cada qual contendo um link que vai para a lista de cidades por estado. Cada um desses links  é acessado pela aranha. A lista de cidades por estado é mostrada abaixo:
![cidades por estado](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_browse_by_cities.png?raw=true)
 
A aranha, então coleta e acessa os links referentes a cada cidade, que exibem uma lista de escolas por cidade:
![Lista de escolas da cidade de Palo Alto](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_schools_by_city.png?raw=true)
Nesta etapa são coletados os links de cada escola. Esta lista exibe 10 escolas por página. Caso a cidade em questão possua mais de escolas é exibido um paginador:
![paginador](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_next_page.png?raw=true)
A aranha captura e acessa o link contido no item definido por >>. 
Após obter os links de todas as escolas, são acessadas as páginas de cada uma delas daí coletamos os dados das seção "College Counseling info,":
![seção 'college counseling info](https://github.com/marciusdm/webscraping/blob/main/assets/school_directory_college_counseling.png?raw=true)
  Aqui são extraídos, o nome, o e-mail, o cargo e  o telefone e gerado um arquivo CSV com os seguintes campos:
* state_region
* city
* school
* first_name
* middle_name
* last_name,
* job_title,
* mail
* phone

# Como executar a aplicação 
* Faça o download do [código fonte](https://github.com/marciusdm/webscraping/raw/refs/heads/main/school_directory/counselinginfo.zip) 
* Crie um ambiente virtual usando IDE python, tal como PyCharm ou VsCode; ou mesmo manualmente, usando o comando:   
  `python -m venv <caminho_para_ambiente_virtual>`  
e extraia o conteúdo do arquivo baixado para o diretório raiz do ambiente virtual
* Instale a bibliobteca Scrapy através do comando:  
 `pip install scrapy`
* navegue até o diretório counselinginfo:
   `cd counselinginfo`
* execute o comando abaixo para extrair a lista de conselheiros escolares:
  `scrapy crawl academics -o counselors.csv:csv `

A lista de conselheiros estará um um arquivo chamado `counselors.csv` na mesma pasta onde o comando acima foi executado 
