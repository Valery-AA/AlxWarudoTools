import importlib
from .AlxModuleManager import (
    Alx_Module_Manager
)

import bpy


bl_info = {
    "name": "AlxWarudoTools",
    "author": "Valeria Bosco[Valy Arhal]",
    "description": "",
    "warning": "",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "category": "3D View",
    "location": "",
    "doc_url": "https://github.com/Valery-AA/AlxWarudoTools/wiki",
    "tracker_url": "https://github.com/Valery-AA/AlxWarudoTools/issues",
}


module_loader = Alx_Module_Manager(__path__, globals())


def register():
    module_loader.developer_register_modules()
    module_loader.developer_process_module_keymaps()

    bpy.context.preferences.use_preferences_save = True


def unregister():
    module_loader.developer_unregister_modules()


if __name__ == "__main__":
    register()
