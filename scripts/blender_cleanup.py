"""
Headless Blender cleanup script.
Usage:
  blender --background --python blender_cleanup.py -- input.glb output.glb [merge_threshold]
"""
import bpy
import sys

def main():
    argv = sys.argv
    if "--" not in argv:
        print("Usage: blender --background --python blender_cleanup.py -- input output [threshold]")
        return
    args = argv[argv.index("--") + 1:]
    if len(args) < 2:
        print("Need input and output paths")
        return
    src, dst = args[0], args[1]
    threshold = float(args[2]) if len(args) > 2 else 0.0001

    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Try common importers
    ext = src.lower().split(".")[-1]
    if ext in ("glb", "gltf"):
        bpy.ops.import_scene.gltf(filepath=src)
    elif ext == "fbx":
        bpy.ops.import_scene.fbx(filepath=src)
    elif ext == "obj":
        bpy.ops.wm.obj_import(filepath=src)
    else:
        print(f"Unsupported extension: {ext}")
        return

    for obj in list(bpy.data.objects):
        if obj.type != "MESH":
            continue
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.remove_doubles(threshold=threshold)
        bpy.ops.mesh.delete_loose()
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.shade_smooth()

    # Export GLB by default; user can re-export if needed
    bpy.ops.export_scene.gltf(filepath=dst, export_format="GLB")
    print(f"Cleaned and exported to {dst}")

if __name__ == "__main__":
    main()
