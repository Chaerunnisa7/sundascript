from lexer          import tokenize
from parser         import Parser
from semantic       import SemanticAnalyzer
from optimizer      import Optimizer
from code_generator import CodeGenerator
from parse_tree     import print_tree

def run():
    print("=== COMPILER SUNDASCRIPT ===")
    print("Tulis program SundaScript di handap ieu.")
    print("Pencet Enter sababaraha kali.")
    print("Ketik SELESAI pikeun compile.")
    print("Ketik KALUAR pikeun kaluar.")
    print()
    print("Keyword Sunda:")
    print("  naro x = 5;          → deklarasi variabel")
    print("  cetakkeun x;         → print")
    print("  lamun (x > 3) { }    → if")
    print("  atawa { }            → else")
    print("  bari (x < 10) { }   → while")
    print("  eureun;              → break")
    print("  balik x;             → return")
    print("  bener / salah        → True / False")
    print()

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "KALUAR":
            print("Hatur nuhun! Sampai jumpa!")
            return
        if line.strip() == "SELESAI":
            break
        lines.append(line)

    code = "\n".join(lines)
    if not code.strip():
        print("Teu aya program anu diasupkeun.")
        return

    print("\n" + "="*40)
    print("KODE SUMBER:")
    print(code)
    print("="*40)

    # ── 1. LEXER ──────────────────────────────
    try:
        tokens = tokenize(code)
    except SyntaxError as e:
        print(f"\n[LEXER ERROR] {e}")
        return

    print("\n===== JENIS TOKEN =====")
    seen = set()
    for kind, _ in tokens:
        seen.add(kind)
    for k in seen:
        print(f"  {k}")
    print(f"\nJumlah Jenis Token = {len(seen)}")

    print("\n===== TOKEN =====")
    for t in tokens:
        print(f"  {t}")

    # ── 2. PARSER ─────────────────────────────
    try:
        ast = Parser(tokens).parse()
    except SyntaxError as e:
        print(f"\n[PARSER ERROR] {e}")
        return

    print("\n===== PARSE TREE =====")
    print_tree(ast)

    # ── 3. SEMANTIC ───────────────────────────
    sem = SemanticAnalyzer()
    sem.analyze(ast)
    sem.report()
    print(f"\nSimbol anu kapanggih: {list(sem.symbol_table.keys())}")

    # ── 4. OPTIMIZER ──────────────────────────
    opt_ast = Optimizer().optimize(ast)
    print("\n===== Optimizer: Constant Folding geus dijalankeun =====")

    # ── 5. CODE GENERATOR ─────────────────────
    py_code = CodeGenerator().generate(opt_ast)
    print("\n===== KODE PYTHON (HASIL KOMPILASI) =====")
    print(py_code)

    # ── 6. EXECUTE ────────────────────────────
    print("\n===== OUTPUT PROGRAM =====")
    try:
        exec(py_code, {})
    except Exception as e:
        print(f"[RUNTIME ERROR] {e}")

if __name__ == "__main__":
    run()