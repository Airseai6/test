#! python3
# -*- coding:utf-8 -*-
from pygal_maps_world.i18n import COUNTRIES

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])


def get_country_code(country_name):
    """根据国家，返回pygal中两个字母的国家别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


# print(get_country_code('China'))
