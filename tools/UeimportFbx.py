import unreal
import json

def _unreal_import_fbx_asset(input_path, destination_path, destination_name):
    """
    Import an FBX into Unreal Content Browser
    :param input_path: The fbx file to import
    :param destination_path: The Content Browser path where the asset will be placed
    :param destination_name: The asset name to use; if None, will use the filename without extension
    """
    tasks = []
    tasks.append(_generate_fbx_import_task(input_path, destination_path,
                                           destination_name,animations=True,automated=True))

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

    first_imported_object = None

    for task in tasks:
        unreal.log("Import Task for: {}".format(task.filename))
        for object_path in task.imported_object_paths:
            unreal.log("Imported object: {}".format(object_path))
            if not first_imported_object:
                first_imported_object = object_path

    return first_imported_object


def _generate_fbx_import_task(filename, destination_path, destination_name=None, replace_existing=False,
                              automated=False, save=False, materials=False,
                              textures=False, as_skeletal=False,animations=False):
    """
    Create and configure an Unreal AssetImportTask
    :param filename: The fbx file to import
    :param destination_path: The Content Browser path where the asset will be placed
    :return the configured AssetImportTask
    """
    task = unreal.AssetImportTask()
    task.filename = filename
    task.destination_path = destination_path

    # By default, destination_name is the filename without the extension
    if destination_name is not None:
        task.destination_name = destination_name

    task.replace_existing = replace_existing
    task.automated = automated
    task.save = save

    task.options = unreal.FbxImportUI()
    task.options.import_materials = materials
    task.options.import_textures = textures
    task.options.import_as_skeletal = as_skeletal
    task.options.import_animations = animations
    # task.options.import_mesh = True
    # task.options.static_mesh_import_data.combine_meshes = True
    # task.options.

    task.options.mesh_type_to_import = unreal.FBXImportType.FBXIT_STATIC_MESH
    if as_skeletal:
        task.options.mesh_type_to_import = unreal.FBXImportType.FBXIT_SKELETAL_MESH

    return task


_unreal_import_fbx_asset("D:\\shot_ep020_sc0072_Anm_fbx_v0001__huang-zhi-cong__YeYu.fbx", "/Game/test", "test")
