if __name__ == '__main__':
    import sys
    import main
    from pathlib import Path

    PATH = str(Path(__file__).parent)
    sys.path.extend([f'{PATH}\\venv',
                     f'{PATH}\\venv\\Lib\\site-packages'])
    main.start()