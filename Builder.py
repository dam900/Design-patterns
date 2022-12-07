from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# The goal of this project is to present the skill of implementation
# and using Builder design pattern
#
# The example below is build with purpose of making characters ex. in games


class Builder(ABC):
    """
    Builder interface for character creation
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_hair(self, length: str) -> None:
        pass

    @abstractmethod
    def produce_hair_color(self, color: str) -> None:
        pass

    @abstractmethod
    def produce_sex(self, sex: str) -> None:
        pass

    @abstractmethod
    def produce_ethnicity(self, ethnicity: str) -> None:
        pass

    @abstractmethod
    def produce_height(self, height: int) -> None:
        pass

    @abstractmethod
    def produce_athletic(self, athletic: bool) -> None:
        pass

    @abstractmethod
    def produce_muscular(self, muscular: bool) -> None:
        pass


class CharacterBuilder(Builder):

    def __init__(self) -> None:
        """
        A fresh building instance
        """
        self.reset()

    def reset(self) -> None:
        self._product = Character()

    @property
    def product(self) -> Character:
        product = self._product
        self.reset()
        return product

    def produce_hair(self, value: str) -> None:
        self._product.add_characteristic('hair', value)

    def produce_athletic(self, athletic: bool) -> None:
        self._product.add_characteristic('athletic', athletic)

    def produce_ethnicity(self, ethnicity: str) -> None:
        self._product.add_characteristic('ethnicity', ethnicity)

    def produce_height(self, height: int) -> None:
        self._product.add_characteristic('height', height)

    def produce_muscular(self, muscular: bool) -> None:
        self._product.add_characteristic('muscular', muscular)

    def produce_sex(self, sex: str) -> None:
        self._product.add_characteristic('sex', sex)

    def produce_hair_color(self, color: str) -> None:
        self._product.add_characteristic('hair color', color)


class Character:

    def __init__(self):
        self.char_dict = {}

    def add_characteristic(self, key: str, value: Any) -> None:
        self.char_dict[key] = value

    def list_characteristics(self) -> None:
        print(f'All Characteristics are:')
        for key, value in self.char_dict.items():
            print(f'{key.title()} -> {value}')


class Director:

    def __init__(self) -> None:
        self.__builder = None

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self.__builder = builder

    def build_default_character(self) -> None:
        self.builder.produce_sex('female')
        self.builder.produce_height(178)
        self.builder.produce_hair('long')
        self.builder.produce_hair_color('blonde')
        self.builder.produce_ethnicity('european')
        self.builder.produce_athletic(True)
        self.builder.produce_muscular(False)


if __name__ == "__main__":
    director = Director()
    builder = CharacterBuilder()
    director.builder = builder

    print('Default character: ')
    director.build_default_character()
    builder.product.list_characteristics()


