# Engine Import Checklist

## Unity

- Import as FBX or glTF (glTFast package recommended for GLB).
- Scale Factor: 1.0 if source is meters. Check model size in scene.
- Mesh: Read/Write enabled only if needed at runtime.
- Materials: Extract textures. Set Normal Map type to Normal Map.
- Animations: None unless rigged.
- After import: Check normals, UV channel 0, and that pivot sits correctly.
- Mobile: Enable mesh compression, generate LODs or use LOD Group.

## Unreal Engine

- FBX import. Scale: often 1.0 if source in cm, or 100 if source in meters (verify).
- Generate Lightmap UVs if using static lighting.
- Nanite: Enable for static high-detail meshes.
- Material: Base Color sRGB, Normal (DirectX), Metallic/Roughness.
- Pivot: Place at origin or logical attachment point before export.
- Collision: Generate simple collision or import custom.

## Godot 4

- Prefer glTF/GLB. Import with Embedded Image.
- Scale: meters, Y-up.
- Mesh: Generate LODs in import settings if available.
- Materials: StandardMaterial3D with PBR textures.
- Collision: Use mesh or create ConvexPolygonShape / Trimesh.

## Common Post-Import Checks

- Model size matches expected real-world size.
- No flipped normals (black faces).
- UV islands have padding (no bleeding at mip levels).
- One material slot preferred for props.
- Performance: draw calls, texture memory, poly count within budget.
