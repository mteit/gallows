import os
import config
import random as rnd


def main():
    os.system('CLS')
    playError = 0
    playWord = rnd.choice(config.vocabulary)
    playUsed = []

    word = '-' * len(playWord)

    while word != playWord:

        print(config.men[playError])

        print(f'Слово "{word}"')
        print(f'Использованые буквы "{playUsed}"')
        lit = input('Введите букву >>>')
        os.system('CLS')

        if lit in playWord:
            for i in range(len(playWord)):
                if playWord[i] == lit:
                    word = word[:i] + lit + word[i + 1:]
        else:
            playError += 1

            if playError == 6:
                print('ты проиграл')
                break

        if not (lit in playUsed):
            playUsed.append(lit)
            playUsed.sort()

    print('ты победил')
    print(f'Ваше слово "{playWord}"')


if __name__ == '__main__':
    main()
