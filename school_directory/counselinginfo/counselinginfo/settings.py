# Scrapy settings for counselinginfo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "counselinginfo"

SPIDER_MODULES = ["counselinginfo.spiders"]
NEWSPIDER_MODULE = "counselinginfo.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "counselinginfo (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "counselinginfo.middlewares.CounselinginfoSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "counselinginfo.middlewares.CounselinginfoDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "counselinginfo.pipelines.CounselinginfoPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEED_EXPORT_FIELDS = [
    "state_region", "city", 'school', "first_name", "middle_name",
    "last_name", "job_title", "mail", "phone"
]
LOG_FILE = "scrapy.log"

# xpath selector for links to state/region, city and school
STATEREGION_LINK_SELECTOR = ("//div[@class='drts-col-12 drts-col-md-6 drts-col-xl-3 "
                             "drts-view-entity-container']/div/div/a/@href")
CITY_LINK_SELECTOR = "//div[@class='drts-bs-col-sm-6']/ul/li/a/@href"
SCHOOL_LINK_SELECTOR = "//div[@data-name='entity_field_post_title']/a/@href"
# link for the next page on cities which has more than 10 schools
NEXT_PAGE_LIST_OF_SCHOOLS = "//i[@class='fas fa-angle-double-right']/parent::a/@href"

# State, City or School names
STATE_SELECTOR = "//h1[@class='banner-title']/text()"
CITY_SELECTOR = "//h1[@class='banner-title']/text()"
SCHOOL_SELECTOR = "//h1[@class='banner-title']/text()"

# College counseling info
COLLEGE_COUNSELING_SECTION_SELECTOR = "//th[text()='College Counseling Info']/following-sibling::td/p"
