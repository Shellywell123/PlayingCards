import numpy as np

def hand_encoder(hand):
    """
    encodes hand to matrix format
    """

    encode_matrix = np.zeros((4,13),dtype=np.int)

    for card in hand:
        card_num = card.split("\x1b[")[0]

        #make A=14
        if card_num =='J':
            card_num = '11'

        if card_num =='Q':
            card_num = '12'

        if card_num =='K':
            card_num = '13'

        if card_num =='A':
            card_num = '14'

        card_suit = card.split('m')[1]

        #write elements to encode_matrix

        if card_suit == '♠':
            encode_matrix[0,int(card_num)-2] += 1

        if card_suit == '♦':
            encode_matrix[1,int(card_num)-2] += 1

        if card_suit == '♥':
            encode_matrix[2,int(card_num)-2] += 1

        if card_suit == '♣':
            encode_matrix[3,int(card_num)-2] += 1

    return encode_matrix