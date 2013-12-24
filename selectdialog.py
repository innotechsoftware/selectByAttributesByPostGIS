# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AttributeSorguDialog
                                 A QGIS plugin
 select by attributes
                             -------------------
        begin                : 2013-02-11
        copyright            : (C) 2013 by Innotech
        email                : info@innotechyazilim.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_select import Ui_AttributeQuery
import qgis
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import O_utils
import random
from PyQt4.QtSql import *
import psycopg2
import sys
from PyQt4.Qt import *

# create the dialog for zoom to point
class AttributeQueryDialog(QtGui.QDialog):
    query = ""
    def __init__(self, iface):
        
        QtGui.QDialog.__init__(self, iface.mainWindow()) 
        # Set up the user interface from Designer.
        self.iface = iface
        
        self.ui = Ui_AttributeQuery()
        self.ui.setupUi(self)

        layers = qgis.utils.iface.legendInterface().layers()
        #katman isimlerini listeleyen kısım
        for layer in layers:
            self.ui.Vlist.addItem(layer.name())

        Vname = self.ui.Vlist.currentText()
        layer = O_utils.getVectorLayerByName(Vname)
        
        #katmandaki öznitelik alanlarını listeleyen kısım
        if self.ui.Vlist.currentText() != "":
            for index, field in layer.dataProvider().fields().iteritems():
                self.ui.Flist.addItem(field.name())
                self.ui.jFlist.addItem(field.name())
                
        settings = QSettings()
        settings.beginGroup("PostgreSQL/connections")
        self.ui.Datalist.addItems(settings.childGroups())
        settings.endGroup()
        
        list_tbl = [] #veritabanı tablı isimleri
        # veritabanındaki tablo isimlerini listeleyen kısım
        if self.ui.Datalist.currentText() != " ":
            mysetting = self.ui.Datalist.currentText()
            mySettings = "/PostgreSQL/connections/" + mysetting 
            db = QSqlDatabase.addDatabase("QPSQL")
            db.setHostName(settings.value(mySettings+"/host").toString())
            db.setDatabaseName(settings.value(mySettings+"/database").toString())
            db.setUserName(settings.value(mySettings+"/username").toString())
            db.setPassword(settings.value(mySettings+"/password").toString())
            db.open()
               
            model = QSqlQueryModel()
            model.setQuery("SELECT TABLE_NAME FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema = 'public' ")
            for i in range(model.rowCount()):
                list_tbl.append(model.record(i).value(0).toString())
            self.ui.DataTlist.addItems(list_tbl)
            db.close()
            
        list_clmn = [] #veritabanındaki tablonun nitelikleri
        # veritabanındaki tablonun nitelikleri listeleyen kısım
        if self.ui.DataTlist.currentText() != " ":
            mysetting = self.ui.Datalist.currentText()
            mySettings = "/PostgreSQL/connections/" + mysetting 
            db = QSqlDatabase.addDatabase("QPSQL")
            db.setHostName(settings.value(mySettings+"/host").toString())
            db.setDatabaseName(settings.value(mySettings+"/database").toString())
            db.setUserName(settings.value(mySettings+"/username").toString())
            db.setPassword(settings.value(mySettings+"/password").toString())
            db.open()
               
            model = QSqlQueryModel()
            model.setQuery("select column_name from information_schema.columns where TABLE_NAME = '"+self.ui.DataTlist.currentText()+"'")
            for i in range(model.rowCount()):
                list_clmn.append(model.record(i).value(0).toString())
            self.ui.jAttlist.addItems(list_clmn)
            db.close()
        
        self.ui.Flist.setCurrentRow(0)
        self.ui.jAttlist.setCurrentRow(0)
        self.ui.jFlist.setCurrentRow(0)
        
        QObject.connect(self.ui.Vlist, SIGNAL("currentIndexChanged(QString)"), self.Vchanged)
        QObject.connect(self.ui.DataTlist, SIGNAL("currentIndexChanged(QString)"), self.JAttchanged)
        QObject.connect(self.ui.Datalist, SIGNAL("currentIndexChanged(QString)"), self.DTchanged)
        QObject.connect(self.ui.Flist, SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.Fdblclick)
        QObject.connect(self.ui.Attlist, SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.AttClick)
        QObject.connect(self.ui.jAttlist, SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.jAttClick)
        QObject.connect(self.ui.DataTNlist, SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.VTclick)
        QtCore.QObject.connect( self.ui.btncln, QtCore.SIGNAL( "clicked()" ), self.docln )
        QtCore.QObject.connect( self.ui.btnSorgu, QtCore.SIGNAL( "clicked()" ), self.doSelect )
        QtCore.QObject.connect( self.ui.btndgr, QtCore.SIGNAL( "clicked()" ), self.doSample)
        QtCore.QObject.connect( self.ui.btnjoin, QtCore.SIGNAL( "clicked()" ), self.dojoin)
        QtCore.QObject.connect( self.ui.btnVdgr, QtCore.SIGNAL( "clicked()" ), self.doVSample)
        #isletmenler
        QtCore.QObject.connect( self.ui.btnesit, QtCore.SIGNAL( "clicked()" ), self.doesit)
        QtCore.QObject.connect( self.ui.btnkck, QtCore.SIGNAL( "clicked()" ), self.dokck)
        QtCore.QObject.connect( self.ui.btnbyk, QtCore.SIGNAL( "clicked()" ), self.dobyk)
        QtCore.QObject.connect( self.ui.btnkckesit, QtCore.SIGNAL( "clicked()" ), self.dokckesit)
        QtCore.QObject.connect( self.ui.btnbykesit, QtCore.SIGNAL( "clicked()" ), self.dobykesit)
        QtCore.QObject.connect( self.ui.btnntesit, QtCore.SIGNAL( "clicked()" ), self.dontesit)
        QtCore.QObject.connect( self.ui.btnlike, QtCore.SIGNAL( "clicked()" ), self.dolike)
        QtCore.QObject.connect( self.ui.btnyzd, QtCore.SIGNAL( "clicked()" ), self.doyzd)
        QtCore.QObject.connect( self.ui.btnin, QtCore.SIGNAL( "clicked()" ), self.doin)
        QtCore.QObject.connect( self.ui.btnntin, QtCore.SIGNAL( "clicked()" ), self.dontin)
        QtCore.QObject.connect( self.ui.btnand, QtCore.SIGNAL( "clicked()" ), self.doand)
        QtCore.QObject.connect( self.ui.btnor, QtCore.SIGNAL( "clicked()" ), self.do_or)

        
    def dojoin(self):
        global query
        
        if self.ui.chckjoin.isChecked():
            query = ' "' + self.ui.DataTlist.currentText() +'".'+self.ui.jAttlist.currentItem().text()+ '="'+self.ui.Vlist.currentText()+'".'+self.ui.jFlist.currentItem().text() + " AND "
        else:
            QMessageBox.information(None, "Cancel", "Join Kismini Aktiflestiriniz.")
                
    # seçili veri bağlantısı değiştiğinde çalışan kısım
    def DTchanged(self):
        self.ui.DataTlist.clear()
        settings = QSettings()
        if self.ui.Datalist.currentText() != " ":
            mysetting = self.ui.Datalist.currentText()
            mySettings = "/PostgreSQL/connections/" + mysetting 
            db = QSqlDatabase.addDatabase("QPSQL")
            db.setHostName(settings.value(mySettings+"/host").toString())
            db.setDatabaseName(settings.value(mySettings+"/database").toString())
            db.setUserName(settings.value(mySettings+"/username").toString())
            db.setPassword(settings.value(mySettings+"/password").toString())
            db.open()
            
            list_tbl = []
            model = QSqlQueryModel()
            model.setQuery("SELECT TABLE_NAME FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema = 'public' ")
            for i in range(model.rowCount()):
                list_tbl.append(model.record(i).value(0).toString())
            self.ui.DataTlist.addItems(list_tbl)
            db.close()
            
    # seçili veritabanı tablosu değiştiğinde çalışan ksım
    def JAttchanged(self):
        self.ui.jAttlist.clear()
        settings = QSettings()
        mysetting = self.ui.Datalist.currentText()
        mySettings = "/PostgreSQL/connections/" + mysetting 
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName(settings.value(mySettings+"/host").toString())
        db.setDatabaseName(settings.value(mySettings+"/database").toString())
        db.setUserName(settings.value(mySettings+"/username").toString())
        db.setPassword(settings.value(mySettings+"/password").toString())
        db.open()
        
        list_clmn = [] #veritabanındaki tablonun nitelikleri
        
        model = QSqlQueryModel()
        model.setQuery("select column_name from information_schema.columns where TABLE_NAME = '"+self.ui.DataTlist.currentText()+"'")
        for i in range(model.rowCount()):
                list_clmn.append(model.record(i).value(0).toString())
        self.ui.jAttlist.addItems(list_clmn)
        db.close()

    #secili katman değişinde çalışan kısım
    def Vchanged(self):
        Vname = self.ui.Vlist.currentText()
        layer = O_utils.getVectorLayerByName(Vname)
        self.ui.Flist.clear()
        self.ui.jFlist.clear()
        
        for index, field in layer.dataProvider().fields().iteritems():
            self.ui.Flist.addItem(field.name())
            self.ui.jFlist.addItem(field.name())
            
    #katmanın özniteliklerine çift tıklandıgında çalışan kısım
    def Fdblclick(self):
        Vname = self.ui.Flist.currentItem().text()
        self.ui.txtbox_1.insertPlainText('"'+self.ui.Flist.currentItem().text()+'" ')
            
    #sorgula butonu    
    def doSelect(self):

        if self.ui.chckjoin.isChecked():
            mysetting = self.ui.Datalist.currentText()
            settings = QSettings()
            mySettings = "/PostgreSQL/connections/" + mysetting 
            db = QSqlDatabase.addDatabase("QPSQL")
            db.setHostName(settings.value(mySettings+"/host").toString())
            db.setDatabaseName(settings.value(mySettings+"/database").toString())
            db.setUserName(settings.value(mySettings+"/username").toString())
            db.setPassword(settings.value(mySettings+"/password").toString())
            db.open()
               
            model = QSqlQueryModel()
            model.setQuery('select * from "'+self.ui.Vlist.currentText()+'","'+self.ui.DataTlist.currentText()+'" where '+query+'' + self.ui.txtbox_1.toPlainText())
            self.ui.tblview.setModel(model)
            self.ui.tblview.show()
            db.close()

            Vname = self.ui.Vlist.currentText()
            layer = O_utils.getVectorLayerByName(Vname)
            provider = layer.dataProvider()
            attrs = provider.attributeIndexes()
            provider.select(attrs)
            feat = QgsFeature()
        
            liste = []

            while provider.nextFeature(feat):
                map = feat.attributeMap()
                for i in range(model.rowCount()):
                    if map[provider.fieldNameIndex(model.headerData(0, Qt.Horizontal).toString())] == model.record(i).value(0).toString():
                        liste.append(feat.id())
              
            layer.setSelectedFeatures(liste)
        else:
            mysetting = self.ui.Datalist.currentText()
            settings = QSettings()
            mySettings = "/PostgreSQL/connections/" + mysetting 
            db = QSqlDatabase.addDatabase("QPSQL")
            db.setHostName(settings.value(mySettings+"/host").toString())
            db.setDatabaseName(settings.value(mySettings+"/database").toString())
            db.setUserName(settings.value(mySettings+"/username").toString())
            db.setPassword(settings.value(mySettings+"/password").toString())
            db.open()
               
            model = QSqlQueryModel()
            model.setQuery('select * from "'+self.ui.Vlist.currentText()+'" where ' + self.ui.txtbox_1.toPlainText())
            self.ui.tblview.setModel(model)
            self.ui.tblview.show()
            db.close()

            Vname = self.ui.Vlist.currentText()
            layer = O_utils.getVectorLayerByName(Vname)
            provider = layer.dataProvider()
            attrs = provider.attributeIndexes()
            provider.select(attrs)
            feat = QgsFeature()
        
            liste = []

            while provider.nextFeature(feat):
                map = feat.attributeMap()
                for i in range(model.rowCount()):
                    if map[provider.fieldNameIndex(model.headerData(0, Qt.Horizontal).toString())] == model.record(i).value(0).toString():
                        liste.append(feat.id())
              
            layer.setSelectedFeatures(liste)
        
    #seçili katman niteliklerinin değerlerini getiren kısım    
    def doSample(self):
        self.ui.Attlist.clear()
        Vname = self.ui.Vlist.currentText()
        layer = O_utils.getVectorLayerByName(Vname)
        provider = layer.dataProvider()
        attrs = provider.attributeIndexes()
        provider.select(attrs)
        feat = QgsFeature()

        while provider.nextFeature(feat):
            map = feat.attributeMap()
            self.ui.Attlist.addItem(map[provider.fieldNameIndex(self.ui.Flist.currentItem().text())].toString())

    #Veritabanı Nitelik örnek değerleri
    def doVSample(self):
        self.ui.DataTNlist.clear()
        settings = QSettings()
        mysetting = self.ui.Datalist.currentText()
        mySettings = "/PostgreSQL/connections/" + mysetting 
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName(settings.value(mySettings+"/host").toString())
        db.setDatabaseName(settings.value(mySettings+"/database").toString())
        db.setUserName(settings.value(mySettings+"/username").toString())
        db.setPassword(settings.value(mySettings+"/password").toString())
        db.open()
        
        list_clmn = [] #veritabanındaki tablonun nitelikleri
        
        model = QSqlQueryModel()
        model.setQuery('select '+self.ui.jAttlist.currentItem().text()+' from "'+self.ui.DataTlist.currentText()+'"')
        for i in range(model.rowCount()):
            list_clmn.append(model.record(i).value(0).toString())
        self.ui.DataTNlist.addItems(list_clmn)
        db.close()
        
    #örnek değerlere çift tıklandıgında çalışan kısım
    def AttClick(self):

        Vname = self.ui.Vlist.currentText()
        layer = O_utils.getVectorLayerByName(Vname)
        provider = layer.dataProvider()

        for index, field in layer.dataProvider().fields().iteritems():
                if field.name() == self.ui.Flist.currentItem().text():
                    if field.typeName() == "Integer":
                        self.ui.txtbox_1.insertPlainText(self.ui.Attlist.currentItem().text())
                    else:
                        self.ui.txtbox_1.insertPlainText(" '"+self.ui.Attlist.currentItem().text()+"'")

    #veritabanı gelen örnek değerler                
    def VTclick(self):
        settings = QSettings()
        mysetting = self.ui.Datalist.currentText()
        mySettings = "/PostgreSQL/connections/" + mysetting 
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName(settings.value(mySettings+"/host").toString())
        db.setDatabaseName(settings.value(mySettings+"/database").toString())
        db.setUserName(settings.value(mySettings+"/username").toString())
        db.setPassword(settings.value(mySettings+"/password").toString())
        db.open()
        
        model = QSqlQueryModel()
        model.setQuery("select data_type from information_schema.columns where TABLE_NAME = '"+self.ui.DataTlist.currentText()+"' and column_name ='"+self.ui.jAttlist.currentItem().text()+"'")
        
        if model.record(0).value(0).toString() == "integer":
            self.ui.txtbox_1.insertPlainText(self.ui.DataTNlist.currentItem().text()+ " ")
        else:
            self.ui.txtbox_1.insertPlainText("'"+self.ui.DataTNlist.currentItem().text()+"' ")
            
    #veritabanı Tablo niteliğine çift tıklama
    def jAttClick(self):
        self.ui.txtbox_1.insertPlainText('"'+self.ui.jAttlist.currentItem().text()+'" ')
        
    def doesit(self):
        self.ui.txtbox_1.insertPlainText("= ")
    def dokck(self):
        self.ui.txtbox_1.insertPlainText("< ")
    def dobyk(self):
        self.ui.txtbox_1.insertPlainText("> ")
    def dokckesit(self):
        self.ui.txtbox_1.insertPlainText("<= ")
    def dobykesit(self):
        self.ui.txtbox_1.insertPlainText(">= ")
    def dontesit(self):
        self.ui.txtbox_1.insertPlainText("!= ")
    def dolike(self):
        self.ui.txtbox_1.insertPlainText("LIKE ")
    def doyzd(self):
        self.ui.txtbox_1.insertPlainText("% ")
    def doin(self):
        self.ui.txtbox_1.insertPlainText("IN ")
    def dontin(self):
        self.ui.txtbox_1.insertPlainText("NOT IN ")
    def doand(self):
        self.ui.txtbox_1.insertPlainText("AND ")
    def do_or(self):
        self.ui.txtbox_1.insertPlainText("OR ")
    def docln(self):
        self.ui.txtbox_1.clear()
        self.ui.Attlist.clear()
        self.ui.DataTNlist.clear()
