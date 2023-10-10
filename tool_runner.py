import arcgis
import toolbox_library.import_portal_item as import_portal_item



def run_import_portal_item():
    # run with example values
    map_id = "e221dc39fa7d43609562c529f170d416" # Eagle Imagery Hybrid basemap
    new_title = None # optional, else item title will be used
    # call our main script, uses active Portal in ArcGIS Pro
    gis = arcgis.GIS("home")
    import_portal_item.do_execute(gis, map_id, new_title)


if __name__ == "__main__":
    run_import_portal_item()
