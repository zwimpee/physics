# Uninstall CPU JAX and install GPU JAX
_Exported on 11/28/2025 at 10:05:50 CST from Cursor (2.1.39)_

---

**User**

help me uninstall cpu jax and install gpu jax @verify_with_einfields.ipynb (1-9) WARNING:2025-11-28 16:00:44,764:jax._src.xla_bridge:854: An NVIDIA GPU may be present on this machine, but a CUDA-enabled jaxlib is not installed. Falling back to cpu.

✓ Ready!

---

**Cursor**

I'll help you uninstall the CPU version of JAX and install the GPU version with CUDA support.

GPU JAX with CUDA 12 has been installed successfully. Let me verify that JAX can now detect the GPU:

JAX is now using the GPU:
- **Devices:** `[CudaDevice(id=0)]` ✓
- **Default backend:** `gpu` ✓

The warnings about GPU interconnect/NVLink are harmless and just indicate you're not running a multi-GPU setup with NVLink.

**Important:** You'll need to restart the Jupyter kernel in your notebook to pick up the new GPU-enabled JAX installation. In Jupyter, go to **Kernel → Restart Kernel** (or click the restart button), then re-run your cells.

