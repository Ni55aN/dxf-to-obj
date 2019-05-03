import bpy
import platform
import sys
argv = sys.argv

inp = '/blender/'+argv[5]
out = '/blender/'+argv[6]

bpy.ops.wm.addon_install(filepath='/blender/addons/io_import_dxf/__init__.py')
bpy.ops.wm.addon_enable(module='io_import_dxf')
bpy.ops.wm.save_userpref()

bpy.ops.scene.new(type='EMPTY')
bpy.ops.import_scene.dxf(filepath=inp)
bpy.ops.export_scene.obj(filepath=out)