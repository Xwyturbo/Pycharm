# encoding: utf-8
import sys
import arcpy
arcpy.env.workspace = "D:/machinelearing/esri/data/等扇分析.gdb"
in_data =  "fen渔网尺度_等扇形分析"
out_data = "fen渔网尺度_等扇形分析_20241004"
data_type = "FeatureClass"
# Execute Rename
arcpy.Rename_management(in_data, out_data, data_type)


## 合并数据 ####
import arcpy
arcpy.env.workspace = "D:/GIShenan/try"
fcs = arcpy.ListFeatureClasses()
lspt = []
for fc in fcs:
    lspt.append(fc)
arcpy.Merge_management(lspt,"缓冲区区合并.shp")

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import arcpy
import string
arcpy.env.workspace  = r"C:\Users\Administrator\Desktop\s\pro\A49.gdb"
out = r"C:\Users\Administrator\Desktop\s\data100\da.gdb"
na = arcpy.env.workspace.split("\\")[-1].split(".")[0]
Files = arcpy.ListFeatureClasses()
for File in Files:
    if File == "BOUA":
        arcpy.Copy_management(File, out+"\\"+na)

