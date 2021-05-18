bl_info = {
    "name": "Geo PyNode",
    "author": (
        "LazyDodo"
     ),
    "version": (0, 0, 1,0),
    "blender": (2, 92, 0),
    "location": "Nodes > Add nodes",
    "description": "geo nodes python script node",
    "warning": "",
    "wiki_url": "",
    "category": "Node"} 

import sys
from pathlib import Path

sys.path.append(Path(__file__).parent / "shadercore")

from .shaderbuilder import ShaderBuilder
from .geometrytreebuilder import GeometryTreeBuilder
import bpy,nodeitems_utils, glob
from nodeitems_utils import NodeCategory, NodeItem

class ShaderNode_GeoPyNode(bpy.types.ShaderNodeCustomGroup):
    bl_name='ShaderNode_GeoPyNode'
    bl_label='py_script'
    bl_icon='NONE'

    def mypropUpdate(self, context):
        self.UpdateScript()
        return None

    def reloads(self, context):
        try:
            self.UpdateScript()
        except Exception as e:
            import traceback
            traceback.print_exc()

    def UpdateScript(self):
        if self.ScriptType == "INTERNAL":
            if (bpy.data.texts.find(self.script.strip()) != -1 ):
                data = bpy.data.texts[self.script.strip()].as_string()
                shared_globals = dict()
                shader = ShaderBuilder()
                shared_globals["nodes"] = shader
                exec(data, shared_globals)
                shader.PrintProgram()
                builder = GeometryTreeBuilder(shader.shader_program)
                self.node_tree = builder.generate()
            else:
                print("geonodes: Script '%s' not found" % self.script)
                return
        else:
            print(self.extScript)


    script : bpy.props.StringProperty(
            update=mypropUpdate
            )
    extScript : bpy.props.StringProperty(
            subtype="FILE_PATH",
            update=reloads
            )
    ScriptType : bpy.props.EnumProperty(
            name="Script Type",
            description="Script Type",
            items=[
                ("INTERNAL", "Internal", "Internal Script"),
                ("EXTERNAL", "External", "External Script")
                ]
            , update=reloads
            )

    reloading : bpy.props.BoolProperty(default=False, update=reloads)

    #def treename(self):
    #    return self.name;
    
    def init(self, context):
        pass
        #self.getNodetree(self.treename())
    
    def draw_buttons(self, context, layout):
        layout.label(text="Node settings")
        layout.prop(self, "ScriptType", expand=True)
        if not self.node_tree == None:
            layout.label(text=self.node_tree.name)

        split = layout.split(factor=0.85, align=True)
        box = split.box()
        if self.ScriptType == "INTERNAL":
            box.prop_search(self, "script", bpy.data, "texts")
        else:
            box.prop(self, "extScript")

        sub_box = split.box()
        sub_box.prop(self, "reloading", text="", emboss=False, icon="FILE_REFRESH")

    @classmethod
    def poll(cls, context):
        return True
            
  
class ExtraNodesCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        print(context.space_data.tree_type)
        return (context.space_data.tree_type == 'GeometryNodeTree')
 
node_categories = [
    ExtraNodesCategory("SH_GeoNodeScript", "NodeBuilder", items=[
        NodeItem("ShaderNode_GeoPyNode")
        ]),
    ]
      
def register():
    bpy.utils.register_class(ShaderNode_GeoPyNode)
    nodeitems_utils.register_node_categories("SH_GeoNodeScript", node_categories)
 
 
def unregister():
    nodeitems_utils.unregister_node_categories("SH_GeoNodeScript")
    bpy.utils.unregister_class(ShaderNode_GeoPyNode)

if __name__ == "__main__":
    register()
   
