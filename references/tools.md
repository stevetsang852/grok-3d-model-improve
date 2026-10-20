# Tool Reference

Prefer free local tools. Cloud services only when the user has an account and explicitly asks.

## Local / Open Source

| Tool | Best For | Repo / Notes |
|------|----------|--------------|
| Blender 4.x / 5.x | Cleanup, QuadriFlow remesh, UV, bake, export | blender.org — headless via `--background --python` |
| trimesh | Inspect, watertight, export, simple ops | github.com/mikedh/trimesh |
| PyMeshLab | Repair, decimate, filters | github.com/cnr-isti-vclab/PyMeshLab |
| Instant Meshes | Field-aligned remesh, forgiving on bad geo | github.com/wjakob/instant-meshes |
| AutoRemesher | All-quad automatic retopo, MIT, CLI | github.com/huxingyi/autoremesher (check latest) |
| QuadriFlow | Built-in Blender remesh or standalone | github.com/hjwdzh/QuadriFlow |
| Open3D | Point cloud → mesh, outlier removal | github.com/isl-org/Open3D |

## AI Generation (base mesh only — always clean after)

| Model | Notes | License |
|-------|-------|---------|
| Hunyuan3D-2.1 | Image/text → textured mesh + paint | Tencent, check current weights |
| TRELLIS.2 | High-detail PBR mesh | MIT (Microsoft) |
| Stable Fast 3D | Fast closed mesh | Stability community / enterprise |

Market: Meshy, Tripo3D, Rodin (Hyper3D), Luma. Use only with user credentials. Never store keys.

## Paid Add-ons (recommend only if user already owns or requests)

- RetopoFlow — assisted character retopo
- Quad Remesher — one-click quality remesh
- Nitro Retopo — segmentation + guided retopo (Blender 5.2+)

## Usage Notes

- AI outputs are starting points. Always inspect and remesh for game use.
- Automatic remeshers work well for static props and environments. Characters need deliberate edge flow.
- After remesh, re-UV. Remesh destroys previous UVs.
