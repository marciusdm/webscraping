[![author](https://img.shields.io/badge/author-Marcius%20D.%20Moraes-green)](https://www.linkedin.com/in/marciusdm) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/marciusdm/portfolio/issues)

<a href="readme_en.md"> <img src="https://flagsapi.com/US/flat/32.png" alt="versão em inglês deste arquivo" /></a>

# Uma aplicação de web-scraping para coletar lista de processadores móveis a partir do site [NanoReview](https://nanoreview.net/en/soc-list/rating)
O site NanoReview é um site que mostra rankings e comparativos de  processadores, tanto de dispositivos móveis quanto de PC's,  além de laptops e smartphones. 
Aqui por exemplo, temos uma lista de processadores de celular em ordem decrescente de pontuação dada pelo próprio Nanoreview com base nos atributos do processador e em alguns benchmarks tais como Antutu e 3D-Mark:

![NanoReview mobile processor home](https://raw.githubusercontent.com/marciusdm/webscraping/refs/heads/main/assets/nanoreview/NanoReviewHome.png)
É uma lista bastante interessante, mas eu senti falta de um formulário que permitisse listar somente os processadores mais recentes, ou filtrar por marca e categoria (flagship, intermediário e entrada ). Isto é o que me motivou a criar esta aplicação, que integra a biblioteca [Scrapy](https://scrapy.org) com o framework [Django](https://www.djangoproject.com).
Ao abrir o aplicativo pela primeira vez, é mostrada uma página vazia apenas com um botão rotulado "Carregar lista de processadores", que ao ser clicado ativa um script Scrapy que percorre o site NanoReview e coleta  os dados dos processadores contidos no site e os armazena em uma base de dados SQLite , que é a base de dados padrão utilizada pelo Django. Após esta operação é exibida uma tabela de processadores como esta:

![app home page](https://raw.githubusercontent.com/marciusdm/webscraping/refs/heads/main/assets/nanoreview/PaginaInicial.png "Home-page da aplicação")
Esta tabela, criada através do componente [django-tables2](https://django-tables2.readthedocs.io/en/latest/) permite ordenar os dados ao clicar no cabeçalho da coluna desejada, além de paginar os dados exibindo 10 itens por página.
Ao clicar em "Definir Filtros" um formulário se expande permitindo filtrar processadores por pontuação no Antutu, por categoria, por fabricante e por data de lançamento:
![Filtro](https://raw.githubusercontent.com/marciusdm/webscraping/refs/heads/main/assets/nanoreview/Filtro.png "Filtro")
Ao clicar em um processador qualquer na coluna "Modelo" é aberta uma página que exibe detalhes adicionais do processador, tal como no site original, porém com menos informações. Ao final da página de detalhes é exibido um link que vai para a página de detalhes do processador no site NanoReview. Segue abaixo a página de detalhes:

![Página de detalhes](https://raw.githubusercontent.com/marciusdm/webscraping/refs/heads/main/assets/nanoreview/Detalhes.png "Detalhes do processador")

# Como construir e executar este aplicativo
Para construir e executar este aplicativo, baixe o [código fonte](https://github.com/marciusdm/webscraping/raw/refs/heads/main/nanoreview-django/processorsrankingpage.zip) e siga os passos abaixo:
* Crie um projeto Python usando um editor IDE como PyCharm ou VsCode ou crie manualmente um ambiente virtual usando o comando abaixo:<br>
 `python -m venv C:\path\to\new\virtual\environment` (Windows)<br>
 ou<br>
 `python  -m  venv  /path/to/new/virtual/environment` (Linux or MacOs)
* Extraia o conteúdo do arquivo zip para o diretório raiz do projeto ou ambiente virtual
* Abra um terminal e execute o comando abaixo para instalar todos as bibliotecas requerids p/ o funcionamento do aplicativo:<br>
  `pip install -r requirements.txt`
  
    Este comando irá instalar todos os pacotes necessários para executar a aplicação:
	* [scrapy](https://scrapy.org) 
	* [django](https://www.djangoproject.com)
	* [django-filter](https://django-filter.readthedocs.io/en/stable/)
	* [django-tables2](https://django-tables2.readthedocs.io/en/latest/#)
	* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
	* [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) 
*  navegue até a pasta ‘processorsrankingpage’:<br>
	`cd processorsrankingpage`   
* Inicie a aplicação:<br>
 `python manage.py runserver`
* Abra um navegador da web no seguinte endereço:<br>
  http://127.0.0.1:8000/mobile_processors/
* Aproveite!
