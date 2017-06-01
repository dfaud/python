#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

tree = etree.parse("fic.xml", parser=None, base_url=None)
for user in tree.xpath("/users/user/nom"):
    print(user.text)