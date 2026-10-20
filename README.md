# Grok 3D Model Improve Skill

Turn raw, AI-generated, or scanned 3D meshes into clean, engine-ready game assets.

## What it does

- Inspect poly count, watertight status, scale, normals
- Clean doubles, loose geometry, and normal direction
- Guide remesh / retopo (props vs characters)
- Basic UV, hard edges, and PBR notes
- Export profiles for Unity, Unreal Engine, and Godot
- Poly budget and engine import checklists

## Quick Start

Place this folder in your Grok skills directory, then ask:

- "Clean this GLB and make it game-ready for Unity"
- "Check if this STL is watertight for printing"
- "Optimize this prop under 10k tris for mobile Godot"

## Scripts

```bash
# Inspect (requires trimesh)
python3 scripts/mesh_inspect.py model.glb

# Basic cleanup (requires Blender)
blender --background --python scripts/blender_cleanup.py -- input.glb output.glb

# Game-ready prep with Smart UV + dual export (requires Blender)
blender --background --python scripts/blender_game_prep.py -- input.glb output_base 8000
```

## Structure

- `SKILL.md` — Core workflow and rules
- `scripts/` — Inspect and Blender headless tools
- `references/` — Tools, budgets, engine import, LOD & collision notes
- `evals/` — Trigger and behavior tests

## Requirements

- Python 3 + trimesh (for inspect)
- Blender 4.x+ (for cleanup and game prep scripts)

## License

MIT. See LICENSE.
