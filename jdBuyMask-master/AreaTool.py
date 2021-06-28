# -*- coding=utf-8 -*-
from jdlogger import logger

'''
找一条第一个版本的url
'''
url = 'https://p.3.cn/prices/mgets?callback=jQuery7046778&type=1&area=19_1655_39461_0&pdtk=&pduid=277273792&pdpin=yao0013&pin=yao0013&pdbp=0&skuIds=J_100011513445%2CJ_100017153370%2CJ_1980618455%2CJ_41181339933%2CJ_47731058821%2CJ_69522895216%2CJ_28027806194%2CJ_100010343850%2CJ_100001484839%2CJ_5968860%2CJ_63488181381%2CJ_100007131001%2CJ_40357736144%2CJ_44638775908&ext=11100000&source=item-pc'
skuId = url.split('skuId=')[1].split('&')[0]
area = url.split('area=')[1].split('&')[0]
logger.info('你的area是[ %s ]，链接的商品id是[ %s ]', area, skuId)
