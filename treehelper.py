import bpy 

class TreeHelper:
    def __init__(self):
        self.variables = {} 
        self.createNodetree("geonodes")

    def register_variable(self, socket, name):
        self.variables[name] = socket

    def createNodetree(self, name):
        self.node_tree = bpy.data.node_groups.new(name, 'GeometryNodeTree')
        self.addNode('NodeGroupInput', {'name': 'GroupInput'})
        self.addNode('NodeGroupOutput', {'name': 'GroupOutput'})
        return self.node_tree

    def getNodetree(self):
        return self.node_tree

    def addInputSocket(self, sockettype, name):
        tmp = self.addSocket(False, sockettype, name)
        self.register_variable(tmp,name)
        return tmp

    def addOutputSocket(self, variable_name, name):
        SI = self.variables[variable_name]
        SO = self.addSocket(True, SI.bl_idname, name)
        self.Link(SI, SO)
        return 

    def addSocket(self, is_output, sockettype, name):
        if is_output==True:
            if self.node_tree.nodes['GroupOutput'].inputs.find(name)==-1:
                self.node_tree.outputs.new(sockettype, name)
            idx = self.node_tree.nodes['GroupOutput'].inputs.find(name)
            socket = self.node_tree.nodes['GroupOutput'].inputs[idx]
        elif is_output==False:
            if self.node_tree.nodes['GroupInput'].outputs.find(name)==-1:
                self.node_tree.inputs.new(sockettype, name)
            idx = self.node_tree.nodes['GroupInput'].outputs.find(name)
            socket = self.node_tree.nodes['GroupInput'].outputs[idx]
        return socket
       
    def addNode(self, nodetype, attrs):
        node=self.node_tree.nodes.new(nodetype)
        for attr in attrs:
            self.value_set(node, attr, attrs[attr])
        return node
   
    def getNode(self, nodename):
        if self.node_tree.nodes.find(nodename)>-1:
            return self.node_tree.nodes[nodename]
        return None

    def Link(self, name_in, name_out):
        if isinstance(name_in, bpy.types.NodeSocket):
            SI = name_in
        else:
            SI = self.variables[name_in]
        
        if isinstance(name_out, bpy.types.NodeSocket):
            SO = name_out
        else:
            SO = self.variables[name_out]
        self.node_tree.links.new(SO,SI)

    def innerLink(self, socketin, socketout):
        print(f'innerLink {socketin} -> {socketout}')        
        SI=self.node_tree.path_resolve(socketin)
        SO=self.node_tree.path_resolve(socketout)
        print(f'innerLink {SO} -> {SI}')        
        self.node_tree.links.new(SI, SO)
       
    def free(self):
        if self.node_tree.users==1:
            bpy.data.node_groups.remove(self.node_tree, do_unlink=True)

    def value_set(self, obj, path, value):
        if '.' in path:
            path_prop, path_attr = path.rsplit('.', 1)
            prop = obj.path_resolve(path_prop)
        else:
            prop = obj
            path_attr = path
        setattr(prop, path_attr, value)
