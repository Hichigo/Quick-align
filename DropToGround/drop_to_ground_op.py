import bpy

from mathutils import Vector

class VIEW3D_OT_drop_to_ground(bpy.types.Operator):
	"""Drop to ground selected objects"""
	bl_idname = "view3d.drop_to_ground"
	bl_label = "Drop to ground"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		objects = bpy.context.selected_objects

		for ob in objects:
			ob.hide_set(True)
			bHit, pos_hit, normal_hit, face_index_hit, obj_hit, matrix_world = context.scene.ray_cast(
				view_layer=context.view_layer,
				origin=ob.location,
				direction=Vector((0,0,-1))
			)

			ob.hide_set(False)
			ob.select_set(True)

			if bHit:
				ob.location = pos_hit

		return {'FINISHED'}