# I am new to Python.  I could not figure out few things first go into Python.
#  My loop was broken.  I could not stop the loop of the song.
#  I could not just initialize it by calling ".song().
#
# The first one, I reversed my loop.
# - Not sure if that fixed it of if I just fixed the ranges.
#
# The second one,  I still have not fixed.
# But, Google and the IDE taught me you could create Template to 'pass' to get to the pass the tests,
# (as long as you passed the song in as a string template).
#
# So, I passed it in, just like the test, so I could make it print by calling `.song()`.
# - Honestly, it still feels a little broken.  The tests pass, but only when providing the song.
######################################################################################################
from typing import Type


class BottleVerseStrTemplate:
    @staticmethod
    def lyrics(number: int) -> str:
        # pass
        verse_0 = (
                "No more bottles of beer on the wall, " +
                "no more bottles of beer.\n" +
                "Go to the store and buy some more, " +
                "99 bottles of beer on the wall.\n"
        )
        verse_2 = (
                f"{number} bottles of beer on the wall, " +
                f"{number} bottles of beer.\n" +
                "Take one down and pass it around, " +
                f"{number - 1} bottle of beer on the wall.\n"
        )
        verse_1 = (
                f"{number} bottle of beer on the wall, " +
                f"{number} bottle of beer.\n" +
                "Take it down and pass it around, " +
                "no more bottles of beer on the wall.\n"
        )
        verse_6 = (
                "1 six-pack of beer on the wall, " +
                "1 six-pack of beer.\n" +
                "Take one down and pass it around, " +
                f"{number - 1} bottles of beer on the wall.\n"
        )
        verse_7 = (
                f"{number} bottles of beer on the wall, " +
                f"{number} bottles of beer.\n"
                "Take one down and pass it around, " +
                f"1 six-pack of beer on the wall.\n"
        )
        default = (
                f"{number} bottles of beer on the wall, " +
                f"{number} bottles of beer.\n" +
                "Take one down and pass it around, " +
                f"{number - 1} bottles of beer on the wall.\n"
        )

        case = {
            0: verse_0,
            1: verse_1,
            2: verse_2,
            6: verse_6,
            7: verse_7
        }
        return case.get(number, default)


class Bottles:
    def __init__(
            self,
            verse_str_template: Type[BottleVerseStrTemplate],
            max_: int = 999_999,
            min_: int = 0,
    ):
        self.verse_str_template = verse_str_template
        self.min_ = min_
        self.max_ = max_

    def song(self) -> str:
        return self.verses(self.max_, self.min_)

    def verses(self, upper: int, lower: int) -> str:
        return f"\n".join(
            [self.verse(i) for i in reversed(range(lower, upper + 1))]
        )

    def verse(self, bottle_number: int) -> str:
        return self.verse_str_template.lyrics(bottle_number)


class BottleNumber:
    def __init__(self, bottle_number: int) -> None:
        self.bottle_number = bottle_number

    @staticmethod
    def get(bottle_number: int):
        if bottle_number == 0:
            return BottleNumber0(bottle_number)
        elif bottle_number == 1:
            return BottleNumber1(bottle_number)
        elif bottle_number == 6:
            return BottleNumber6(bottle_number)
        else:
            return BottleNumber(bottle_number)

    def get_quantity_and_container(self) -> str:
        return " ".join([self.get_quantity(), self.get_container()])

    def get_container(self) -> str:
        return "bottles"

    def get_pronoun(self) -> str:
        return "one"

    def get_quantity(self) -> str:
        return str(self.bottle_number)

    def get_action(self) -> str:
        return f"Take {self.get_pronoun()} down and pass it around"

    def get_successor(self) -> int:
        return self.get(self.bottle_number - 1)


class BottleNumber0(BottleNumber):
    def get_quantity(self) -> str:
        return "no more"

    def get_action(self) -> str:
        return "Go to the store and buy some more"

    def get_successor(self) -> int:
        return self.get(99)


class BottleNumber1(BottleNumber):
    def get_container(self) -> str:
        return "bottle"

    def get_pronoun(self) -> str:
        return "it"


class BottleNumber6(BottleNumber):
    def get_quantity(self) -> str:
        return "1"

    def get_container(self) -> str:
        return "six-pack"


class BottleVerse:
    def __init__(self, bottle_number) -> None:
        self.bottle_number = bottle_number

    @staticmethod
    def lyrics(bottle_number: int) -> str:
        return BottleVerse(BottleNumber.get(bottle_number))._lyrics()

    def _lyrics(self) -> str:
        return (
            f"{self.bottle_number.get_quantity_and_container().capitalize()} of beer on the wall, "
            f"{self.bottle_number.get_quantity_and_container()} of beer.\n"
            f"{self.bottle_number.get_action()}, {self.bottle_number.get_successor().get_quantity_and_container()}"
            f" of beer on the wall.\n"
        )


if __name__ == "__main__":
    bottles = Bottles(BottleVerseStrTemplate, 99, 0)
    print(f"{bottles.song()}")
