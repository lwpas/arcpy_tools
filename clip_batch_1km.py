import arcpy
from arcpy.sa import *

# 设置工作空间和输出路径
arcpy.env.workspace = r"E:\地遥中心\项目\tmp\data"
out_folder_path = r"E:\地遥中心\项目\tmp"

in_raster = r"E:\地遥中心\项目\tmp\500118GF1709095820220706C1.tif"
clip_features = r"E:\地遥中心\项目\tmp\第一批成果.shp"
out_file = r"E:\地遥中心\项目\tmp"

Distance = 1000

# 获取矢量要素的数量
feature_count = int(arcpy.GetCount_management(in_raster).getOutput(0))

# 循环遍历每一个要素并裁剪栅格数据
with arcpy.da.SearchCursor(vector_path, ["SHAPE@"]) as cursor:
    for i, row in enumerate(cursor):
        # 裁剪栅格数据
        out_raster = ExtractByMask(raster_path, row[0])
        # 保存裁剪后的栅格数据
        out_name = "raster_" + str(i) + ".tif"
        out_raster.save(out_folder_path + "/" + out_name)

