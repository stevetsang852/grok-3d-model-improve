#!/usr/bin/env python3
"""Inspect a mesh file with trimesh. Reports key game-ready metrics."""
import sys
import trimesh

def main():
    if len(sys.argv) < 2:
        print("Usage: mesh_inspect.py <mesh_file>")
        sys.exit(1)
    path = sys.argv[1]
    try:
        m = trimesh.load(path, force="mesh")
    except Exception as e:
        print(f"Load failed: {e}")
        sys.exit(1)

    if isinstance(m, trimesh.Scene):
        m = trimesh.util.concatenate(m.dump())

    info = {
        "vertices": len(m.vertices),
        "faces": len(m.faces),
        "is_watertight": bool(m.is_watertight),
        "is_winding_consistent": bool(m.is_winding_consistent),
        "bounds": m.bounds.tolist(),
        "extents": m.extents.tolist(),
        "center_mass": m.center_mass.tolist() if hasattr(m, "center_mass") else None,
        "volume": float(m.volume) if m.is_watertight else None,
    }
    print(info)

if __name__ == "__main__":
    main()
