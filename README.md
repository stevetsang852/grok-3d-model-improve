# Grok 3D Model Improve Skill

A Grok skill for turning raw, AI-generated, or scanned 3D meshes into game-ready assets.

## What it does

- Inspect meshes (poly count, watertight, scale, normals)
- Clean topology and fix normals
- Remesh / retopo guidance for props vs characters
- UV, bake, and PBR material notes
- Export profiles for Unity, Unreal Engine, and Godot

## Structure

- `SKILL.md` — Main skill instructions
- `scripts/` — Blender headless scripts and mesh inspector
- `references/` — Tool list, poly budgets, engine import checklists
- `evals/` — Trigger and behavior tests

## Quick start

1. Place this folder in your Grok skills directory.
2. Ask Grok to clean or prepare a 3D model for your engine.

## Scripts

```bash
# Inspect (requires trimesh)
python3 scripts/mesh_inspect.py model.glb

# Game-ready prep (requires Blender)
blender --background --python scripts/blender_game_prep.py -- input.glb output_base 8000
```

## License

Use freely for game development. Scripts are provided as-is.
