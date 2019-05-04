# -*- coding: utf-8 -*-

# Scrapy settings for juren project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'juren'

SPIDER_MODULES = ['juren.spiders']
NEWSPIDER_MODULE = 'juren.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'juren (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.01
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/55.0.2883.87 Safari/537.36',
  'Cookie':'ydjn_2132_sid=Z7R9pp; ydjn_2132_saltkey=MKeL11S1; ydjn_2132_lastvisit=1556901078; ydjn_2132_sendmail=1; ydjn_2132_st_p=0%7C1556904714%7Cbcd2fc12c171de293342f8213a3ab142; ydjn_2132_seccode=19.1ef0c87d0cb954dab0; ydjn_2132_con_request_uri=http%3A%2F%2Fwww.jurensucai.com%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dhttp%253A%252F%252Fwww.jurensucai.com%252Fwz-2145-1-1.html; ydjn_2132_client_created=1556904804; ydjn_2132_client_token=E4BC862B86883742F1C5DEA28937AE23; ydjn_2132_ulastactivity=ee62TJ53xJGiFyxRla9EkpceImWHsWG6ktIzXLSvn%2FKZyd1NUTOA; ydjn_2132_auth=bb1bXfzb4SIqy%2FOx9LoHXT686RJG8Hhvovwbm28rULDEAzYMEs0oVSL6JtZDvoQ2V5EOnj72HlRkXFryw6RNWa4; ydjn_2132_connect_login=1; ydjn_2132_connect_is_bind=1; ydjn_2132_connect_uin=E4BC862B86883742F1C5DEA28937AE23; ydjn_2132_stats_qc_login=3; ydjn_2132_lastact=1556904805%09home.php%09spacecp; ydjn_2132_checkpm=1',
  'Upgrade-Insecure-Requests':'1'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'juren.middlewares.JurenSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'juren.middlewares.JurenDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'juren.pipelines.JurenPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
