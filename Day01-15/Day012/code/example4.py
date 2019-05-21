"""

@Author:jyang
@Date:5/19/2019
"""
import re


def main():
    poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentences = re.split(r'[，。]', poem)
    while '' in sentences:
        sentences.remove('')
    print(sentences)


if __name__ == '__main__':
    main()
