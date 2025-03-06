import ply.lex as lex


tokens = (
    "SELECT", "WHERE", "LIMIT",
    "VAR", "PREFIX", "COLON", "IRI",
    "DOT", "LBRACE", "RBRACE",
    "STRING", "NUMBER", "A"
)

# Expressões regulares para tokens reservados
def t_SELECT(t):
    r'select'
    return t

def t_WHERE(t):
    r'where'
    return t

def t_LIMIT(t):
    r'LIMIT'
    return t

def t_A(t):
    r'a'
    return t


t_DOT = r'\.'
t_COLON = r':'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Token para variáveis (ex: ?nome, ?desc)
def t_VAR(t):
    r'\?[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Token para prefixos (ex: dbo, foaf)
def t_PREFIX(t):
    r'[a-zA-Z]+'
    return t

# Token para IRIs completas (ex: MusicalArtist, name, artist)
def t_IRI(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Token para strings (ex: "Chuck Berry"@en)
def t_STRING(t):
    r'\"[^\"]*\"(@[a-zA-Z]+)?'
    return t

# Token para números (ex: 1000)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços e quebras de linha
t_ignore = " \t\n"


def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

test_query = '''
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
'''

lexer.input(test_query)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
