---
name: 3d-model-improve
description: "Improve 3D meshes into game-ready assets: clean topology, fix normals, UV, bake PBR, set poly budgets, and export for Unity, Unreal, or Godot. Use for AI-generated models, scans, retopology, cleanup, or making models production-ready."
type: workflow
lifecycle: active
---

# 3D Model Improve — Game-Ready Asset Pipeline

Turn raw, AI-generated, or scanned meshes into clean, engine-ready assets. Focus on real-time performance, correct scale, usable UVs, and predictable shading. Prefer local tools (Blender, trimesh, MeshLab) over cloud APIs unless the user provides credentials.

## Core Workflow

1. **Inspect** — Load the mesh and report: vertex/face count, watertight status, bounds/extents (assume meters), normal consistency, existing UVs, material slots. Use `scripts/mesh_inspect.py` or Blender.
2. **Decide target profile**
   - Static prop: tris or quads, aggressive decimation OK.
   - Character / deformable: quad-dominant with edge flow, manual or guided retopo preferred.
   - Print: watertight, outward normals, no UVs required.
3. **Clean** — Remove doubles, delete loose, make normals consistent, merge by distance (threshold relative to scale). Shade smooth or set hard edges at >60–90°.
4. **Remesh / Retopo only if needed**
   - Static / AI mesh: Blender QuadriFlow, Instant Meshes, or AutoRemesher.
   - Character: prefer assisted (RetopoFlow) or manual; automatic only as base.
   - Never remesh a clean CAD model.
5. **UV** — Non-overlapping (or intentional mirror), padding ≥ 4–8 texels at target resolution, seams aligned with hard edges. Second UV channel for lightmaps if the engine needs it.
6. **Bake** — Normal, AO, curvature from high to low if high-poly exists. Match hard edges to UV seams.
7. **Materials** — PBR: Base Color (sRGB), Metallic, Roughness, Normal (OpenGL or DirectX per engine). Keep texture sizes power-of-two.
8. **Export** — Match engine profile below. State before/after poly count and what was verified.

## Engine Export Profiles

| Engine       | Preferred Format | Scale / Units | Notes |
|--------------|------------------|---------------|-------|
| Unity        | FBX or glTF     | Meters, Y-up | Apply scale, freeze transform. Lightmap UV optional. |
| Unreal       | FBX             | Centimeters often preferred | Check import scale. Nanite can accept higher density. |
| Godot        | glTF/GLB        | Meters, Y-up | Embedded PBR preferred. |
| Web / three.js | GLB           | Meters       | Draco optional only if asked. |

## Tool Selection

| Need                  | Free / Local Preferred                  | Paid / Cloud Alternative     |
|-----------------------|-----------------------------------------|------------------------------|
| Inspect / repair      | trimesh, Blender, MeshLab               | —                            |
| Auto remesh (props)   | QuadriFlow (Blender), Instant Meshes, AutoRemesher | Quad Remesher, Meshy Remesh |
| Character retopo      | Manual + PolyQuilt                      | RetopoFlow, Nitro Retopo     |
| AI generate base      | Hunyuan3D-2.1, TRELLIS.2, Stable Fast 3D (local weights) | Meshy, Tripo, Rodin     |
| UV / bake             | Blender                                 | Substance Painter, Marmoset  |

See `references/tools.md` for repo links and usage notes. See `references/game_budgets.md` for poly and texture guidelines. See `references/engine_import.md` for engine checklists. See `references/lod_collision.md` for LOD and collision notes. See `references/lightmap_batch.md` for lightmap UV and batch processing.

## Scripts

- `scripts/mesh_inspect.py <file>` — Print verts, faces, watertight, extents, bounds.
- `scripts/blender_game_prep.py` — Full game-ready prep (clean, hard edges, Smart UV, export FBX + GLB). Optional target tris.

Adjust merge distance to model scale. Do not silently rescale; report units and ask if extents look wrong (e.g. 100s of units = likely cm).

## Quality Checklist (must report)

- [ ] Poly count before / after and target budget
- [ ] Manifold / non-manifold edge count (critical for print)
- [ ] Normals consistent and outward
- [ ] Scale stated (meters assumed)
- [ ] UV present + padding if textured
- [ ] Hard edges aligned with UV seams (if baked)
- [ ] Pivot / origin sensible
- [ ] Export format matches target engine
- [ ] List what was not checked (rig, LODs, texel density, engine import)

## Common Issues

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Black faces / shading seams | Inconsistent normals | Recalculate outward |
| Huge or tiny model | Wrong units | Report extents; scale only after confirmation |
| AI mesh explodes on animate | Triangle soup, no edge flow | Retopo to quads for characters |
| Bake artifacts | UV seams ≠ hard edges | Align seams to hard edges |
| Texture bleed | Insufficient padding | Increase island margin |

## Next Steps After Cleanup

Offer: LOD generation, lightmap UV, collision mesh, material atlas, or engine import checklist.
