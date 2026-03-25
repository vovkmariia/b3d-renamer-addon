bl_info = {
    "name": "Renamer Tool",
    "author": "Mariia Vovk - https://github.com/vovkmariia",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Renamer",
    "description": "Smart batch renamer for game-dev pipelines.",
    "category": "Object",
}

import bpy
import re


# ---------------------------OPERATORS---------------------------

class OBJECT_OT_smart_prefix(bpy.types.Operator):
    bl_idname = "object.smart_prefix"
    bl_label = "Add Smart Prefix"
    bl_description = "Appends the selected prefix to the start of the object name, replacing known prefixes"
    bl_options = {'REGISTER', 'UNDO'}

    target_prefix: bpy.props.StringProperty()

    def execute(self, context):
        known_prefixes = ["SM_", "SK_", "UCX_", "UBX_"]

        for obj in context.selected_objects:
            if obj.name.startswith(self.target_prefix):
                continue

            for k_prefix in known_prefixes:
                if obj.name.startswith(k_prefix):
                    obj.name = obj.name[len(k_prefix):]
                    break

            obj.name = self.target_prefix + obj.name

        return {'FINISHED'}


class OBJECT_OT_smart_suffix(bpy.types.Operator):
    bl_idname = "object.smart_suffix"
    bl_label = "Add Smart Suffix"
    bl_description = "Appends the selected suffix to the end of the object name, replacing known suffixes"
    bl_options = {'REGISTER', 'UNDO'}

    target_suffix: bpy.props.StringProperty()

    def execute(self, context):
        known_suffixes = ["_low", "_high", "_lp", "_hp"]

        for obj in context.selected_objects:
            if obj.name.endswith(self.target_suffix):
                continue

            for k_suffix in known_suffixes:
                if obj.name.endswith(k_suffix):
                    obj.name = obj.name[:-len(k_suffix)]
                    break

            obj.name = obj.name + self.target_suffix

        return {'FINISHED'}


class OBJECT_OT_clean_duplication_numbers(bpy.types.Operator):
    bl_idname = "object.clean_duplication_numbers"
    bl_label = "Clean .00x Suffixes"
    bl_description = "Removes Blender's automatically generated .001, .002 duplication numbers"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            obj.name = re.sub(r'\.\d{3}$', '', obj.name)
        return {'FINISHED'}


class OBJECT_OT_find_replace(bpy.types.Operator):
    bl_idname = "object.find_replace"
    bl_label = "Replace Text"
    bl_description = "Finds the specified text in selected object names and replaces it"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        find_str = context.scene.rename_find
        replace_str = context.scene.rename_replace
        if not find_str:
            self.report({'WARNING'}, "Find field is empty!")
            return {'CANCELLED'}
        for obj in context.selected_objects:
            obj.name = obj.name.replace(find_str, replace_str)
        return {'FINISHED'}


# ---------------------------UI PANEL---------------------------

class VIEW3D_PT_batch_renamer(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renamer'
    bl_label = "Renamer Tool"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # ---------------------------Prefixes---------------------------
        layout.label(text="Prefixes:", icon='MESH_DATA')
        row = layout.row()
        row.operator("object.smart_prefix", text="SM_").target_prefix = "SM_"
        row.operator("object.smart_prefix", text="SK_").target_prefix = "SK_"

        row = layout.row()
        row.operator("object.smart_prefix", text="UCX_").target_prefix = "UCX_"
        row.operator("object.smart_prefix", text="UBX_").target_prefix = "UBX_"

        layout.separator()

        # ---------------------------Suffixes---------------------------
        layout.label(text="Suffixes:", icon='TEXTURE')
        row = layout.row()
        row.operator("object.smart_suffix", text="_low").target_suffix = "_low"
        row.operator("object.smart_suffix", text="_high").target_suffix = "_high"

        row = layout.row()
        row.operator("object.smart_suffix", text="_lp").target_suffix = "_lp"
        row.operator("object.smart_suffix", text="_hp").target_suffix = "_hp"

        layout.separator()

        # ---------------------------Additional---------------------------
        layout.label(text="Additional:", icon='TOOL_SETTINGS')

        box = layout.box()
        box.prop(scene, "rename_find")
        box.prop(scene, "rename_replace")
        box.operator("object.find_replace", text="Replace Text", icon='FILE_REFRESH')

        layout.separator()

        layout.operator("object.clean_duplication_numbers", text="Remove .00x", icon='BRUSH_DATA')


# ---------------------------REGISTRATION---------------------------

classes = [
    OBJECT_OT_smart_prefix,
    OBJECT_OT_smart_suffix,
    OBJECT_OT_clean_duplication_numbers,
    OBJECT_OT_find_replace,
    VIEW3D_PT_batch_renamer
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.rename_find = bpy.props.StringProperty(
        name="Find",
        description="Text to search for",
        default=""
    )
    bpy.types.Scene.rename_replace = bpy.props.StringProperty(
        name="Replace",
        description="Text to replace it with",
        default=""
    )


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.rename_find
    del bpy.types.Scene.rename_replace


if __name__ == "__main__":
    register()