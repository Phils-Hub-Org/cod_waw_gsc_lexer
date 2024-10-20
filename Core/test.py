import os

class Test:

    @classmethod
    def test(cls, gsc_lexer):
        # Set directory
        dir = r'D:\SteamLibrary\steamapps\common\Call of Duty World at War\raw\maps'

        # Get files
        # files = [os.path.join(dir, file) for file in os.listdir(dir) if file.endswith('.gsc')]
        
        filename = '_zombiemode_spawner.gsc'
        files_to_tokenize = os.path.join(dir, filename)

        files = [files_to_tokenize]

        # Read code from files
        for file in files:
            with open(file, 'r') as f:
                code = f.read()

            # Tokenize code
            try:
                tokens = gsc_lexer.tokenize(code)
            except AttributeError as e:
                print(f'You forgot to inherit the Lexer class!\n{e}')
                continue
            except Exception as e:
                print(f'An unhandled error occurred while tokenizing {file}: {e}')
                continue
        
            # Tokenize string
            tokens = gsc_lexer.tokenize(code)

            cls.viewResults(tokens, write_tokens=True)

    @classmethod
    def viewResults(cls, tokens, print_tokens=False, write_tokens=False, filename='tokens'):
        if print_tokens:
            # Print tokens
            print('\n'.join(str(token) for token in tokens))

        if write_tokens:
            # Write tokens to file
            with open(os.path.join(os.getcwd(), '--output', f'{filename}.txt'), 'w') as f:
                f.write('\n'.join(str(token) for token in tokens))