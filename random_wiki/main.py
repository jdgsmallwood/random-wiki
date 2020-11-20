from random_wiki.models import RandomWiki
from random_wiki.interface import Interface


def main():
    interface = Interface(RandomWiki())
    interface.main()


if __name__ == '__main__':
    main()
