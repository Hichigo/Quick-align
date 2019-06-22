import bpy

from .DropToGround.drop_to_ground_ui import *

panel_space_type = "VIEW_3D"
panel_region_type = "UI"
panel_category = "Nexus"

class VIEW3D_PT_QuickAlign(bpy.types.Panel):
	"""Creates a Panel in the view3d context of the tools panel (key "N")"""
	bl_label = "Quick Align"
	bl_idname = "VIEW3D_PT_QuickAlign"
	bl_space_type = panel_space_type
	bl_region_type = panel_region_type
	bl_category = panel_category
	bl_options = {"DEFAULT_CLOSED"}

	def draw(self, context):
		layout = self.layout
		tools_settings = context.scene.tool_settings
		box = layout.box()
		box.label(text="Align by:")
		col = box.column()
		col.prop(tools_settings, "transform_pivot_point", expand=True)

class VIEW3D_PT_DropToGround(VIEW3D_PT_DropToGroundBase):
    bl_space_type = panel_space_type
    bl_region_type = panel_region_type
    bl_parent_id = VIEW3D_PT_QuickAlign.bl_idname
    bl_category = panel_category