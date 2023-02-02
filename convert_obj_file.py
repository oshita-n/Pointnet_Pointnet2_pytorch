import open3d as o3d
import numpy as np
import os

def obj_mesh(path):
    return o3d.io.read_triangle_mesh(path)

def draw_mesh(mesh):
    mesh.paint_uniform_color([1., 0., 0.])
    mesh.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh])

def mesh2ply(mesh):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.asarray(mesh.vertices))
    return pcd


if __name__ == "__main__":
    file_name = "102_00_pred.obj"
    path = "log/sem_seg/pointnet2_sem_seg/visual/" + file_name
    mesh = obj_mesh(path)

    pcd = mesh2ply(mesh)
    print(os.path.splitext(file_name)[0] +".pcd")
    # o3d.io.write_point_cloud(os.path.splitext(file_name)[0] +".pcd", pcd)