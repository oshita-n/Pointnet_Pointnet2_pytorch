import open3d as o3d
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description='add filename')
parser.add_argument('--filename', type=str, default="filename")

args = parser.parse_args()
file_name = args.filename

def delete_v(path): 
    with open(path, "r") as f:
        lines = f.read().splitlines()
    re_lines = []
    for line in lines:
        re_lines.append(line.replace("v ", ""))

    return re_lines

if __name__ == "__main__":
    path = "log/sem_seg/pointnet2_sem_seg/visual/" + file_name
    lines = delete_v(path)

    with open("log/sem_seg/pointnet2_sem_seg/visual/" + os.path.splitext(file_name)[0] + ".txt", "w") as f:
        for line in lines:
            f.write(line + "\n")
