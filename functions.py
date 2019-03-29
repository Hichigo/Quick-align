import bpy

def align_XYZ(x, y, z, axisX, axisY, axisZ):
	bpy.context.scene.tool_settings.use_transform_pivot_point_align = True

	# piv = bpy.context.space_data.pivot_point
	# scene = bpy.context.scene
	# bpy.context.space_data.pivot_point = scene.regarding

	if bpy.context.mode == 'OBJECT':
		# bpy.context.space_data.use_pivot_point_align = True
		bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), orient_matrix_type='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
		# bpy.context.space_data.use_pivot_point_align = False
	else:
		bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), orient_matrix_type='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

	# bpy.context.space_data.pivot_point = piv
	bpy.context.scene.tool_settings.use_transform_pivot_point_align = False


def align_graph(x, y, z, axisX, axisY, axisZ):
	bpy.ops.transform.resize(value=(x, y, z), constraint_axis=(axisX, axisY, axisZ), orient_matrix_type='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
