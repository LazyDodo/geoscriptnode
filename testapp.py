from shaderbuilder import *

class RunScript:
     def run(self):
         str = open('testscript.py', 'r').read()
         print(str)
         shader = ShaderBuilder()
         exec(str)
         shader.PrintProgram()

x = RunScript()
x.run()        