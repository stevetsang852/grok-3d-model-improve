# Lightmap UV and Batch Notes

## Lightmap UV (Second Channel)

Needed for baked lighting in Unity (Lightmap UV) and Unreal (Lightmap UVs).

### Blender: Generate Lightmap UV

```python
import bpy
obj = bpy.context.active_object
# Ensure UV1 exists for lightmap
if not obj.data.uv_layers.get("Lightmap"):
    obj.data.uv_layers.new(name="Lightmap")
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.uv.lightmap_pack(PREF_CONTEXT="ALL_FACES", PREF_PACK_IN_ONE=True, PREF_MARGIN_DIV=0.1)
bpy.ops.object.mode_set(mode="OBJECT")
```

- Keep lightmap UV non-overlapping.
- Use larger margin than the main UV for mip safety.
- Export with both UV channels (FBX supports this; glTF support varies by importer).

### Engine Notes

- Unity: Enable Generate Lightmap UVs on import if you did not create them.
- Unreal: Check "Generate Lightmap UVs" in FBX import options.
- Godot: Lightmap UV support depends on version and pipeline; prefer engine bake tools when available.

## Batch Processing

### Simple Python Batch Inspect

```python
import os
import subprocess
folder = "models/"
for f in os.listdir(folder):
    if f.lower().endswith((".glb", ".gltf", ".obj", ".fbx", ".stl")):
        print(f"--- {f} ---")
        subprocess.run(["python3", "scripts/mesh_inspect.py", os.path.join(folder, f)])
```

### Blender Headless Batch (shell)

```bash
for f in models/*.glb; do
  base=$(basename "$f" .glb)
  blender --background --python scripts/blender_game_prep.py -- "$f" "out/${base}" 10000
done
```

- Process one mesh at a time in headless Blender to avoid memory spikes.
- Log poly count before/after for each file.
- Skip already-clean CAD files if extents and face count look intentional.

## Recommendations

- Always inspect before batch remesh.
- Keep original files; write cleaned versions to a separate folder.
- For large batches, add a simple report CSV (filename, verts, faces, watertight, max_extent).
