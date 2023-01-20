import sys
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

input_dir = "data/"
file_name_list = glob.glob(input_dir + "*.pcd")
for file_name in file_name_list:
    pcd = o3d.io.read_point_cloud(file_name)
    points = np.asanyarray(pcd.points)
    colors = np.array(np.asanyarray(pcd.colors)*255, dtype=np.int64)
    os.makedirs(input_dir + "Annotations/", exist_ok=True)
    with open(input_dir + "Annotations/" + os.path.splitext(os.path.basename(file_name))[0] + ".txt", "w") as f:
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            z = points[i][2]
            r = colors[i][0]
            g = colors[i][1]
            b = colors[i][2]
            f.write(f"{x} {y} {z} {r} {g} {b}\n")