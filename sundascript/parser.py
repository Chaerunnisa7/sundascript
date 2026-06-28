from ast_builder import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos    = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, kind=None, value=None):
        tok = self.peek()
        if tok is None:
            raise SyntaxError("Token teu aya (end of input)")
        if kind and tok[0] != kind:
            raise SyntaxError(f"Ekspektasi {kind}, meunang {tok[0]} ({tok[1]!r})")
        if value and tok[1] != value:
            raise SyntaxError(f"Ekspektasi '{value}', meunang '{tok[1]}'")
        self.pos += 1
        return tok

    def parse(self):
        stmts = []
        while self.peek():
            stmts.append(self.parse_statement())
        return Program(stmts)

    def parse_statement(self):
        tok = self.peek()
        if tok is None:
            raise SyntaxError("Pernyataan teu lengkep")

        if tok == ('KEYWORD', 'naro'):
            return self.parse_vardecl()
        elif tok == ('KEYWORD', 'cetakkeun'):
            return self.parse_print()
        elif tok == ('KEYWORD', 'lamun'):
            return self.parse_if()
        elif tok == ('KEYWORD', 'bari'):
            return self.parse_while()
        elif tok == ('KEYWORD', 'balik'):
            return self.parse_return()
        elif tok == ('KEYWORD', 'eureun'):
            self.consume()
            self.consume('DELIMITER', ';')
            return Break()
        elif tok[0] == 'IDENTIFIER':
            return self.parse_assign()
        else:
            raise SyntaxError(f"Pernyataan teu dipikanyaho: {tok}")

    def parse_vardecl(self):
        self.consume('KEYWORD', 'naro')
        name = self.consume('IDENTIFIER')[1]
        self.consume('OPERATOR', '=')
        value = self.parse_expr()
        self.consume('DELIMITER', ';')
        return VarDecl(name, value)

    def parse_assign(self):
        name = self.consume('IDENTIFIER')[1]
        self.consume('OPERATOR', '=')
        value = self.parse_expr()
        self.consume('DELIMITER', ';')
        return Assign(name, value)

    def parse_print(self):
        self.consume('KEYWORD', 'cetakkeun')
        expr = self.parse_expr()
        self.consume('DELIMITER', ';')
        return Print(expr)

    def parse_if(self):
        self.consume('KEYWORD', 'lamun')
        self.consume('DELIMITER', '(')
        cond = self.parse_expr()
        self.consume('DELIMITER', ')')
        then_block = self.parse_block()
        else_block = None
        if self.peek() == ('KEYWORD', 'atawa'):
            self.consume()
            else_block = self.parse_block()
        return If(cond, then_block, else_block)

    def parse_while(self):
        self.consume('KEYWORD', 'bari')
        self.consume('DELIMITER', '(')
        cond = self.parse_expr()
        self.consume('DELIMITER', ')')
        body = self.parse_block()
        return While(cond, body)

    def parse_return(self):
        self.consume('KEYWORD', 'balik')
        expr = self.parse_expr()
        self.consume('DELIMITER', ';')
        return Return(expr)

    def parse_block(self):
        self.consume('DELIMITER', '{')
        stmts = []
        while self.peek() and self.peek() != ('DELIMITER', '}'):
            stmts.append(self.parse_statement())
        self.consume('DELIMITER', '}')
        return stmts

    def parse_expr(self):
        return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_additive()
        tok  = self.peek()
        if tok and tok[0] == 'OPERATOR' and tok[1] in ('>', '<', '>=', '<=', '==', '!='):
            op = self.consume()[1]
            right = self.parse_additive()
            return BinOp(left, op, right)
        return left

    def parse_additive(self):
        left = self.parse_multiplicative()
        while self.peek() and self.peek()[0] == 'OPERATOR' and self.peek()[1] in ('+', '-'):
            op    = self.consume()[1]
            right = self.parse_multiplicative()
            left  = BinOp(left, op, right)
        return left

    def parse_multiplicative(self):
        left = self.parse_primary()
        while self.peek() and self.peek()[0] == 'OPERATOR' and self.peek()[1] in ('*', '/'):
            op    = self.consume()[1]
            right = self.parse_primary()
            left  = BinOp(left, op, right)
        return left

    def parse_primary(self):
        tok = self.peek()
        if tok is None:
            raise SyntaxError("Ekspresi teu aya")
        if tok[0] == 'NUMBER':
            self.consume()
            return Number(tok[1])
        elif tok[0] == 'STRING':
            self.consume()
            return String(tok[1])
        elif tok[0] == 'KEYWORD' and tok[1] in ('bener', 'salah'):
            self.consume()
            return Bool(tok[1])
        elif tok[0] == 'IDENTIFIER':
            self.consume()
            return Identifier(tok[1])
        elif tok == ('DELIMITER', '('):
            self.consume()
            expr = self.parse_expr()
            self.consume('DELIMITER', ')')
            return expr
        raise SyntaxError(f"Primary teu dipikanyaho: {tok}")