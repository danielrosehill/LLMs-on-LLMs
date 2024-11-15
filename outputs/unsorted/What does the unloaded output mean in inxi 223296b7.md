# Terminal input

```
  Device-1: AMD Navi 32 [Radeon RX 7700 XT / 7800 XT] driver: amdgpu v: kernel
  Display: x11 server: X.Org v: 1.21.1.11 with: Xwayland v: 24.1.1 driver:
    X: loaded: amdgpu unloaded: fbdev,modesetting,vesa dri: radeonsi gpu: amdgpu
    resolution: 1: 1920x1080~60Hz 2: 1920x1080~60Hz 3: 1920x1080~60Hz
  API: OpenGL v: 4.6 Mesa 23.3.4 renderer: AMD Radeon RX 7700 XT (radeonsi
    navi32 LLVM 17.0.6 DRM 3.57 6.4.0-150600.23.25-default)
```

In your GPU driver output, "unloaded: fbdev,modesetting,vesa" indicates the display drivers that are not currently in use. Here's what this means:

## Currently Active

- `amdgpu` - This is the main driver currently loaded and running your RX 7700 XT
- `radeonsi` - The OpenGL driver implementation for AMD cards

## Unloaded Drivers

These are alternative basic display drivers that are not being used:

- `fbdev` - Basic framebuffer driver
- `modesetting` - Generic modesetting driver
- `vesa` - Basic VESA driver

This is actually the ideal configuration because:

1. The high-performance `amdgpu` driver is loaded and active
2. The basic fallback drivers are unloaded since they're not needed
3. The `radeonsi` DRI driver is providing 3D acceleration

Having these basic drivers unloaded is normal and preferred when running the full-featured `amdgpu` driver. It shows your system is correctly prioritizing the proper high-performance driver for your GPU.

&#x20;
