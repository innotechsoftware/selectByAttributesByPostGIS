# -*- coding: utf-8 -*-
# Utility functions
# -------------------------------------------------
#
# combineVectorAttributes( QgsAttributeMap, QgsAttributeMap )
# convertFieldNameType( QgsField.name() )
# combineVectorFields( QgsVectorLayer, QgsVectorLayer )
# checkCRSCompatibility( QgsCoordinateReferenceSystem, QgsCoordinateReferenceSystem )
# writeVectorLayerToShape(QgsVectorLayer, QString *file path, QString *encoding style )
# getVectorTypeAsString( QgsVectorLayer )
# measurePerimeter( QgsGeometry )
# extractPoints( QgsGeometry )
# testForUniqueness( QList *QgsField, QList *QgsField )
# createUniqueFieldName( QgsField.name() )
# checkFieldNameLength( QgsFieldMap )
# getLayerNames( QGis.vectorType() )
# getFieldNames( QgsVectorLayer )
# getVectorLayerByName( QgsVectorLayer.name() )
# getFieldList( QgsVectorLayer )
# createIndex( QgsVectorDataProvider )
# addShapeToCanvas( QString *file path )
# getUniqueValues( QgsVectorDataProvider, int *field id )
# saveDialog( QWidget *parent )
# getFieldType( QgsVectorLayer, QgsField.name() )
# getUniqueValuesCount( QgsVectorLayer, int fieldIndex, bool useSelection ):
#
# -------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *



def getVectorLayerByName(myName):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        for name, layer in layermap.iteritems():
            if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
                if layer.isValid():
                    return layer
                else:
                    return None
