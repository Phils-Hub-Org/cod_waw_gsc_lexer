import re

# Token definitions (same as yours)
tokens = [
    ('SL_COMMENT', r'//.*'),                                # Single Line Comment
    ('ML_COMMENT', r'/\*[\s\S]*?\*/'),                      # Multi-line Comment
    ('DEV_COMMENT', r'/#.*?#/'),                            # Developer Comment
    ('NEWLINE', r'\n'),                                     # Newline
    ('ESCAPE_CHAR', r'\\'),                                 # Escape character, especially in paths
    ('INCLUDE_DIRECTIVE', r'#include'),                     # #include directive
    ('ANIMTREE_DIRECTIVE', r'#animtree'),                   # #animtree directive
    ('USING_ANIMTREE_DIRECTIVE', r'#using_animtree'),       # #using_animtree directive
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),              # Identifiers
    ('INT', r'\d+'),                                        # Integer
    ('FLOAT', r'\d+\.\d+'),                                 # Floating point number
    ('KEYWORD', r'\b(self|true|false|undefined|if|else|while|for|switch|case|break|continue|return|level|thread|wait)\b'),   # Keywords
    ('FUNCTION_REFERENCE', r'::[a-zA-Z_][a-zA-Z0-9_]*'),    # Function references
    ('POINTER_FUNCTION_LBRACES', r'\[\['),                  # Pointer function opening braces
    ('POINTER_FUNCTION_RBRACES', r'\]\]'),                  # Pointer function closing braces
    ('STRING', r'"[^"]*"'),                                 # String literals
    ('LOCAL_STRING', r'&"[^"]*"'),                          # Localized strings
    ('DOT', r'\.'),                                         # Period
    ('COMMA', r','),                                        # Comma
    ('QUOTE', r'"'),                                        # Quote
    ('SEMICOLON', r';'),                                    # Semicolon
    ('LPAREN', r'\('),                                      # Opening parenthesis
    ('RPAREN', r'\)'),                                      # Closing parenthesis
    ('LBRACE', r'\{'),                                      # Opening brace
    ('RBRACE', r'\}'),                                      # Closing brace
    ('LBRACKET', r'\['),                                    # Opening bracket
    ('RBRACKET', r'\]'),                                    # Closing bracket
    ('ADD', r'\+'),                                         # Addition
    ('SUB', r'-'),                                          # Subtraction
    ('MUL', r'\*'),                                         # Multiplication
    ('EXP', r'\*\*'),                                       # Exponentiation
    ('DIV', r'/'),                                          # Division
    ('MOD', r'%'),                                          # Modulus
    ('INC', r'\+\+'),                                       # Increment
    ('DEC', r'--'),                                         # Decrement
    ('ASSIGN', r'='),                                       # Assignment
    ('EQ', r'=='),                                          # Equality
    ('NEQ', r'!='),                                         # Inequality
    ('GT', r'>'),                                           # Greater than
    ('LT', r'<'),                                           # Less than
    ('GE', r'>='),                                          # Greater or equal
    ('LE', r'<='),                                          # Less or equal
    ('ADD_ASSIGN', r'\+='),                                 # Addition assignment
    ('SUB_ASSIGN', r'-='),                                  # Subtraction assignment
    ('MUL_ASSIGN', r'\*='),                                 # Multiplication assignment
    ('DIV_ASSIGN', r'/='),                                  # Division assignment
    ('AND', r'&&'),                                         # Logical AND
    ('NOT', r'!'),                                          # Logical NOT
    ('OR', r'\|\|'),                                        # Logical OR
    ('EOF', r'$'),                                          # End of file
]

# Function to test the regex patterns
def test_tokens():
    test_cases = [
        ("// This is a comment", 'SL_COMMENT'),
        ("/** This is a multi-line comment **/", 'ML_COMMENT'),
        ("/# Developer comment #/", 'DEV_COMMENT'),
        ("#include", 'INCLUDE_DIRECTIVE'),
        ("#animtree", 'ANIMTREE_DIRECTIVE'),
        ("myVar", 'IDENTIFIER'),
        ("42", 'INT'),
        ("3.14", 'FLOAT'),
        ("if", 'KEYWORD'),
        ('"Hello World"', 'STRING'),
        ('&"Localized String"', 'LOCAL_STRING'),
        ("{", 'LBRACE'),
        ("}", 'RBRACE'),
        ("(", 'LPAREN'),
        (")", 'RPAREN'),
        ("++", 'INC'),
        ("==", 'EQ'),
        ("!", 'NOT'),
        ("&&", 'AND'),
        ("||", 'OR'),
        ("myFunc", 'IDENTIFIER'),  # Check for identifier with parentheses
    ]

    for input_string, expected_token in test_cases:
        matched = False
        for token_type, regex in tokens:
            if re.fullmatch(regex, input_string):
                matched = True
                # print(f"Input: {input_string} | Matched: {token_type} | Expected: {expected_token}")
                if token_type != expected_token:
                    print(f"  **Warning**: Expected {expected_token}, but got {token_type}")
                break
        if not matched:
            print(f"Input: {input_string} | No match found")

# Run the tests
test_tokens()
