bl_info = {
	"name": "Quick align",
	"author": "Nexus Studio",
	"version": (0, 7, 7),
	"blender": (2, 80, 0),
	"location": "View3D / Graph Editor / Node Editor / Image Editor > alt-Q key",
	"description": "Quick alignment on axis and fast set origin",
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
	bl_idname = "alignsubmenu"
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		tools_settings = context.scene.tool_settings
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.prop(tools_settings, "transform_pivot_point", expand=True)

#class panel
# class QuickAlignPanel(bpy.types.Panel):
# 	"""Creates a Panel in the view3d context of the tools panel (key "T")"""
# 	bl_label = "Quick align"
# 	bl_idname = "quickalignid"
# 	bl_space_type = 'VIEW_3D'
# 	bl_region_type = 'TOOLS'
# 	bl_category = "Nexus Tools"

# 	itemsEnum = [
# 		("ACTIVE_ELEMENT", "Active element", ""),
# 		("MEDIAN_POINT", "Median point", ""),
# 		("CURSOR", "3D Cursor", "")
# 	]

# 	bpy.types.Scene.regarding = EnumProperty(items=itemsEnum)

# 	def draw(self, context):
# 		layout = self.layout
# 		scene = context.scene
# 		box = layout.box()
# 		box.label(text="Align by:")
# 		col = box.column()
# 		col.prop(scene, "regarding", expand=True)

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
	OBJECT_OT_SetOrigin,
	VIEW3D_OT_align_all_axis,
	VIEW3D_OT_align_x_slots,
	VIEW3D_OT_align_y_slots,
	VIEW3D_OT_align_z_slots,
	VIEW3D_OT_drop_to_ground,
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
	# QuickAlignPanel
	)

def register():
	# bpy.utils.register_module(__name__)
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

def unregister():
	# bpy.utils.unregister_module(__name__)
	from bpy.utils import unregister_class
	for cls in reversed(classes):
		unregister_class(cls)

	wm = bpy.context.window_manager
	if wm.keyconfigs.addon:
		for km in addon_keymaps:
			for kmi in km.keymap_items:
				km.keymap_items.remove(kmi)
	addon_keymaps.clear()

if __name__ == "__main__":
	register()


#################### FOR DROP TO GROUND #####################
# import bpy
# from mathutils import *

# ground = bpy.context.active_object
# obs = bpy.context.selected_objects
# down = Vector((0.0, 0.0, -1.0))

# obs.remove(ground)



# def transform_ground_to_world(sc, ground):
#     tmpMesh = ground.to_mesh(sc, True, 'PREVIEW')
#     tmpMesh.transform(ground.matrix_world)
#     tmp_ground = bpy.data.objects.new('tmpGround', tmpMesh)
#     sc.objects.link(tmp_ground)
#     sc.update()
#     return tmp_ground


# tmp_ground = transform_ground_to_world(bpy.context.scene, ground)
# for ob in obs:
#     if ob.type == "MESH":
#         is_hit, hit_location, hit_normal, hit_index = tmp_ground.ray_cast(ob.location, down)
        
#         if is_hit:
#             ob.location = hit_location

# bpy.ops.object.select_all(action='DESELECT')
# tmp_ground.select = True
# bpy.ops.object.delete('EXEC_DEFAULT')
# for ob in obs:
#     ob.select = True
# ground.select = True

# print(is_hit, hit_location, hit_normal, hit_index)