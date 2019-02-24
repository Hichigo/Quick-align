import bpy

from . functions import align_graph

# -----------------------------------------------------------------------------
# node
class NODE_OT_align_x_slots(bpy.types.Operator):
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

class NODE_OT_align_y_slots(bpy.types.Operator):
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
