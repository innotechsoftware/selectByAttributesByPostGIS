# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_select.ui'
#
# Created: Mon Feb 11 10:22:18 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AttributeQuery(object):
    def setupUi(self, select):
        select.setObjectName(_fromUtf8("select"))
        select.resize(1200, 700)
        
        self.HLayout = QtGui.QHBoxLayout(select)
        self.HLayout.setObjectName(_fromUtf8("HLayout"))
        
        # layer kısmının ui elemanları
        self.horizontalGroupBox = QtGui.QGroupBox(select)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        
        self.gridLayout = QtGui.QGridLayout(self.horizontalGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.label = QtGui.QLabel(select)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        
        self.Vlist = QtGui.QComboBox(select)
        self.Vlist.setObjectName(_fromUtf8("self.Vlist"))
        self.gridLayout.addWidget(self.Vlist, 1, 0, 1, 2)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.label_3 = QtGui.QLabel(select)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.hboxlayout1.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(select)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.hboxlayout1.addWidget(self.label_4)
        self.gridLayout.addLayout(self.hboxlayout1, 2, 0, 1, 2)
        
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.Flist = QtGui.QListWidget(select)
        self.Flist.setObjectName(_fromUtf8("self.Flist"))
        self.hboxlayout.addWidget(self.Flist)
        self.Attlist = QtGui.QListWidget(select)
        self.Attlist.setObjectName(_fromUtf8("self.Attlist"))
        self.hboxlayout.addWidget(self.Attlist)
        self.gridLayout.addLayout(self.hboxlayout, 3, 0, 1, 2)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.label_1 = QtGui.QLabel(select)                                     
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.hboxlayout2.addWidget(self.label_1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem)
        self.btndgr = QtGui.QPushButton(select)
        self.btndgr.setObjectName(_fromUtf8("btndgr"))
        self.hboxlayout2.addWidget(self.btndgr)
        self.gridLayout.addLayout(self.hboxlayout2, 4, 0, 1, 2)
        
        #İŞLETMEN BUTONLARI
        self.hboxlayoutist = QtGui.QHBoxLayout()
        self.hboxlayoutist.setObjectName(_fromUtf8("hboxlayoutist"))
                                     
        self.btnesit = QtGui.QPushButton(select)
        self.btnesit.setObjectName(_fromUtf8("btnesit"))
        self.hboxlayoutist.addWidget(self.btnesit)
        
        self.btnkck = QtGui.QPushButton(select)
        self.btnkck.setObjectName(_fromUtf8("btnkck"))
        self.hboxlayoutist.addWidget(self.btnkck)
        
        self.btnbyk = QtGui.QPushButton(select)
        self.btnbyk.setObjectName(_fromUtf8("btnbyk"))
        self.hboxlayoutist.addWidget(self.btnbyk)
        
        self.btnlike = QtGui.QPushButton(select)
        self.btnlike.setObjectName(_fromUtf8("btnlike"))
        self.hboxlayoutist.addWidget(self.btnlike)
        
        self.btnyzd = QtGui.QPushButton(select)
        self.btnyzd.setObjectName(_fromUtf8("btnyzd"))
        self.hboxlayoutist.addWidget(self.btnyzd)

        self.btnin = QtGui.QPushButton(select)
        self.btnin.setObjectName(_fromUtf8("btnin"))
        self.hboxlayoutist.addWidget(self.btnin)

        self.gridLayout.addLayout(self.hboxlayoutist, 5, 0, 1, 2)

        self.hboxlayoutist1 = QtGui.QHBoxLayout()
        self.hboxlayoutist1.setObjectName(_fromUtf8("hboxlayoutist1"))

        self.btnkckesit = QtGui.QPushButton(select)
        self.btnkckesit.setObjectName(_fromUtf8("btnkckesit"))
        self.hboxlayoutist1.addWidget(self.btnkckesit)

        self.btnbykesit = QtGui.QPushButton(select)
        self.btnbykesit.setObjectName(_fromUtf8("btnbykesit"))
        self.hboxlayoutist1.addWidget(self.btnbykesit)
        
        self.btnntesit = QtGui.QPushButton(select)
        self.btnntesit.setObjectName(_fromUtf8("btnntesit"))
        self.hboxlayoutist1.addWidget(self.btnntesit)

        self.btnand = QtGui.QPushButton(select)
        self.btnand.setObjectName(_fromUtf8("btnand"))
        self.hboxlayoutist1.addWidget(self.btnand)

        self.btnor = QtGui.QPushButton(select)
        self.btnor.setObjectName(_fromUtf8("btnor"))
        self.hboxlayoutist1.addWidget(self.btnor)
        
        self.btnntin = QtGui.QPushButton(select)
        self.btnntin.setObjectName(_fromUtf8("btnntin"))
        self.hboxlayoutist1.addWidget(self.btnntin)
        
        self.gridLayout.addLayout(self.hboxlayoutist1, 6, 0, 1, 2)
        #işletmenler bitiş
        
        self.label_5 = QtGui.QLabel(select)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 2)

        self.tblview = QtGui.QTableView(select)
        self.tblview.setObjectName(_fromUtf8("tblview"))
        self.gridLayout.addWidget(self.tblview, 8, 0, 1, 2)
        
        self.label_2 = QtGui.QLabel(select)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 2)
        
        self.txtbox_1 = QtGui.QTextEdit(select)
        self.txtbox_1.setObjectName(_fromUtf8("txtbox_1"))
        self.gridLayout.addWidget(self.txtbox_1, 10, 0, 1, 2)
        
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        
        self.btnSorgu = QtGui.QPushButton(select)
        self.btnSorgu.setObjectName(_fromUtf8("btnSorgu"))
        self.hboxlayout.addWidget(self.btnSorgu)
        
        self.btncln = QtGui.QPushButton(select)
        self.btncln.setObjectName(_fromUtf8("btncln"))
        self.hboxlayout.addWidget(self.btncln)

        self.btncancel = QtGui.QPushButton(select)
        self.btncancel.setObjectName(_fromUtf8("btncancel"))
        self.hboxlayout.addWidget(self.btncancel)

        self.gridLayout.addLayout(self.hboxlayout, 11, 0, 1, 2)
        self.HLayout.addWidget(self.horizontalGroupBox)

        QtCore.QObject.connect(self.btncancel, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), select.reject)
        
        #layer kısmının bitiş yeri

        #Join kısmı Başlangıç
        self.horizontalGroupBox1 = QtGui.QGroupBox(select)
        self.horizontalGroupBox1.setObjectName(_fromUtf8("horizontalGroupBox1"))
        
        self.gridLayoutj = QtGui.QGridLayout(self.horizontalGroupBox1)
        self.gridLayoutj.setObjectName(_fromUtf8("gridLayoutj"))

        self.chckjoin = QtGui.QCheckBox(select)
        self.chckjoin.setObjectName(_fromUtf8("chckjoin"))
        self.gridLayoutj.addWidget(self.chckjoin, 0, 0, 1, 2)
        
        self.jlabel = QtGui.QLabel(select)
        self.jlabel.setObjectName(_fromUtf8("jlabel"))
        self.gridLayoutj.addWidget(self.jlabel, 1, 0, 1, 2)
        
        self.Datalist = QtGui.QComboBox(select)
        self.Datalist.setObjectName(_fromUtf8("self.Datalist"))
        self.gridLayoutj.addWidget(self.Datalist, 2, 0, 1, 2)

        self.jlabel1 = QtGui.QLabel(select)
        self.jlabel1.setObjectName(_fromUtf8("jlabel1"))
        self.gridLayoutj.addWidget(self.jlabel1, 3, 0, 1, 2)
        
        self.DataTlist = QtGui.QComboBox(select)
        self.DataTlist.setObjectName(_fromUtf8("self.DataTlist"))
        self.gridLayoutj.addWidget(self.DataTlist, 4, 0, 1, 2)
        
        self.jhboxlayout = QtGui.QHBoxLayout()
        self.jhboxlayout.setObjectName(_fromUtf8("jhboxlayout"))
        
        self.jlabel3 = QtGui.QLabel(select)
        self.jlabel3.setObjectName(_fromUtf8("jlabel3"))
        self.jhboxlayout.addWidget(self.jlabel3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.jhboxlayout.addItem(spacerItem)
        self.jlabel2 = QtGui.QLabel(select)
        self.jlabel2.setObjectName(_fromUtf8("jlabel2"))
        self.jhboxlayout.addWidget(self.jlabel2)
        self.gridLayoutj.addLayout(self.jhboxlayout, 5, 0, 1, 2)
        
        self.jhboxlayout1 = QtGui.QHBoxLayout()
        self.jhboxlayout1.setObjectName(_fromUtf8("jhboxlayout1"))

        self.jFlist = QtGui.QListWidget(select)
        self.jFlist.setObjectName(_fromUtf8("self.jFlist"))
        self.jhboxlayout1.addWidget(self.jFlist)
        
        self.jAttlist = QtGui.QListWidget(select)
        self.jAttlist.setObjectName(_fromUtf8("self.jAttlist"))
        self.jhboxlayout1.addWidget(self.jAttlist)
        self.gridLayoutj.addLayout(self.jhboxlayout1, 6, 0, 1, 2)

        self.jlabel4 = QtGui.QLabel(select)
        self.jlabel4.setObjectName(_fromUtf8("jlabel4"))
        self.gridLayoutj.addWidget(self.jlabel4, 7, 0, 1, 2)
        
        self.DataTNlist = QtGui.QListWidget(select)
        self.DataTNlist.setObjectName(_fromUtf8("self.DataTNlist"))
        self.gridLayoutj.addWidget(self.DataTNlist, 8, 0, 1, 2)

        self.btnVdgr = QtGui.QPushButton(select)
        self.btnVdgr.setObjectName(_fromUtf8("btnVdgr"))
        self.gridLayoutj.addWidget(self.btnVdgr, 9, 0, 1, 2)

        self.btnjoin = QtGui.QPushButton(select)
        self.btnjoin.setObjectName(_fromUtf8("btnjoin"))
        self.gridLayoutj.addWidget(self.btnjoin, 10, 0, 1, 2)
        
        self.HLayout.addWidget(self.horizontalGroupBox1)
        
        self.retranslateUi(select)
        QtCore.QMetaObject.connectSlotsByName(select)

    def retranslateUi(self, select):
        select.setWindowTitle(QtGui.QApplication.translate("select", "Select by Attributes with POSTGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalGroupBox.setTitle(QtGui.QApplication.translate("select", "Select by Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalGroupBox1.setTitle(QtGui.QApplication.translate("select", "Join Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("select", "Input Layer:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("select", "Operators :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("select", "SQL Query :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("select", "Attributes :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("select", "Samples :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("select", "Results :", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSorgu.setText(QtGui.QApplication.translate("select", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btncln.setText(QtGui.QApplication.translate("select", "Clean", None, QtGui.QApplication.UnicodeUTF8))
        self.btncancel.setText(QtGui.QApplication.translate("select", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btndgr.setText(QtGui.QApplication.translate("select", "Show Table Records", None, QtGui.QApplication.UnicodeUTF8))
        self.btnesit.setText(QtGui.QApplication.translate("select", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.btnkck.setText(QtGui.QApplication.translate("select", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.btnbyk.setText(QtGui.QApplication.translate("select", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.btnkckesit.setText(QtGui.QApplication.translate("select", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.btnbykesit.setText(QtGui.QApplication.translate("select", ">=", None, QtGui.QApplication.UnicodeUTF8))
        self.btnntesit.setText(QtGui.QApplication.translate("select", "!=", None, QtGui.QApplication.UnicodeUTF8))
        self.btnlike.setText(QtGui.QApplication.translate("select", "LIKE", None, QtGui.QApplication.UnicodeUTF8))
        self.btnyzd.setText(QtGui.QApplication.translate("select", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.btnin.setText(QtGui.QApplication.translate("select", "IN", None, QtGui.QApplication.UnicodeUTF8))
        self.btnntin.setText(QtGui.QApplication.translate("select", "NOT IN", None, QtGui.QApplication.UnicodeUTF8))
        self.btnand.setText(QtGui.QApplication.translate("select", "AND", None, QtGui.QApplication.UnicodeUTF8))
        self.btnor.setText(QtGui.QApplication.translate("select", "OR", None, QtGui.QApplication.UnicodeUTF8))

        #join Kısmı Arayüz Elemanları
        self.jlabel.setText(QtGui.QApplication.translate("select", "Database Connection :", None, QtGui.QApplication.UnicodeUTF8))
        self.jlabel1.setText(QtGui.QApplication.translate("select", "Database Tables:", None, QtGui.QApplication.UnicodeUTF8))
        self.jlabel2.setText(QtGui.QApplication.translate("select", "Selected joined layer attributes :", None, QtGui.QApplication.UnicodeUTF8))
        self.jlabel3.setText(QtGui.QApplication.translate("select", "Select input layer attributes :", None, QtGui.QApplication.UnicodeUTF8))
        self.jlabel4.setText(QtGui.QApplication.translate("select", "Samples :", None, QtGui.QApplication.UnicodeUTF8))
        self.btnjoin.setText(QtGui.QApplication.translate("select", "Join Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.btnVdgr.setText(QtGui.QApplication.translate("select", "Get Sample data from the joined layer", None, QtGui.QApplication.UnicodeUTF8))
        self.chckjoin.setText(QtGui.QApplication.translate("select", "Activated JOIN", None, QtGui.QApplication.UnicodeUTF8))
        
