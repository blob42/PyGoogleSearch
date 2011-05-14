# Scrapy settings for PyGoogleSearch project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'PyGoogleSearch'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['PyGoogleSearch.spiders']
NEWSPIDER_MODULE = 'PyGoogleSearch.spiders'
DEFAULT_ITEM_CLASS = 'PyGoogleSearch.items.PygooglesearchItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

