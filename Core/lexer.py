"""
Lexer (Lexical Analyzer)

The purpose of the lexer is to break down the input code (GSC) into smaller, manageable components known as "tokens".
A token can be a keyword, operator, identifier, or symbol (e.g., `int`, `+`, `while`, `{`, `}`, etc.).
This tokenization process allows a parser to understand the structure of the code more easily by focusing on individual parts.

Lexing and Parsing are two separate processes. You can check out our parser repository for more information.

The lexer scans through the input code character by character, groups them into tokens, and assigns a type (e.g., identifier, number, operator) to each token.
It effectively reduces the complexity of the input code by producing a list of tokens, making it easier for a parser to analyze and process.

Steps:
1. Take input code (GSC).
2. Scan characters to create tokens.
3. Return list of tokens.

Class Attributes:
- `code`: The source code (GSC) to be tokenized.
- `position`: The current character position in the input.
- `tokens`: The list of generated tokens.
- `lineNumber`: The current line number.

Methods:
tokenize(inputCode: str, ignoreComments: bool = True)`: Breaks down the entire code into tokens.
- `getNextToken()`: Returns the next token in the input.

Whitespaces are ignored by the lexer.

Comments can sometimes be needed, and sometimes not, so you can decide whether to tokenize comments or not via the parameter: `ignoreComments`. This parameter is set to `True` by default.

Note: A newline '\n' is treated as a single character when iterating through a string.
"""

class Lexer:

    CODE: str
    POSITION: int
    TOKENS: list
    LINE_NUMBER: int

    @classmethod
    def currPos(cls) -> int:
        # Return the current position
        return cls.POSITION
    
    @classmethod
    def incrementPosition(cls, amount: int=1) -> None:
        # Move the position forward
        cls.POSITION += amount
    
    @classmethod
    def currChar(cls) -> str:
        # Return the current character
        return cls.CODE[cls.POSITION]
    
    @classmethod
    def nextChar(cls) -> str:
        # Return the next character
        return cls.CODE[cls.POSITION + 1]

    @classmethod
    def isCurrChar(cls, char: str) -> bool:
        # Check if the current character is the given character
        return cls.CODE[cls.POSITION] == char
    
    @classmethod
    def isNextChar(cls, char: str) -> bool:
        # Check if the next character is the given character
        return cls.CODE[cls.POSITION + 1] == char
    
    @staticmethod
    def isCustomWhitespace(value: str) -> bool:
        # Check if the given value is whitespace
        return value in {' ', '\t', '\r', '\f', '\v'}
    
    @classmethod
    def prevChar(cls) -> str:
        # Return the previous character
        return cls.CODE[cls.POSITION - 1]

    @classmethod
    def prevPos(cls) -> int:
        # Return the position of the previous character
        return cls.POSITION - 1
    
    @classmethod
    def getLineNumber(cls) -> int:
        # Return the line number
        return cls.LINE_NUMBER

    @classmethod
    def endOfInput(cls) -> bool:
        # Check if the end of the input has been reached
        return cls.POSITION >= len(cls.CODE)

    @classmethod
    def setup(cls, code: str) -> None:
        # Set up the lexer
        cls.CODE = code.strip()
        cls._pvt()

    @classmethod
    def reset(cls) -> None:
        # Reset the lexer
        cls.CODE = ""
        cls._pvt()
    
    @classmethod
    def _pvt(cls):
        # Private methods for internal use (prevent duplication)
        cls.POSITION = 0
        cls.TOKENS = []
        cls.LINE_NUMBER = 0
    
    @classmethod
    def tokenize(cls, code: str, ignoreComments: bool = True) -> list:
        # Tokenize the input code
        pass