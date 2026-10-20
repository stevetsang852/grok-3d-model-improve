# Game Asset Budgets (Guidance)

These are typical targets. Always confirm with the project's platform and art style. Numbers are approximate.

## Polygon Budgets (triangles)

| Asset Type | Mobile | PC / Console | Notes |
|------------|--------|--------------|-------|
| Small prop | 200–2k | 1k–8k | Aggressive decimation OK |
| Medium prop / furniture | 2k–8k | 5k–20k | |
| Hero prop / weapon | 5k–15k | 15k–40k | Keep silhouette |
| Character (LOD0) | 8k–25k | 25k–80k+ | Quad-dominant preferred |
| Environment modular | 1k–5k | 3k–15k | Instance heavily |

Nanite (Unreal) or similar can raise limits significantly for static geometry.

## Texture Resolutions

| Asset Role | Mobile | PC / Console |
|------------|--------|--------------|
| Small prop | 256–512 | 512–1k |
| Medium / modular | 512–1k | 1k–2k |
| Hero | 1k–2k | 2k–4k |
| Character | 1k–2k | 2k–4k (UDIM possible) |

Padding: at least 4–8 texels at the target resolution to prevent bleed.

## Other Guidelines

- Prefer power-of-two textures.
- One material slot per mesh when possible (atlas for many small props).
- Second UV channel for lightmaps if baked lighting is used.
- LODs: generate at least LOD1 at ~50% and LOD2 at ~25% for important assets.
- Scale: meters in DCC, confirm engine import scale.
- Pivot: at base for props that sit on surfaces; at logical joint for modular pieces.

Update these numbers if the project has a specific style guide.
