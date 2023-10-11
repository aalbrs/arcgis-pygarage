import arcgis.gis
import arcpy


def log(message):
    arcpy.AddMessage(message)


def do_execute(target_gis: arcgis.GIS, item_id: str, title: str = None):
    home_gis = arcgis.GIS("https://arcgis.com")
    log(f"Searching {home_gis.url}")
    log(f"Cloning to {target_gis.url}")

    # source webmap (template)
    log(f"Searching for item by ID: {item_id}")
    src_item = home_gis.content.get(item_id)
    src_item_props = {}
    for key in src_item:
        val = src_item[key]
        if key == 'title' and title:
            val = title
        src_item_props[key] = val
    src_data = src_item.get_data()

    # copy to new web map item
    log(f"Copying item as: {src_item_props['title']}")
    target_item = target_gis.content.add(src_item_props)
    target_data = target_item.get_data()
    target_data.update(src_data)
    target_item.update(data=target_data)

    # also consider webmap method:
    # map1 = arcgis.mapping.WebMap(map_data).save({ }, folder="")
