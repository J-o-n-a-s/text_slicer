from sys import setrecursionlimit


setrecursionlimit(10**6)


class BreakTextIntoLines:
    def __init__(
        self,
        p_text: str,
        p_characters: int = 79,
        p_starting_character: str = '',
        p_terminating_character: str = '',
    ):
        self.__text: str = p_text
        self.__characters: int = p_characters
        self.__starting_character: str = p_starting_character
        self.__terminating_character: str = p_terminating_character

    def exec(self) -> str:
        return '\n'.join(
            self.__director(
                self.__text,
                self.__characters,
                self.__starting_character,
                self.__terminating_character,
            )
        )

    def __director(
        self,
        p_text: str,
        p_characters: int,
        p_starting_character,
        p_terminating_character: str,
    ) -> list:
        _modifier: int = (
            1 + len(p_starting_character) + len(p_terminating_character)
        )
        _result: list = []
        _text_copy: str = p_text[:]

        _result.append(
            p_starting_character
            + _text_copy[:p_characters]
            + p_terminating_character
        )

        if len(_text_copy) > p_characters:
            _result += self.__director(
                _text_copy[p_characters:],
                p_characters,
                p_starting_character,
                p_terminating_character,
            )
        return _result


result = BreakTextIntoLines(
    p_text=input('\nDigite o texto\n> '),
    p_characters=int(input('\nDigite o número de caracteres\n> ')),
    p_starting_character=input('\nDigite o prefixo\n> '),
    p_terminating_character=input('\nDigite o sufixo\n> '),
)

print('\n\n', result.exec())
input('\n\nPressione <enter> para finalizar...')
