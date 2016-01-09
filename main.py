#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   xubigshu@gmail.com
# @site     http://www.51lu.me
# @date     2016-1-9
#

from crawler import Crawler
from sniffer import Sniffer
from etc.logger import logger


def main():
    proxyips = Crawler.run()
    logger.info('Crawler finish, total ip: %s', len(proxyips))
    sniffer = Sniffer()
    sniffer.run(proxyips)

if __name__ == "__main__":
    main()
