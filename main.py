from scrapy.cmdline import execute
import sys
import os
"""
https://nkcoder.github.io/2015/11/17/Scrapy-crawl-intro-install-and-config/
"""
print(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","hello"])