import bpy

from . functions import align_graph

# -----------------------------------------------------------------------------
# uv
class UV_OT_align_x_slots(bpy.types.Operator):
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

class UV_OT_align_y_slots(bpy.types.Operator):
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
