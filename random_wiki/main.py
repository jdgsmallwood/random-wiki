from random_wiki.interface import Interface
from random_wiki.models import RandomWiki


def main():
    interface = Interface(RandomWiki())
    interface.main()


if __name__ == "__main__":
    main()
