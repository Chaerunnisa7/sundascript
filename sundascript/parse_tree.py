from ast_builder import *

def print_tree(node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    child_prefix = prefix + ("    " if is_last else "│   ")

    if isinstance(node, Program):
        print(prefix + "Program")
        for i, s in enumerate(node.statements):
            print_tree(s, prefix, i == len(node.statements) - 1)

    elif isinstance(node, VarDecl):
        print(prefix + connector + f"VarDecl: {node.name}")
        print_tree(node.value, child_prefix)

    elif isinstance(node, Assign):
        print(prefix + connector + f"Assign: {node.name}")
        print_tree(node.value, child_prefix)

    elif isinstance(node, Print):
        print(prefix + connector + "cetakkeun")
        print_tree(node.expr, child_prefix)

    elif isinstance(node, If):
        print(prefix + connector + "lamun (if)")
        print_tree(node.condition, child_prefix, False)
        print(child_prefix + "├── then:")
        for s in node.then_block:
            print_tree(s, child_prefix + "│   ")
        if node.else_block:
            print(child_prefix + "└── atawa (else):")
            for s in node.else_block:
                print_tree(s, child_prefix + "    ")

    elif isinstance(node, While):
        print(prefix + connector + "bari (while)")
        print_tree(node.condition, child_prefix, False)
        for s in node.body:
            print_tree(s, child_prefix)

    elif isinstance(node, BinOp):
        print(prefix + connector + f"BinOp: {node.op}")
        print_tree(node.left,  child_prefix, False)
        print_tree(node.right, child_prefix)

    elif isinstance(node, Number):
        print(prefix + connector + f"Number: {node.value}")

    elif isinstance(node, String):
        print(prefix + connector + f'String: "{node.value}"')

    elif isinstance(node, Bool):
        val = "bener" if node.value else "salah"
        print(prefix + connector + f"Bool: {val}")

    elif isinstance(node, Identifier):
        print(prefix + connector + f"Identifier: {node.name}")

    elif isinstance(node, Return):
        print(prefix + connector + "balik (return)")
        print_tree(node.expr, child_prefix)

    elif isinstance(node, Break):
        print(prefix + connector + "eureun (break)")