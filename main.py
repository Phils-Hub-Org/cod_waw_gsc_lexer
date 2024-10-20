from Core.gsc_lexer import GscLexer
from Core.test import Test

class Entry:

    @classmethod
    def init(cls):
        
        # Initialize gsc lexer
        cls.gsc_lexer = GscLexer()

        Test.test(cls.gsc_lexer)

if __name__ == "__main__":
    entry = Entry()
    entry.init()