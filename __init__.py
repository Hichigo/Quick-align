bl_info = {
	"name": "Quick align",
	"author": "Nexus Studio",
	"version": (0, 7, 7),
	"blender": (2, 80, 0),
	"location": "View3D / Graph Editor / Node Editor / Image Editor > alt-Q key",
	"description": "Quick alignment on axis, fast set origin, drop to ground selected object",
	"wiki_url": "none",
	"category": "User",
}

import bpy

from bpy.props import StringProperty, BoolProperty, EnumProperty

from .functions import align_XYZ, align_graph

from .view3d_op import *
from .graph_op import *
from .uv_op import *
from .node_op import *
from .panels import *
from .DropToGround.drop_to_ground_op import *
# from .DropToGround.drop_to_ground_ui import *

# -----------------------------------------------------------------------------
#Pivot point
class OBJECT_OT_SetOrigin(bpy.types.Operator):
	"""Fast set origin to active vertex / polygon / edge"""
	bl_idname = "view3d.set_origin"
	bl_label = "Set origin to active vertex / polygon / edge"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		if (bpy.context.mode == 'EDIT_MESH') or (bpy.context.mode ==  'EDIT_CURVE'):
			cursor_location_temp = (bpy.context.scene.cursor.location.x,bpy.context.scene.cursor.location.y, bpy.context.scene.cursor.location.z)
			bpy.ops.view3d.snap_cursor_to_selected()
			bpy.ops.object.editmode_toggle()
			bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR')
			bpy.context.scene.cursor.location = cursor_location_temp
			#bpy.ops.object.editmode_toggle()
		elif bpy.context.mode == 'OBJECT':
			bpy.ops.object.origin_set(type = 'ORIGIN_GEOMETRY')

		return {'FINISHED'}

# -----------------------------------------------------------------------------
# menu classes
class VIEW3D_MT_menu(bpy.types.Menu):
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator(VIEW3D_OT_drop_to_ground.bl_idname, text="Drop to ground", icon="VIEW3D")
		layout.operator(VIEW3D_OT_align_all_axis.bl_idname, text="Align all axis", icon='EMPTY_AXIS')
		layout.operator(VIEW3D_OT_align_x_slots.bl_idname, text="X align", icon='EVENT_X')
		layout.operator(VIEW3D_OT_align_y_slots.bl_idname, text="Y align", icon='EVENT_Y')
		layout.operator(VIEW3D_OT_align_z_slots.bl_idname, text="Z align", icon='EVENT_Z')
		layout.operator(OBJECT_OT_SetOrigin.bl_idname, text="SetOrigin", icon='OBJECT_ORIGIN')
		layout.menu(ALIGN_MT_submenu.bl_idname, text="Align by")

class GRAPH_MT_menu(bpy.types.Menu):
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator(GRAPH_OT_align_x_slots.bl_idname, text="X align", icon='EVENT_X')
		layout.operator(GRAPH_OT_align_y_slots.bl_idname, text="Y align", icon='EVENT_Y')

class UV_MT_menu(bpy.types.Menu):
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator(UV_OT_align_x_slots.bl_idname, text="X align", icon='EVENT_X')
		layout.operator(UV_OT_align_y_slots.bl_idname, text="Y align", icon='EVENT_Y')

class NODE_MT_menu(bpy.types.Menu):
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator(NODE_OT_align_x_slots.bl_idname, text="X align", icon='EVENT_X')
		layout.operator(NODE_OT_align_y_slots.bl_idname, text="Y align", icon='EVENT_Y')

class ALIGN_MT_submenu(bpy.types.Menu):
	bl_label = "Quick align"
	bl_idname = "ALIGN_MT_submenu"

	def draw(self, context):
		layout = self.layout
		tools_settings = context.scene.tool_settings
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.prop(tools_settings, "transform_pivot_point", expand=True)

#class panel


class QuickAlign_WM_Properties(bpy.types.PropertyGroup):

	align_by_normal: BoolProperty(
		name="Align by Normal",
		description="Align object by normal",
		default=False
	)

	drop_by: EnumProperty(
		name="Drop by",
		items=[
			("ORIGIN", "Origin", "", 0),
			("ACTIVE", "Active Object", "", 1),
			# ("3DCURSOR", "3D Cursor", "", 2)
		],
		default = "ORIGIN"
	)

	direction_drop: EnumProperty(
		name="Direction Drop",
		items=[
			("-Z", "-Z", "", 0), # down
			( "Z",  "Z", "", 1), # up
			("-X", "-X", "", 2), # backward
			( "X",  "X", "", 3), # forward
			("-Y", "-Y", "", 4), # left
			( "Y",  "Y", "", 5), # right
			("3DCURSOR",  "to 3D cursor", "", 6)
		],
		default = "-Z"
	)

addon_keymaps = []
keymapsList = [
	{
		'name_view': "3D View",
		'space_type': "VIEW_3D",
		'prop_name': "VIEW3D_MT_menu"
	},
	{
		'name_view': "Image",
		'space_type': "IMAGE_EDITOR",
		'prop_name': "UV_MT_menu"
	},
	{
		'name_view': "Graph Editor",
		'space_type': "GRAPH_EDITOR",
		'prop_name': "GRAPH_MT_menu"
	},
	{
		'name_view': "Node Editor",
		'space_type': "NODE_EDITOR",
		'prop_name': "NODE_MT_menu"
	}
]

classes = (
	QuickAlign_WM_Properties,
	OBJECT_OT_SetOrigin,
	VIEW3D_OT_align_all_axis,
	VIEW3D_OT_align_x_slots,
	VIEW3D_OT_align_y_slots,
	VIEW3D_OT_align_z_slots,
	VIEW3D_OT_drop_to_ground,
	VIEW3D_PT_QuickAlign,
	VIEW3D_PT_DropToGround,
	GRAPH_OT_align_x_slots,
	GRAPH_OT_align_y_slots,
	UV_OT_align_x_slots,
	UV_OT_align_y_slots,
	NODE_OT_align_x_slots,
	NODE_OT_align_y_slots,
	VIEW3D_MT_menu,
	GRAPH_MT_menu,
	UV_MT_menu,
	NODE_MT_menu,
	ALIGN_MT_submenu
)

def register():
	from bpy.utils import register_class
	for cls in classes:
		register_class(cls)

	kc = bpy.context.window_manager.keyconfigs.addon
	if kc:
		for keym in keymapsList:
			km = kc.keymaps.new(name=keym['name_view'], space_type=keym['space_type'])
			kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS', alt=True)
			kmi.properties.name = keym['prop_name']
			addon_keymaps.append(km)

	bpy.types.Scene.quick_align = bpy.props.PointerProperty(type=QuickAlign_WM_Properties)

def unregister():
	from bpy.utils import unregister_class
	for cls in reversed(classes):
		unregister_class(cls)

	wm = bpy.context.window_manager
	if wm.keyconfigs.addon:
		for km in addon_keymaps:
			for kmi in km.keymap_items:
				km.keymap_items.remove(kmi)
	addon_keymaps.clear()

	del bpy.types.Scene.quick_align

if __name__ == "__main__":
	register()