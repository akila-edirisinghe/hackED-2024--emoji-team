import folium
import pandas as pd
from sodapy import Socrata


def main(inputs):
    # Create a folium map
    maps = displaying_map()
    data = request_files()
    return {"maps" : maps, "data" : data}


def displaying_map():

    map_tile = ['OpenStreetMap']
    m = folium.Map(location=[53.5461, -113.4937],zoom_start=10, tiles=map_tile[0])
    map_html = m._repr_html_()
    return {"map": map_html}


def request_files():
    client = Socrata("data.edmonton.ca", None)
    results = client.get("7fnd-72gr")
    results_df = pd.DataFrame.from_records(results)
    return results_df