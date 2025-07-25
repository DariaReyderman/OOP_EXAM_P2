from abc import ABC, abstractmethod
from enum import Enum
import random


class CardContract(ABC):
    @property
    @abstractmethod
    def suit(self):
        pass

    @property
    @abstractmethod
    def rank(self):
        pass

    @abstractmethod
    def get_display_name(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class DeckContract(ABC):
    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add_card(self, card):
        pass

    @property
    @abstractmethod
    def cards(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, index):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def max(self):
        pass

    @abstractmethod
    def min(self):
        pass


class DeckCheatingError(Exception):
    """Used to identify cases where there is suspicion of manipulation of a deck of cards"""
    pass


class CardSuit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class CardRank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Card:
    def __init__(self, suit: CardSuit, rank: CardRank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self) -> CardSuit:
        return self._suit

    @property
    def rank(self) -> CardRank:
        return self._rank

    def get_display_name(self) -> str:
        return f"{self._rank.name.title()} of {self._suit.name.title()}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return (self._rank.value, self._suit.value) == (other._rank.value, other._suit.value)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return (self._rank.value, self._suit.value) < (other._rank.value, other._suit.value)

    def __gt__(self, other) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return (self._rank.value, self._suit.value) > (other._rank.value, other._suit.value)

    def __hash__(self) -> int:
        return hash((self._rank.value, self._suit.value))

    def __str__(self) -> str:
        return self.get_display_name()

    def __repr__(self) -> str:
        return f"Card(suit={self._suit!r}, rank={self._rank!r})"


class Deck:
    def __init__(self, shuffle: bool = True):
        self._cards = [Card(suit, rank) for suit in CardSuit for rank in CardRank]
        if shuffle:
            random.shuffle(self._cards)

    @property
    def cards(self) -> list:
        return list(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)
        return self

    def draw(self) -> Card:
        return self._cards.pop(0) if self._cards else None

    def add_card(self, card: Card):
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added to the deck")
        self._cards.append(card)
        return self

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int) -> Card:
        return self._cards[index]

    def __iter__(self):
        highest = self.max()
        lowest = self.min()
        if highest is not None and lowest is not None:
            yield highest
            yield lowest

    def max(self):
        return max(self._cards) if self._cards else None

    def min(self):
        return min(self._cards) if self._cards else None


def main():
    deck = Deck(shuffle=False)
    print("The deck is created, first 5 cards: ", deck.cards[:5])

    top_card = deck.draw()
    print("Top card:", top_card)

    deck.add_card(top_card)
    print("Added card back, the length is: ", len(deck))

    print("Accessing cards directly by index:")
    for i in range(5):
        print(deck[i])

    print("Iterating through all cards in the deck:")
    for card in deck:
        print(card)

    print("The highest card in deck:", deck.max())
    print("The lowest card in deck:", deck.min())


if __name__ == '__main__':
    main()
