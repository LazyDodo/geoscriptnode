input = nodes.Input("geometry","geometry")
trans = nodes.Vector(1,0,0)
pos = input.attributes.Vector("position")
pos = pos+trans
input.attributes.position = pos
nodes.Output("geometry", input)