class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class VarDecl(ASTNode):
    def __init__(self, name, value):
        self.name  = name
        self.value = value

class Assign(ASTNode):
    def __init__(self, name, value):
        self.name  = name
        self.value = value

class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class If(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition  = condition
        self.then_block = then_block
        self.else_block = else_block

class While(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body      = body

class Return(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class Break(ASTNode):
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left  = left
        self.op    = op
        self.right = right

class Number(ASTNode):
    def __init__(self, value):
        self.value = float(value) if '.' in str(value) else int(value)

class String(ASTNode):
    def __init__(self, value):
        self.value = value.strip('"\'')

class Bool(ASTNode):
    def __init__(self, value):
        self.value = (value == 'bener')

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name