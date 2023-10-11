# -*- coding: utf-8 -*-

import arcpy, arcgis
import toolbox_library.import_portal_item as import_portal_item


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "PyGarage"
        self.alias = "PyGarage"

        # List of tool classes associated with this toolbox
        self.tools = [ImportPortalItem]


class ImportPortalItem(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Import Web Map"
        self.description = "Imports a public web map item to your Portal or ArcGIS Online site"
        self.canRunInBackground = True

    def getParameterInfo(self):
        # see for reference
        # https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameter-data-types-in-a-python-toolbox.htm

        param0 = arcpy.Parameter(
            displayName="Web Map ID to Clone",
            name="source_map_id",
            datatype="GPString",
            parameterType="Optional",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName="New Title",
            name="dest_map_title",
            datatype="GPString",
            parameterType="Optional",
            direction="Input")

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        # gather parameters by index
        map_id = parameters[0].valueAsText
        new_title = parameters[1].valueAsText
        # call our main script
        gis = arcgis.GIS("home")
        import_portal_item.do_execute(gis, map_id, new_title)
