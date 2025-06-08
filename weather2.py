from pyowm import OWM
from pyowm.tiles.enums import MapLayerEnum
from PIL import Image

owm = OWM('978910f354606707ef717cdf3b483575')

# Choose the map layer you want tiles for (eg. temeperature
layer_name = MapLayerEnum.TEMPERATURE

# Obtain an instance to a tile manager object
tm = owm.tile_manager(layer_name)

# Now say you want tile at coordinate x=5 y=2 at a zoom level of 6
tile = tm.get_tile(5, 2, 6)

# You can now save the tile to disk
#tile.persist('/path/to/file.png')

img = tile.image.data
img.show()


# Wait! but now I need the pressure layer tile at the very same coordinates and zoom level! No worries...
# Just change the map layer name on the TileManager and off you go!
tm.map_layer = MapLayerEnum.PRESSURE
tile = tm.get_tile(5, 2, 6)