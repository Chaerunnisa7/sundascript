from ast_builder import *

class CodeGenerator:
    def __init__(self):
        self.indent_level = 0

    def indent(self):
        return "    " * self.indent_level

    def generate(self, node):
        if isinstance(node, Program):
            lines = []
            for stmt in node.statements:
                lines.append(self.generate(stmt))
            return "\n".join(lines)

        elif isinstance(node, VarDecl):
            return f"{self.indent()}{node.name} = {self.generate(node.value)}"

        elif isinstance(node, Assign):
            return f"{self.indent()}{node.name} = {self.generate(node.value)}"

        elif isinstance(node, Print):
            return f"{self.indent()}print({self.generate(node.expr)})"

        elif isinstance(node, If):
            code = f"{self.indent()}if {self.generate(node.condition)}:\n"
            self.indent_level += 1
            for s in node.then_block:
                code += self.generate(s) + "\n"
            self.indent_level -= 1
            if node.else_block:
                code += f"{self.indent()}else:\n"
                self.indent_level += 1
                for s in node.else_block:
                    code += self.generate(s) + "\n"
                self.indent_level -= 1
            return code.rstrip()

        elif isinstance(node, While):
            code = f"{self.indent()}while {self.generate(node.condition)}:\n"
            self.indent_level += 1
            for s in node.body:
                code += self.generate(s) + "\n"
            self.indent_level -= 1
            return code.rstrip()

        elif isinstance(node, Return):
            return f"{self.indent()}return {self.generate(node.expr)}"

        elif isinstance(node, Break):
            return f"{self.indent()}break"

        elif isinstance(node, BinOp):
            return f"({self.generate(node.left)} {node.op} {self.generate(node.right)})"

        elif isinstance(node, Number):
            return str(node.value)

        elif isinstance(node, String):
            return f'"{node.value}"'

        elif isinstance(node, Bool):
            return "True" if node.value else "False"

        elif isinstance(node, Identifier):
            return node.name

        return ""