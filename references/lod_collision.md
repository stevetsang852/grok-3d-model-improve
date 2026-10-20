# LOD and Collision Notes

## LOD Generation

Prefer engine-side or dedicated tools for final LODs. Blender can produce quick baselines.

### Quick Blender Decimate LODs

```python
# In Blender Python or headless script
import bpy
obj = bpy.context.active_object
for name, ratio in [("LOD1", 0.5), ("LOD2", 0.25)]:
    dup = obj.copy()
    dup.data = obj.data.copy()
    dup.name = name
    bpy.context.collection.objects.link(dup)
    mod = dup.modifiers.new("Decimate", "DECIMATE")
    mod.ratio = ratio
    bpy.context.view_layer.objects.active = dup
    bpy.ops.object.modifier_apply(modifier=mod.name)
```

- Keep silhouette on LOD1.
- LOD2 can be more aggressive for distant props.
- For characters, manual or guided reduction is safer than pure decimate.
- Unreal Nanite often reduces the need for hand-made LODs on static meshes.

## Collision

### Simple Collision Options

| Type | Use Case | Notes |
|------|----------|-------|
| Box / Sphere / Capsule | Simple props, characters | Fastest, preferred for mobile |
| Convex Hull | Irregular props that need decent shape | Good middle ground |
| Trimesh | Complex static environment | Expensive, use sparingly |
| Simplified Mesh | Custom accuracy | Duplicate + decimate, then export separately |

### Blender Convex Hull Example

```python
import bpy
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.mesh.convex_hull()
bpy.ops.object.mode_set(mode="OBJECT")
```

Export the collision mesh with a clear name (e.g. `prop_collider.fbx`) or as a second object in the same file.

## Recommendations

- Always generate collision separately from the render mesh.
- Test collision in the target engine; visual mesh is not the authority.
- For mobile, prefer primitive colliders over trimesh.
- Document which LODs and collision type were created in the asset notes.
