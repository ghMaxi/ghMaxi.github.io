from stack import Stack,\
    standard_deck_52


class DrunkCard:
    def __init__(self,
                 player_count: int,
                 deck: Stack):
        self.player_hands = \
            tuple(
                Stack() for _ in
                range(player_count)
            )
        while deck.has_cards(player_count):
            for hand in self.player_hands:
                deck.deal_card(hand)

    def __str__(self):
        line = '\n'.join(
            f'{i + 1}: {self.player_hands[i]}'
            for i in
            range(len(self.player_hands)))
        return f'DrunkCard(\n{line})'


if __name__ == '__main__':
    game = DrunkCard(3, standard_deck_52())
    print(game)
