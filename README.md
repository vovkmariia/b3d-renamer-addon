<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/6b3db41f-14da-485f-8e15-c603735d4fc6" width="250px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/6b3db41f-14da-485f-8e15-c603735d4fc6" width="250px">
  <img alt="Blender Logo" src="https://github.com/user-attachments/assets/6b3db41f-14da-485f-8e15-c603735d4fc61" width="400px">
</picture>

 
</p>


<h1 align="center">Blender Renamer Tool</h1>

A pipeline-focused Blender add-on designed to automate standard game development naming conventions, make baking workflows faster, and keep outliners organized. 

This tool eliminates the repetitive, error-prone process of manually renaming meshes for engine export (Unreal Engine / Unity) and baking software (Marmoset Toolbag / Substance Painter).

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/926d6b2d-a875-499f-b75b-9d74bf598f32" width="1000px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/926d6b2d-a875-499f-b75b-9d74bf598f32" width="1000px">
  <img alt="Using addon - gif" src="https://github.com/user-attachments/assets/926d6b2d-a875-499f-b75b-9d74bf598f32" width="400px">
</picture>

</p>
---
# Key Features

Unlike basic string-append scripts, this tool uses "Smart Affix" logic. It detects existing pipeline prefixes/suffixes and replaces them rather than stacking them (e.g., swapping `Crate_high` to `Crate_low` with one click, instead of accidentally creating `Crate_high_low`).

* **Smart Engine Prefixes:** Quickly apply or swap `SM_` (Static Mesh) and `SK_` (Skeletal Mesh).
* **Smart Collision Prefixes:** Standardize custom Unreal Engine collisions with one-click `UCX_` and `UBX_` toggles.
* **Smart Baking Suffixes:** Instantly swap between `_low` / `_high` or `_lp` / `_hp` for seamless raycast baking in Substance Painter or Marmoset.
* **Duplication Cleanup:** A single button to strip Blender's default `.001`, `.002` iteration suffixes using regex matching.
* **Find & Replace:** Quickly swap specific naming strings across massive modular kits.

As a 3D Environment Artist, I noticed how much pipeline time was wasted manually formatting names for FBX exports or fixing baking raycast errors caused by typos. I developed this tool using Blender's `bpy` Python API to enforce strict naming conventions.

---
# Installation

1. Download the latest release: `b3d-renamer-addon.zip`
2. Open Blender and navigate to **Edit > Preferences > Add-ons**.
3. Click **Install...** and select the downloaded `.zip` file.
4. Check the box next to **Object: Game Dev Batch Renamer** to enable it.
5. ...or just drag and drop the archive straight into Blender!

---
# Usage

Once installed, the tool is designed to be easily accessible directly in the 3D Viewport.

1. Select one or more objects in the 3D Viewport.
2. Press **N** to open the side panel (N-Panel).
3. Click on the **Renamer** tab.
4. Use the categorized buttons to apply your desired naming conventions. All actions fully support `Ctrl+Z` undo functionality.

---
# Help!

If you encounter any issues with the plugin, please reach out to me via email:
mariia.vovk.contact@gmail.com