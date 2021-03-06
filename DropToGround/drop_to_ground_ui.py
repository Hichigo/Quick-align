import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty

class VIEW3D_PT_DropToGroundBase(bpy.types.Panel):
    """Panel drop to ground"""
    bl_label = "Drop To Ground"
    bl_idname = "VIEW3D_PT_DropToGroundBase"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Nexus"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        quick_align = context.scene.quick_align

        use_align_by_normal = True

        if quick_align.drop_by == "ACTIVE":
            use_align_by_normal = False

        col = layout.column()
        col.operator("view3d.drop_to_ground", text="Drop to ground", icon="VIEW3D")

        col = layout.column()
        col.enabled = use_align_by_normal
        col.prop(quick_align, "align_by_normal")

        row = layout.row()
        row.label(text="Drop by:")
        row.prop(quick_align, "drop_by", text="")

        row = layout.row()
        row.label(text="Direction Drop:")
        row.prop(quick_align, "direction_drop", text="")