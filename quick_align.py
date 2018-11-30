bl_info = {
	"name": "Quick align",
	"author": "Nexus Studio",
	"version": (0, 7, 1),
	"blender": (2, 80, 0),
	"location": "View3D / Graph Editor / Node Editor / Image Editor > alt-Q key",
	"description": "Quick alignment on axis and fast set origin",
	"wiki_url": "none",
	"category": "User",
}

import bpy

from bpy.props import StringProperty, BoolProperty, EnumProperty

def align_XYZ(x, y, z, axisX, axisY, axisZ):
	# piv = bpy.context.space_data.pivot_point
	# scene = bpy.context.scene
	# bpy.context.space_data.pivot_point = scene.regarding

	if bpy.context.mode == 'OBJECT':
		# bpy.context.space_data.use_pivot_point_align = True
		bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
		# bpy.context.space_data.use_pivot_point_align = False
	else:
		bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

	# bpy.context.space_data.pivot_point = piv


def align_graph(x, y, z, axisX, axisY, axisZ):
	bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

#Pivot point

class ObjectSetOrigin(bpy.types.Operator):
	"""Fast set origin to active vertex / polygon / edge"""
	bl_idname = "view3d.set_origin"
	bl_label = "Set origin to active vertex / polygon / edge"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		if (bpy.context.mode == 'EDIT_MESH') or (bpy.context.mode ==  'EDIT_CURVE'):
			cursor_location_temp = (bpy.context.scene.cursor_location.x,bpy.context.scene.cursor_location.y, bpy.context.scene.cursor_location.z);
			bpy.ops.view3d.snap_cursor_to_selected();
			bpy.ops.object.editmode_toggle();
			bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR');
			bpy.context.scene.cursor_location = cursor_location_temp;
			#bpy.ops.object.editmode_toggle()
		elif bpy.context.mode == 'OBJECT':
			bpy.ops.object.origin_set(type = 'ORIGIN_GEOMETRY');

		return {'FINISHED'}


# -----------------------------------------------------------------------------
# View 3d
class VIEW3D_align_all_axis(bpy.types.Operator):
	"""the alignment along the x-axis in view 3d (object or edit mode)"""
	bl_idname = "view3d.align_all_axis"
	bl_label = "Align x"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_XYZ(0,0,0,True,True,True)
		return {'FINISHED'}

class VIEW3D_align_x_slots(bpy.types.Operator):
	"""the alignment along the x-axis in view 3d (object or edit mode)"""
	bl_idname = "view3d.align_x_slots"
	bl_label = "Align x"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_XYZ(0,1,1,True,False,False)
		return {'FINISHED'}

class VIEW3D_align_y_slots(bpy.types.Operator):
	"""the alignment along the y-axis in view 3d (object or edit mode)"""
	bl_idname = "view3d.align_y_slots"
	bl_label = "Align y"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_XYZ(1,0,1,False,True,False)
		return {'FINISHED'}

class VIEW3D_align_z_slots(bpy.types.Operator):
	"""the alignment along the z-axis in view 3d (object or edit mode)"""
	bl_idname = "view3d.align_z_slots"
	bl_label = "Align z"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_XYZ(1,1,0,False,False,True)
		return {'FINISHED'}

# -----------------------------------------------------------------------------
# Graph
class GRAPH_align_x_slots(bpy.types.Operator):
	"""the alignment along the x-axis in graph editor"""
	bl_idname = "graph.align_x_slots"
	bl_label = "Align x"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_graph(0,1,1,True,False,False)
		return {'FINISHED'}

class GRAPH_align_y_slots(bpy.types.Operator):
	"""the alignment along the y-axis in graph editor"""
	bl_idname = "graph.align_y_slots"
	bl_label = "Align y"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_graph(1,0,1,False,True,False)
		return {'FINISHED'}

# -----------------------------------------------------------------------------
# uv
class UV_align_x_slots(bpy.types.Operator):
	"""the alignment along the x-axis in uv editor"""
	bl_idname = "uv.align_x_slots"
	bl_label = "Align x"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_graph(0,1,1,True,False,False)
		return {'FINISHED'}

class UV_align_y_slots(bpy.types.Operator):
	"""the alignment along the y-axis in uv editor"""
	bl_idname = "uv.align_y_slots"
	bl_label = "Align y"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_graph(1,0,1,False,True,False)
		return {'FINISHED'}

# -----------------------------------------------------------------------------
# node
class NODE_align_x_slots(bpy.types.Operator):
	"""the alignment along the x-axis in node editor"""
	bl_idname = "node.align_x_slots"
	bl_label = "Align x"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_graph(0,1,1,True,False,False)
		return {'FINISHED'}

class NODE_align_y_slots(bpy.types.Operator):
	"""the alignment along the y-axis in node editor"""
	bl_idname = "node.align_y_slots"
	bl_label = "Align y"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		align_graph(1,0,1,False,True,False)
		return {'FINISHED'}

# -----------------------------------------------------------------------------
# menu classes
class view3d_menu(bpy.types.Menu):
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator(VIEW3D_align_all_axis.bl_idname, text="Align all axis", icon='EMPTY_AXIS')
		layout.operator(VIEW3D_align_x_slots.bl_idname, text="X align", icon='EVENT_X')
		layout.operator(VIEW3D_align_y_slots.bl_idname, text="Y align", icon='EVENT_Y')
		layout.operator(VIEW3D_align_z_slots.bl_idname, text="Z align", icon='EVENT_Z')
		layout.operator(ObjectSetOrigin.bl_idname, text="SetOrigin", icon='OBJECT_ORIGIN')
		layout.menu(align_submenu.bl_idname, text="Align by")

class graph_menu(bpy.types.Menu):
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator(GRAPH_align_x_slots.bl_idname, text="X align", icon='EVENT_X')
		layout.operator(GRAPH_align_y_slots.bl_idname, text="Y align", icon='EVENT_Y')

class uv_menu(bpy.types.Menu):
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator(UV_align_x_slots.bl_idname, text="X align", icon='EVENT_X')
		layout.operator(UV_align_x_slots.bl_idname, text="Y align", icon='EVENT_Y')

class node_menu(bpy.types.Menu):
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator(NODE_align_x_slots.bl_idname, text="X align", icon='EVENT_X')
		layout.operator(NODE_align_x_slots.bl_idname, text="Y align", icon='EVENT_Y')

class align_submenu(bpy.types.Menu):
	bl_idname = "alignsubmenu"
	bl_label = "Quick align"

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.prop(scene, "regarding", expand=True)

#class panel
class QuickAlignPanel(bpy.types.Panel):
	"""Creates a Panel in the view3d context of the tools panel (key "T")"""
	bl_label = "Quick align"
	bl_idname = "quickalignid"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = "Nexus Tools"

	itemsEnum = [
		("ACTIVE_ELEMENT", "Active element", ""),
		("MEDIAN_POINT", "Median point", ""),
		("CURSOR", "3D Cursor", "")
	]

	bpy.types.Scene.regarding = EnumProperty(items=itemsEnum)

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		box = layout.box()
		box.label(text="Align by:")
		col = box.column()
		col.prop(scene, "regarding", expand=True)

addon_keymaps = []
keymapsList = [
	{
		'name_view': "3D View",
		'space_type': "VIEW_3D",
		'prop_name': "view3d_menu"
	},
	{
		'name_view': "Image",
		'space_type': "IMAGE_EDITOR",
		'prop_name': "uv_menu"
	},
	{
		'name_view': "Graph Editor",
		'space_type': "GRAPH_EDITOR",
		'prop_name': "graph_menu"
	},
	{
		'name_view': "Node Editor",
		'space_type': "NODE_EDITOR",
		'prop_name': "node_menu"
	}
]

classes = (
	ObjectSetOrigin,
	VIEW3D_align_all_axis,
	VIEW3D_align_x_slots,
	VIEW3D_align_y_slots,
	VIEW3D_align_z_slots,
	GRAPH_align_x_slots,
	GRAPH_align_y_slots,
	UV_align_x_slots,
	UV_align_y_slots,
	NODE_align_x_slots,
	NODE_align_y_slots,
	view3d_menu,
	graph_menu,
	uv_menu,
	node_menu,
	align_submenu
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
