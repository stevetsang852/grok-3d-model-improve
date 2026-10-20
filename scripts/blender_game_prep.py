"""
Enhanced Blender game-ready prep script.
Cleans mesh, sets hard edges on sharp angles, basic smart UV, exports FBX + GLB.
Usage:
  blender --background --python blender_game_prep.py -- input.glb output_base [target_tris]
"""
import bpy
import sys
import bmesh

def main():
    argv = sys.argv
    if "--" not in argv:
        print("Usage: blender --background --python blender_game_prep.py -- input output_base [target_tris]")
        return
    args = argv[argv.index("--") + 1:]
    if len(args) < 2:
        print("Need input and output base name")
        return
    src = args[0]
    base = args[1]
    target_tris = int(args[2]) if len(args) > 2 else None

    bpy.ops.wm.read_factory_settings(use_empty=True)

    ext = src.lower().split(".")[-1]
    if ext in ("glb", "gltf"):
        bpy.ops.import_scene.gltf(filepath=src)
    elif ext == "fbx":
        bpy.ops.import_scene.fbx(filepath=src)
    elif ext == "obj":
        bpy.ops.wm.obj_import(filepath=src)
    else:
        print(f"Unsupported: {ext}")
        return

    for obj in list(bpy.data.objects):
        if obj.type != "MESH":
            continue
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        # Clean
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.remove_doubles(threshold=0.0001)
        bpy.ops.mesh.delete_loose()
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.mode_set(mode="OBJECT")

        # Optional decimate toward target
        if target_tris and len(obj.data.polygons) > target_tris:
            mod = obj.modifiers.new("Decimate", "DECIMATE")
            mod.ratio = max(0.1, target_tris / len(obj.data.polygons))
            bpy.ops.object.modifier_apply(modifier=mod.name)

        # Hard edges on sharp angles
        bpy.ops.object.mode_set(mode="EDIT")
        bm = bmesh.from_edit_mesh(obj.data)
        for edge in bm.edges:
            if edge.calc_face_angle_signed(0) > 1.0:  # ~57 degrees
                edge.smooth = False
        bmesh.update_edit_mesh(obj.data)
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.shade_smooth()

        # Basic Smart UV
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(angle_limit=66, island_margin=0.02)
        bpy.ops.object.mode_set(mode="OBJECT")

    # Export both
    bpy.ops.export_scene.fbx(filepath=base + ".fbx", use_selection=False, apply_scale_options="FBX_SCALE_ALL")
    bpy.ops.export_scene.gltf(filepath=base + ".glb", export_format="GLB")
    print(f"Exported {base}.fbx and {base}.glb")

if __name__ == "__main__":
    main()
