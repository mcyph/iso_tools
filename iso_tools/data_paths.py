import os
from toolkit.data_paths import DataPaths

dir_path = os.path.dirname(os.path.realpath(__file__))

data_paths = DataPaths(dir_path, {
    "iso_codes": "iso_tools/data/iso_codes",
    "cldr": "iso_tools/data/cldr"
})
data_path = data_paths.data_path
