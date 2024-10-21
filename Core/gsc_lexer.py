# Token Definitions
tokens = [
    ('SL_COMMENT', '//'),                                    # Single Line Comment
    ('ML_COMMENT_START', '/*'),                             # Multi-line Comment start
    ('ML_COMMENT_END', '*/'),                               # Multi-line Comment end
    ('DEV_COMMENT', '#'),                                   # Developer Comment
    ('NEWLINE', '\n'),                                     # Newline
    ('ESCAPE_CHAR', '\\'),                                  # Escape character
    ('INCLUDE_DIRECTIVE', '#include'),                      # #include directive
    ('ANIMTREE_DIRECTIVE', '#animtree'),                    # #animtree directive
    ('USING_ANIMTREE_DIRECTIVE', '#using_animtree'),        # #using_animtree directive
    ('IDENTIFIER', 'IDENTIFIER'),                            # Identifiers
    ('INT', 'INT'),                                        # Integer
    ('FLOAT', 'FLOAT'),                                     # Floating point number
    ('KEYWORD', 'if'),                                     # Keywords
    ('FUNCTION_REFERENCE', '::'),                           # Function references
    ('STRING', '"'),                                       # String literals
    ('LOCAL_STRING', '&""'),                                # Localized strings
    ('DOT', '.'),                                          # Period
    ('COMMA', ','),                                        # Comma
    ('QUOTE', '"'),                                       # Quote
    ('SEMICOLON', ';'),                                   # Semicolon
    ('LPAREN', '('),                                      # Opening parenthesis
    ('RPAREN', ')'),                                      # Closing parenthesis
    ('LBRACE', '{'),                                      # Opening brace
    ('RBRACE', '}'),                                      # Closing brace
    ('LBRACKET', '['),                                    # Opening bracket
    ('RBRACKET', ']'),                                    # Closing bracket
    ('ADD', '+'),                                         # Addition
    ('SUB', '-'),                                          # Subtraction
    ('MUL', '*'),                                         # Multiplication
    ('DIV', '/'),                                          # Division
    ('INC', '++'),                                       # Increment
    ('DEC', '--'),                                       # Decrement
    ('ASSIGN', '='),                                     # Assignment
    ('EQ', '=='),                                        # Equality
    ('NEQ', '!='),                                       # Inequality
    ('GT', '>'),                                         # Greater than
    ('LT', '<'),                                         # Less than
    ('GE', '>='),                                        # Greater or equal
    ('LE', '<='),                                        # Less or equal
    ('AND', '&&'),                                       # Logical AND
    ('NOT', '!'),                                        # Logical NOT
    ('OR', '||'),                                        # Logical OR
    ('EOF', '$'),                                        # End of file
]

# Ignored tokens (whitespace and comments)
ignored_tokens = [' ', '\t', '\n']

# Tokenizer Function with Line Numbers
def tokenize(code):
    position = 0
    tokens_list = []
    line_number = 1  # Start from line 1

    while position < len(code):
        char = code[position]

        # Check for ignored tokens
        if char in ignored_tokens:
            if char == '\n':
                line_number += 1
            position += 1
            continue

        # Check for SL_COMMENT
        if code.startswith('//', position):
            end_pos = code.find('\n', position)
            if end_pos == -1:  # If no newline, go to end of string
                end_pos = len(code)
            tokens_list.append(('SL_COMMENT', code[position:end_pos], line_number))
            position = end_pos
            continue

        # Check for ML_COMMENT
        if code.startswith('/*', position):
            end_pos = code.find('*/', position)
            if end_pos == -1:  # If no closing, go to end of string
                end_pos = len(code)
            tokens_list.append(('ML_COMMENT_START', code[position:end_pos], line_number))
            position = end_pos + 2  # Skip past '*/'
            continue

        # Check for Developer Comment
        if code.startswith('#', position):
            end_pos = code.find('\n', position)
            if end_pos == -1:
                end_pos = len(code)
            tokens_list.append(('DEV_COMMENT', code[position:end_pos], line_number))
            position = end_pos
            continue

        # Check for INCLUDE_DIRECTIVE
        if code.startswith('#include', position):
            tokens_list.append(('INCLUDE_DIRECTIVE', '#include', line_number))
            position += len('#include')
            continue

        # Check for ANIMTREE_DIRECTIVE
        if code.startswith('#animtree', position):
            tokens_list.append(('ANIMTREE_DIRECTIVE', '#animtree', line_number))
            position += len('#animtree')
            continue

        # Check for IDENTIFIER or keywords
        if char.isalpha() or char == '_':  # Starting character for identifier
            start_pos = position
            while position < len(code) and (code[position].isalnum() or code[position] == '_'):
                position += 1
            identifier = code[start_pos:position]
            # Check for keywords
            if identifier in ('self', 'true', 'false', 'undefined', 'if', 'else', 'while', 'for',
                              'switch', 'case', 'break', 'continue', 'return', 'level', 'thread', 'wait'):
                tokens_list.append(('KEYWORD', identifier, line_number))
            else:
                tokens_list.append(('IDENTIFIER', identifier, line_number))
            continue

        # Check for INT
        if char.isdigit():
            start_pos = position
            while position < len(code) and code[position].isdigit():
                position += 1
            tokens_list.append(('INT', code[start_pos:position], line_number))
            continue

        # Check for FLOAT
        if char.isdigit() and position + 1 < len(code) and code[position] == '.':
            start_pos = position - 1
            position += 1
            while position < len(code) and code[position].isdigit():
                position += 1
            tokens_list.append(('FLOAT', code[start_pos:position], line_number))
            continue

        # Check for STRING
        if char == '"':
            start_pos = position
            position += 1
            while position < len(code) and code[position] != '"':
                if code[position] == '\\':  # Escape character
                    position += 1  # Skip escape character
                position += 1
            position += 1  # Skip closing quote
            tokens_list.append(('STRING', code[start_pos:position], line_number))
            continue

        # Check for SEMICOLON, COMMA, etc.
        simple_tokens = {
            ';': 'SEMICOLON', ',': 'COMMA', '(': 'LPAREN', ')': 'RPAREN',
            '{': 'LBRACE', '}': 'RBRACE', '[': 'LBRACKET', ']': 'RBRACKET',
            '+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV', 
            '=': 'ASSIGN', '==': 'EQ', '!=': 'NEQ', '>': 'GT',
            '<': 'LT', '>=': 'GE', '<=': 'LE', '&&': 'AND',
            '||': 'OR', '!': 'NOT', '++': 'INC', '--': 'DEC'
        }
        
        if char in simple_tokens:
            token_type = simple_tokens[char]
            tokens_list.append((token_type, char, line_number))
            position += 1
            continue

        # If the character doesn't match any known tokens, raise an error
        raise SyntaxError(f'Unexpected character: {char} at line {line_number}')

    tokens_list.append(('EOF', '$', line_number))  # End of file token
    return tokens_list

if __name__ == '__main__':
    # Example usage
    code = """
    #include maps\\_utility;
    myVar = 10;
    myFunc(arg) {
        // Single-line comment
        /* Multi-line comment */
        str = &"";
        if (myVar == 10) {
            myFunc = ::myFunc;
        }
    }
    """

    tokens_list = tokenize(code)
    for token in tokens_list:
        print(token)
