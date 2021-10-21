from card_deck import Deck, Card, deck


class DrunkCard:
    def __init__(self,
                 player_count, deck: Deck):
        print(f"Взяли колоду {deck}")
        self.deck = deck
        self.player_decks = tuple(
            Deck() for _ in
            range(player_count))
        i = 0
        while self.deck.has_cards() and\
                not self.player_decks[-1].has_cards(6):
            self.deck.deal(self.player_decks[i])
            i = (i + 1) % player_count
        print(self.player_deck_line())

    def player_deck_line(self):
        line = '\n'.join(
            f'№{i + 1}:{self.player_decks[i]}'
            for i in range(len(self.player_decks)))
        return f"Колоды игроков:\n{line}"

    def run(self):
        active_cards = []
        while all(player.has_cards()
                  for player in self.player_decks):
            winner_id = 0
            card = self.player_decks[0].get_top_card()
            active_cards.append(card)
            for i in range(1, len(self.player_decks)):
                new_card: Card =\
                    self.player_decks[i].get_top_card()
                active_cards.append(new_card)
                if new_card.beats(card):
                    winner_id = i
                    card = new_card
                elif new_card.ties(card):
                    winner_id = -1
            if winner_id >= 0:
                self.player_decks[winner_id].add(active_cards)
                active_cards.clear()


if __name__ == "__main__":
    game = DrunkCard(3, deck)
    game.run()
