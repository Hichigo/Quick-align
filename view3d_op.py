import bpy

from . functions import align_XYZ


# -----------------------------------------------------------------------------
# View 3d
class VIEW3D_OT_align_all_axis(bpy.types.Operator):
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

class VIEW3D_OT_align_x_slots(bpy.types.Operator):
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

class VIEW3D_OT_align_y_slots(bpy.types.Operator):
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

class VIEW3D_OT_align_z_slots(bpy.types.Operator):
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