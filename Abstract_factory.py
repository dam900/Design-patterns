from __future__ import annotations
from abc import ABC, abstractmethod

# The goal of this project is to present the skill of implementation
# and using Abstract Factory design pattern
#
# The example below is build with purpose of making character class ex. Mage can be Fire Mage , Ice Mage ...


# --------------------------------------
# -------------- FACTORY ---------------
# --------------------------------------


class AbstractFactory(ABC):

    @abstractmethod
    def create_mage(self) -> AbstractMage:
        pass

    @abstractmethod
    def create_warrior(self) -> AbstractWarrior:
        pass


class FireFactory(AbstractFactory):

    def create_mage(self) -> AbstractMage:
        return FireMage()

    def create_warrior(self) -> AbstractWarrior:
        return FireWarrior()


class IceFactory(AbstractFactory):

    def create_mage(self) -> AbstractMage:
        return IceMage()

    def create_warrior(self) -> AbstractWarrior:
        return IceWarrior()


# --------------------------------------
# --------------- Class ----------------
# --------------------------------------

# --------------- Mage -----------------
class AbstractMage(ABC):

    @abstractmethod
    def cast_spell(self) -> None:
        pass


class FireMage(AbstractMage):

    def cast_spell(self) -> None:
        print('Casting FireBall')


class IceMage(AbstractMage):

    def cast_spell(self) -> None:
        print('Casting FrostBolt')


# ------------- Warrior ------------
class AbstractWarrior(ABC):

    @abstractmethod
    def attack(self) -> None:
        pass

    @abstractmethod
    def attack_with_companion(self, companion: AbstractMage) -> None:
        pass


class FireWarrior(AbstractWarrior):

    def attack(self) -> None:
        print('Attacking with FireAxe')

    def attack_with_companion(self, companion: AbstractMage) -> None:
        print(f'Fire Warrior is attacking and Mage is')
        companion.cast_spell()


class IceWarrior(AbstractWarrior):

    def attack(self) -> None:
        print('Attacking with IceSword')

    def attack_with_companion(self, companion: AbstractMage) -> None:
        print('Ice Warrior is attacking and Mage is')
        companion.cast_spell()


def soldiers_attack(factory: AbstractFactory) -> None:

    mage = factory.create_mage()
    warrior = factory.create_warrior()

    mage.cast_spell()
    warrior.attack()
    warrior.attack_with_companion(mage)


if __name__ == '__main__':
    print('Fire Soldiers attacking IceSoldiers')
    soldiers_attack(FireFactory())

    print('-'*40)

    print('Ice Soldiers counterattacking')
    soldiers_attack(IceFactory())
    print('-' * 40)




