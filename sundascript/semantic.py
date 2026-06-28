from ast_builder import *

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}
        self.errors       = []

    def analyze(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.analyze(stmt)

        elif isinstance(node, VarDecl):
            self.analyze(node.value)
            self.symbol_table[node.name] = True

        elif isinstance(node, Assign):
            if node.name not in self.symbol_table:
                self.errors.append(f"Variabel '{node.name}' can dipikanyaho (teu dideklarasikeun)")
            self.analyze(node.value)

        elif isinstance(node, Print):
            self.analyze(node.expr)

        elif isinstance(node, If):
            self.analyze(node.condition)
            for s in node.then_block:
                self.analyze(s)
            if node.else_block:
                for s in node.else_block:
                    self.analyze(s)

        elif isinstance(node, While):
            self.analyze(node.condition)
            for s in node.body:
                self.analyze(s)

        elif isinstance(node, Return):
            self.analyze(node.expr)

        elif isinstance(node, BinOp):
            self.analyze(node.left)
            self.analyze(node.right)

        elif isinstance(node, Identifier):
            if node.name not in self.symbol_table:
                self.errors.append(f"Variabel '{node.name}' can dipikanyaho")

    def report(self):
        if self.errors:
            print("\n===== KASALAHAN SEMANTIK =====")
            for e in self.errors:
                print(f"  [ERROR] {e}")
        else:
            print("\n===== Semantik: Teu aya kasalahan =====")