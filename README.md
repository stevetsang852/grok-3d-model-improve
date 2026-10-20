# Grok 3D Model Improve

A practical skill for turning raw, AI-generated, or scanned meshes into clean, engine-ready game assets.

Focus on real-time performance, correct scale, usable UVs, and predictable shading. Prefer free local tools (Blender, trimesh, MeshLab) over cloud services.

## Features

- Mesh inspection (poly count, watertight, scale, normals, UV presence)
- Cleanup (doubles, loose geometry, consistent normals)
- Remesh / retopo guidance (static props vs deformable characters)
- UV, hard edges, lightmap UV, and bake notes
- Poly budgets and engine-specific export profiles
- LOD, collision, and batch processing guidance
- Headless Blender scripts for repeatable cleanup

## Quick Start

1. Place this folder in your Grok skills directory.
2. Ask Grok things like:
   - "Clean this GLB and make it game-ready for Unity"
   - "Check if this STL is watertight for printing"
   - "Optimize this prop under 10k tris for mobile Godot"
   - "Add lightmap UVs and generate simple LODs"

## Scripts

```bash
# Inspect (requires trimesh)
python3 scripts/mesh_inspect.py model.glb

# Basic cleanup (requires Blender 4.x+)
blender --background --python scripts/blender_cleanup.py -- input.glb output.glb

# Game-ready prep: clean, hard edges, Smart UV, FBX + GLB (optional target tris)
blender --background --python scripts/blender_game_prep.py -- input.glb output_base 8000
```

## Structure

```
.
├── SKILL.md                  # Core workflow and rules
├── CHANGELOG.md
├── LICENSE                   # MIT
├── scripts/
│   ├── mesh_inspect.py       # trimesh inspection + scale warnings
│   ├── blender_cleanup.py    # Headless basic cleanup
│   └── blender_game_prep.py  # Cleanup + hard edges + Smart UV + dual export
├── references/
│   ├── tools.md              # Free and commercial tool list
│   ├── game_budgets.md       # Poly and texture budgets
│   ├── engine_import.md      # Unity / Unreal / Godot checklists
│   ├── lod_collision.md      # LOD and collision notes
│   └── lightmap_batch.md     # Lightmap UV and batch processing
└── evals/                    # Trigger and behavior tests
```

## Supported Targets

| Engine   | Preferred Format | Notes |
|----------|------------------|-------|
| Unity    | FBX or glTF     | Meters, Y-up |
| Unreal   | FBX             | Check import scale; Nanite for static |
| Godot    | glTF/GLB        | Meters, Y-up, embedded PBR |
| Web      | GLB             | Meters |

## Requirements

- Python 3 + `trimesh` (inspect script)
- Blender 4.x or later (cleanup and game prep scripts)

## Workflow Summary

1. Inspect and report metrics
2. Decide target (static prop / character / print)
3. Clean normals and topology
4. Remesh only if needed
5. UV and optional lightmap channel
6. Bake and assign PBR
7. Export with engine profile
8. Report before/after and what was not verified

## License

MIT. See [LICENSE](LICENSE).
