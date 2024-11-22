import ply.lex as lex
from rich import print

import logging

logging.basicConfig(level=logging.CRITICAL)

common_tokens = (
    'FUNCTION_CALL', 'FUNCTION_DEF', 'FUNCTION_DECL', 'VAR_DECL', 'ASSIGN', 'RETURN',
    'CALCULATIONS', 'IDENTIFIER', 'BRANCH', 'FOR_LOOP', 'WHILE_LOOP',
    'ACCESS_SPECIFIERS', 'CLASS'
)

python_tokens = (
    'PYTHON_DEF', 'PYTHON_CLASS'
)

cpp_tokens = (
    'CPP_INCLUDE', 'CPP_PRINT', 'CPP_EXCLUSIVE_KEYWORDS'
)

java_tokens = (
    'JAVA_EXCLUSIVE_KEYWORDS',
)

# C# specific tokens
csharp_tokens = (
    'CSHARP_USING', 'CSHARP_NAMESPACE', 'CSHARP_CLASS', 'CSHARP_METHOD', 'CSHARP_INTERFACE',
    'CSHARP_ENUM', 'CSHARP_STRUCT', 'CSHARP_PROPERTY', 'CSHARP_EVENT',
    'CSHARP_GET', 'CSHARP_SET', 'CSHARP_ASYNC', 'CSHARP_AWAIT',
    'CSHARP_PUBLIC', 'CSHARP_PRIVATE', 'CSHARP_PROTECTED', 'CSHARP_INTERNAL',
    'CSHARP_OVERRIDE', 'CSHARP_VIRTUAL', 'CSHARP_STATIC', 'CSHARP_CONST',
    'IDENTIFIER', 'FUNCTION_DEF', 'FUNCTION_CALL', 'CLASS'
)

# Haskell specific tokens
haskell_tokens = (
    'HASKELL_MODULE', 'HASKELL_IMPORT', 'HASKELL_WHERE', 'HASKELL_LET', 'HASKELL_IN',
    'HASKELL_DATA', 'HASKELL_TYPE', 'HASKELL_DERIVING', 'HASKELL_CASE',
    'HASKELL_OF', 'HASKELL_DO', 'HASKELL_NEWTYPE',
    'IDENTIFIER', 'FUNCTION_DEF', 'FUNCTION_CALL', 'CLASS', 'ASSIGN'
)

tokens = common_tokens + python_tokens + cpp_tokens + java_tokens + csharp_tokens + haskell_tokens

def t_FUNCTION_CALL(t):
    r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*\(.*\)'
    return t

def t_FUNCTION_DEF(t):
    r'\bdef\b|\bvoid\b|\bfunction\b'
    return t

def t_CLASS(t):
    r'\bclass\b'
    return t

# Python-specific tokens
def t_PYTHON_DEF(t):
    r'\bdef\b'
    return t

def t_PYTHON_CLASS(t):
    r'\bclass\b'
    return t

# C++ specific tokens
def t_CPP_INCLUDE(t):
    r'\#include\s*<.*>'
    return t

def t_CPP_PRINT(t):
    r'cout<<'
    return t

# Java-specific tokens
def t_JAVA_EXCLUSIVE_KEYWORDS(t):
    r'\b(finally|super|this)\b'
    return t

# C# specific tokens
def t_CSHARP_USING(t):
    r'\busing\b'
    return t

def t_CSHARP_NAMESPACE(t):
    r'\bnamespace\b'
    return t

def t_CSHARP_CLASS(t):
    r'\bclass\b'
    return t

def t_CSHARP_METHOD(t):
    r'\bvoid\b|\basync\s+void\b|\bint\b|\bstring\b|\bbool\b|\bTask\b'
    return t

def t_CSHARP_INTERFACE(t):
    r'\binterface\b'
    return t

def t_CSHARP_ENUM(t):
    r'\benum\b'
    return t

def t_CSHARP_STRUCT(t):
    r'\bstruct\b'
    return t

def t_CSHARP_PROPERTY(t):
    r'\b(get|set)\b'
    return t

def t_CSHARP_EVENT(t):
    r'\bevent\b'
    return t

def t_CSHARP_ASYNC(t):
    r'\basync\b'
    return t

def t_CSHARP_AWAIT(t):
    r'\bawait\b'
    return t

def t_CSHARP_PUBLIC(t):
    r'\bpublic\b'
    return t

def t_CSHARP_PRIVATE(t):
    r'\bprivate\b'
    return t

def t_CSHARP_PROTECTED(t):
    r'\bprotected\b'
    return t

def t_CSHARP_INTERNAL(t):
    r'\binternal\b'
    return t

def t_CSHARP_OVERRIDE(t):
    r'\boverride\b'
    return t

def t_CSHARP_VIRTUAL(t):
    r'\bvirtual\b'
    return t

def t_CSHARP_STATIC(t):
    r'\bstatic\b'
    return t

def t_CSHARP_CONST(t):
    r'\bconst\b'
    return t

# Haskell-specific tokens
def t_HASKELL_MODULE(t):
    r'\bmodule\b'
    print(t.type)
    return t

def t_HASKELL_IMPORT(t):
    r'\bimport\b'
    return t

def t_HASKELL_WHERE(t):
    r'\bwhere\b'
    return t

def t_HASKELL_LET(t):
    r'\blet\b'
    return t

def t_HASKELL_IN(t):
    r'\bin\b'
    return t

def t_HASKELL_DATA(t):
    r'\bdata\b'
    return t

def t_HASKELL_TYPE(t):
    r'\btype\b'
    return t

def t_HASKELL_DERIVING(t):
    r'\bderiving\b'
    return t

def t_HASKELL_CASE(t):
    r'\bcase\b'
    return t

def t_HASKELL_OF(t):
    r'\bof\b'
    return t

def t_HASKELL_DO(t):
    r'\bdo\b'
    return t

def t_HASKELL_NEWTYPE(t):
    r'\bnewtype\b'
    return t

# General token rules
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_ASSIGN(t):
    r'='
    return t

def t_RETURN(t):
    r'\breturn\b'
    return t

def t_ignore_WHITESPACE(t):
    r'\s+'
    pass

def t_error(t):
    # print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
# lexer = lex.lex()
lexer = lex.lex(errorlog=logging.getLogger('ply'))

def tokenize(code):
    lexer.input(code)
    tokens_list = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append((tok.type, tok.value))
    
    return tokens_list

def detect_language(tokens_list):
    token_types = [tok[0] for tok in tokens_list]
    print("\nToken List:\n")
    for type in token_types:
        print(f"{type}")
    common_detected =  all([type in common_tokens for type in token_types])
    cpp_detected =  all([type in cpp_tokens for type in token_types])
    python_detected =  all([type in python_tokens for type in token_types])
    java_detected =  all([type in java_tokens for type in token_types])
    csharp_detected =  all([type in csharp_tokens for type in token_types])
    haskell_detected =  all([type in haskell_tokens for type in token_types])
    class_detected = any(tok == 'CLASS' for tok in token_types)

    if common_detected and class_detected:
        return "C++ and Java"
    elif common_detected:
        return "C++, Java and Python"
    elif python_detected:
        return "Python"
    elif cpp_detected:
        return "C++"
    elif java_detected:
        return "Java"
    elif csharp_detected:
        return "C#"
    elif haskell_detected:
        return "Haskell"
    else:
        return "Unable to detect the Language"


# Driver code
code_snippet1 = """
    using System;
    namespace ExampleNamespace {
        public class Example {
            public void Display() {
                Console.WriteLine("Hello, World!");
            }
        }
    }
    """

code_snippet2 = """
    module Example where
    import Data.List

    main :: IO ()
    main = do
        let x = 5
        print x
    """


print("\n[bold purple]---Multi Language Compiler---[/]\n")
# print("")
print("(Press 1 to analyse code snippet 1 and 2 for code snippet 2)")
choice = int(input("Enter your choice: "))
tokens_list = []
if choice == 1:
    tokens_list = tokenize(code_snippet1)
else:
    tokens_list = tokenize(code_snippet2)

# for token in tokens_list:
#     print(f"{token[0]}: {token[1]}")

detected_language = detect_language(tokens_list)
print(f"\n[bold green]Detected Language is:[/] [bold italic blue]{detected_language}[/]\n")
