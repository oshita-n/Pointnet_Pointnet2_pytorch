import os
import sys
from indoor3d_util import DATA_PATH, collect_point_label
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)

output_folder = os.path.join(ROOT_DIR, 'data/preprocessing')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Note: there is an extra character in the v1.2 data in Area_5/hallway_6. It's fixed manually.
for file_name in glob.glob(os.path.join(ROOT_DIR,'data/Annotations/*.txt')):
    out_filename = os.path.splitext(os.path.basename(file_name))[0] +'.npy'
    collect_point_label(file_name, os.path.join(output_folder, out_filename), 'numpy')