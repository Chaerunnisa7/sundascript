import re

# ============================================================
#  DESAIN BAHASA SUNDASCRIPT
#  Keyword Sunda:
#    naro       = deklarasi variabel  (var)
#    cetakkeun  = print
#    asupkeun   = input
#    lamun      = if
#    atawa      = else
#    bari       = while
#    eureun     = break
#    balik      = return
#    jieun      = def (fungsi)
#    bener      = True
#    salah      = False
# ============================================================

KEYWORDS = {
    'naro', 'cetakkeun', 'asupkeun',
    'lamun', 'atawa', 'bari',
    'eureun', 'balik', 'jieun',
    'bener', 'salah'
}

# 7 jenis token:
# 1. KEYWORD    - kata kunci bahasa
# 2. IDENTIFIER - nama variabel/fungsi
# 3. NUMBER     - angka
# 4. STRING     - teks
# 5. OPERATOR   - +, -, *, /, =, ==, !=, <, >, <=, >=
# 6. DELIMITER  - ; , ( ) { }
# 7. BOOLEAN    - bener / salah

TOKEN_SPEC = [
    ('NUMBER',     r'\d+(\.\d+)?'),
    ('STRING',     r'"[^"]*"|\'[^\']*\''),
    ('BOOLEAN',    r'\b(?:bener|salah)\b'),
    ('KEYWORD',    r'\b(?:' + '|'.join(KEYWORDS - {'bener','salah'}) + r')\b'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('OPERATOR',   r'==|!=|<=|>=|[+\-*/=<>]'),
    ('DELIMITER',  r'[;,\(\)\{\}]'),
    ('SKIP',       r'[ \t\n\r]+'),
    ('COMMENT',    r'//[^\n]*'),
    ('MISMATCH',   r'.'),
]

TOKEN_RE = re.compile(
    '|'.join(f'(?P<{name}>{pat})' for name, pat in TOKEN_SPEC)
)

def tokenize(code):
    tokens = []
    for mo in TOKEN_RE.finditer(code):
        kind  = mo.lastgroup
        value = mo.group()
        if kind in ('SKIP', 'COMMENT'):
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"[LEXER ERROR] Karakter teu dipikanyaho: {value!r}")
        tokens.append((kind, value))
    return tokens