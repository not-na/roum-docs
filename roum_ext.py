#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  roum_ext.py
#  
#  Copyright 2019 notna <notna@apparat.org>
#  
#  This file is part of roum.
#
#  roum is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  roum is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with roum.  If not, see <http://www.gnu.org/licenses/>.

import sphinxcontrib
from sphinxcontrib.domaintools import custom_domain

# Monkeypatch for Python 3 compatibility
def get_objects(self):
        for (type, name), info in self.data['objects'].items():
            yield (name, name, type, info[0], info[1],
                   self.object_types[type].attrs['searchprio'])
sphinxcontrib.domaintools.CustomDomain.get_objects = get_objects

def setup(app):
    app.add_domain(custom_domain('roumDomain',
        name  = 'roum',
        label = "Roum",

        elements = dict(
            entity = dict(
                objname = "roum Entity",
                indextemplate = "pair: %s; roum Entity",
            ),
            event  = dict(
                objname = "roum Event",
                indextemplate = "pair: %s; roum Event",
            ),
            packet = dict(
                objname = "roum Packet",
                indextemplate = "pair: %s; roum Packet",
            ),
            dtype = dict(
                objname = "roum Data Type",
                indextemplate = "pair: %s; roum DataType",
            ),
            plugin = dict(
                objname = "roum Plugin",
                indextemplate = "pair: %s; roum Plugin",
            ),
            command = dict(
                objname = "roum Command",
                indextemplate = "pair: %s; roum Command",
            ),
            confval = dict(
                objname = "roum Config Value",
                indextemplate = "pair: %s; roum ConfigValue"
            ),
            permission = dict(
                objname = "roum Permission",
                indextemplate = "pair: %s; roum Permission"
            )
        )))
    return {"version":"1.0"}