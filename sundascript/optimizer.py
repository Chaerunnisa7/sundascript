from ast_builder import *

class Optimizer:
    def optimize(self, node):
        if isinstance(node, Program):
            node.statements = [self.optimize(s) for s in node.statements]
        elif isinstance(node, VarDecl):
            node.value = self.optimize(node.value)
        elif isinstance(node, Assign):
            node.value = self.optimize(node.value)
        elif isinstance(node, Print):
            node.expr = self.optimize(node.expr)
        elif isinstance(node, If):
            node.condition  = self.optimize(node.condition)
            node.then_block = [self.optimize(s) for s in node.then_block]
            if node.else_block:
                node.else_block = [self.optimize(s) for s in node.else_block]
        elif isinstance(node, While):
            node.condition = self.optimize(node.condition)
            node.body      = [self.optimize(s) for s in node.body]
        elif isinstance(node, Return):
            node.expr = self.optimize(node.expr)
        elif isinstance(node, BinOp):
            node.left  = self.optimize(node.left)
            node.right = self.optimize(node.right)
            # Constant folding
            if isinstance(node.left, Number) and isinstance(node.right, Number):
                l, r = node.left.value, node.right.value
                if node.op == '+': return Number(l + r)
                if node.op == '-': return Number(l - r)
                if node.op == '*': return Number(l * r)
                if node.op == '/' and r != 0: return Number(l / r)
        return node