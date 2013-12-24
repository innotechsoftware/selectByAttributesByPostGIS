# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AttributeSorgu
                                 A QGIS plugin
 select by attributes
                             -------------------
        begin                : 2013-06-12
        copyright            : (C) 2013 by Innotech Software
        email                : info@innotechyazilim.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Select By Attributes from Postgis Table"
def description():
    return "Select by attributes with Postgis"
def version():
    return "Version 1.0"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load AttributeSorgu class from file AttributeSorgu
    from select import AttributeQuery
    return AttributeQuery(iface)
