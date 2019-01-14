#! python3
# -*- coding:utf-8 -*-
import pygal.maps.world


wm = pygal.maps.world.World()
wm.title = 'North, Central and South American'
wm.add('North American',  {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.add('Central American', ['bz', 'cr', 'gt'])
wm.add('South American', ['ar', 'bo', 'br'])

wm.render_to_file('americas.svg')