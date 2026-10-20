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
        loaded = trimesh.load(path, force="mesh")
    except Exception as e:
        print(f"Load failed: {e}")
        sys.exit(1)

    if isinstance(loaded, trimesh.Scene):
        meshes = loaded.dump()
        m = trimesh.util.concatenate(meshes) if meshes else None
        mesh_count = len(meshes)
    else:
        m = loaded
        mesh_count = 1

    if m is None or len(m.faces) == 0:
        print("No mesh geometry found")
        sys.exit(1)

    # Non-manifold edges if available
    try:
        non_manifold = len(m.edges_unique[m.edges_unique_inverse]) - len(m.edges_unique) if hasattr(m, "edges_unique") else None
        # Simpler reliable check
        non_manifold_count = len(m.edges[m.edges_unique_length != 2]) if hasattr(m, "edges_unique_length") else None
    except Exception:
        non_manifold_count = None

    info = {
        "file": path,
        "mesh_count": mesh_count,
        "vertices": len(m.vertices),
        "faces": len(m.faces),
        "is_watertight": bool(m.is_watertight),
        "is_winding_consistent": bool(m.is_winding_consistent),
        "bounds": m.bounds.tolist(),
        "extents": [round(x, 4) for x in m.extents.tolist()],
        "center_mass": [round(x, 4) for x in m.center_mass.tolist()] if hasattr(m, "center_mass") else None,
        "volume": round(float(m.volume), 4) if m.is_watertight else None,
        "has_uv": bool(hasattr(m.visual, "uv") and m.visual.uv is not None),
        "non_manifold_edges_approx": non_manifold_count,
    }
    print(info)

    # Quick scale warning
    max_ext = max(info["extents"])
    if max_ext > 50:
        print("WARNING: Extents > 50. Likely centimeters or millimeters. Confirm units before scaling.")
    elif max_ext < 0.01:
        print("WARNING: Extents < 0.01. Model may be too small or in wrong units.")

if __name__ == "__main__":
    main()
