# cod_waw_gsc_lexer
 
Tokenizer for the GSC (Game Scripting Code) language.

## Installation

pass

## Usage

gsc_code = r"""
// This is a single-line comment
/*
This is a,
multi-line comment
*/
myFunc(arg) {
    x = 10; // Initialize x
    if (x > 5) {
        x += 1;
    }
}
"""

gsc_lexer = GscLexer()

tokens = gsc_lexer.tokenize(gsc_code)

print(tokens)

This is a Phils-Hub community-contributed project.