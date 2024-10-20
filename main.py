import os
from Core.gsc_lexer import GscLexer

class Test:

    @classmethod
    def test(cls, gsc_lexer, files):

        # Print status
        print(f'Tokenizing {len(files)} files...\n')

        # Read code from files
        for i, file in enumerate(files):

            # Print status
            print(f'Tokenizing {file}...')

            # Read code from file
            with open(file, 'r') as f:
                code = f.read()

            # Tokenize code
            try:
                tokens = gsc_lexer.tokenize(code)
            except AttributeError as err:
                print(f'Skipping...\nYou forgot to inherit the Lexer class!\n{err}\n{file}')
                continue
            except IndexError as err:
                print(f'Skipping...\nAn index error occurred while tokenizing {file}: {err}')
                continue
            except Exception as err:
                print(f'Skipping...\nAn unhandled error occurred while tokenizing {file}: {err}')
                continue
        
            # Tokenize string
            tokens = gsc_lexer.tokenize(code)

            cls.viewResults(tokens, write_tokens=True, filename=f'tokens_{i}')

    @classmethod
    def viewResults(cls, tokens, print_tokens=False, write_tokens=False, filename='tokens'):
        if print_tokens:
            # Print tokens
            print('\n'.join(str(token) for token in tokens))

        if write_tokens:
            # Write tokens to file
            with open(os.path.join(os.getcwd(), '--output', f'{filename}.txt'), 'w') as f:
                f.write('\n'.join(str(token) for token in tokens))

if __name__ == "__main__":
    """
    Options:
    1. Read code from file
    2. Read code from _zombiemode_spawner.gsc
    3. Read code from all .gsc files in directory
    """
    OPTION = 1

    files = []

    if OPTION == 1:
        file = os.path.join(os.getcwd(), '--input', 'code.txt')
        with open(file, 'r') as f:
            code = f.read()

        files.append(file)

    elif OPTION in [2, 3]:
        # Set directory
        dir = r'D:\SteamLibrary\steamapps\common\Call of Duty World at War\raw\maps'

        if OPTION == 2:
            # Get file
            filename = '_zombiemode_spawner.gsc'
            files_to_tokenize = os.path.join(dir, filename)
            files.append(files_to_tokenize)

        elif OPTION == 3:
            # Get files
            files.append(os.path.join(dir, file) for file in os.listdir(dir) if file.endswith('.gsc'))

    else:
        print('Invalid option')
        exit()

    Test.test(GscLexer(), files)