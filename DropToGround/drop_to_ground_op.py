import bpy

from mathutils import Vector, Matrix

class VIEW3D_OT_drop_to_ground(bpy.types.Operator):
	"""Drop to ground selected objects"""
	bl_idname = "view3d.drop_to_ground"
	bl_label = "Drop to ground"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def get_vector_direction(self, context):
		quick_align = context.scene.quick_align
		direction_drop = quick_align.direction_drop

		vector_result = None
		if direction_drop == "-Z":
			vector_result = Vector((0, 0, -1)) # down
		elif direction_drop == "Z":
			vector_result = Vector((0, 0, 1)) # up
		elif direction_drop == "-X":
			vector_result = Vector((-1, 0, 0)) # backward
		elif direction_drop == "X":
			vector_result = Vector((1, 0, 0)) # forward
		elif direction_drop == "-Y":
			vector_result = Vector((0, -1, 0)) # left
		elif direction_drop == "Y":
			vector_result = Vector((0, 1, 0)) # right
		
		return vector_result

	def drop_individual_objects(self, context, objects, dir, align_by_normal = False):
		vector_drop_direction = self.get_vector_direction(context)
		for ob in objects:
			ob.hide_set(True)
			bHit, pos_hit, normal_hit, face_index_hit, obj_hit, matrix_world = context.scene.ray_cast(
				view_layer=context.view_layer,
				origin=ob.location,
				direction=vector_drop_direction
			)

			ob.hide_set(False)
			ob.select_set(True)

			if bHit:
				loc, rot, scale = ob.matrix_world.decompose()

				loc = Matrix.Translation(pos_hit)

				scale_mat = Matrix.Scale(1, 4)
				scale_mat[0][0] = scale.x
				scale_mat[1][1] = scale.y
				scale_mat[2][2] = scale.z


				# apply rotation by normal
				if align_by_normal:
					rot_by_normal = normal_hit.rotation_difference(Vector((0,0,1)))
					rot_by_normal.invert()
					rot_by_normal = rot_by_normal.to_euler().to_matrix().to_4x4()

					rot = rot_by_normal
				else:
					rot = rot.to_matrix().to_4x4()

				mat_w = loc @ rot @ scale_mat

				ob.matrix_world = mat_w

	def drop_by_active_object(self, context, objects, dir):
		vector_drop_direction = self.get_vector_direction(context)
		active_object = context.active_object

		active_object.hide_set(True)

		bHit, pos_hit, normal_hit, face_index_hit, obj_hit, matrix_world = context.scene.ray_cast(
			view_layer=context.view_layer,
			origin=active_object.location,
			direction=vector_drop_direction
		)

		active_object.hide_set(False)
		active_object.select_set(True)

		if bHit:
			loc, rot, scale = active_object.matrix_world.decompose()

			loc_mat = Matrix.Translation(pos_hit)

			scale_mat = Matrix.Scale(1, 4)
			scale_mat[0][0] = scale.x
			scale_mat[1][1] = scale.y
			scale_mat[2][2] = scale.z

			rot = rot.to_matrix().to_4x4()

			mat_w = loc_mat @ rot @ scale_mat

			active_object.matrix_world = mat_w

			offset_vector = loc - pos_hit

			objects.remove(active_object)
			for ob in objects:
				loc, rot, scale = ob.matrix_world.decompose()

				loc_mat = Matrix.Translation(loc - offset_vector)

				scale_mat = Matrix.Scale(1, 4)
				scale_mat[0][0] = scale.x
				scale_mat[1][1] = scale.y
				scale_mat[2][2] = scale.z

				rot = rot.to_matrix().to_4x4()

				mat_w = loc_mat @ rot @ scale_mat

				ob.matrix_world = mat_w

	def execute(self, context):
		objects = context.selected_objects

		quick_align = context.scene.quick_align
		drop_by = quick_align.drop_by
		direction_drop = quick_align.direction_drop
		align_by_normal = quick_align.align_by_normal


		if drop_by == "ORIGIN":
			self.drop_individual_objects(context, objects, direction_drop, align_by_normal)
		elif drop_by == "ACTIVE":
			self.drop_by_active_object(context, objects, direction_drop)
		# elif drop_by == "3DCURSOR":
		# 	self.report({"INFO"}, "WORK IN PROGRESS!!!")

		return {'FINISHED'}