# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （Emiya)
# created:  2019.7.10

# Description:
#   定义标准发牌机的动作函数
# ------------------------(max to 80 columns)-----------------------------------

# import some external moduls
import random
import codecs
import os
import csv
import logging


def create_deck_54(new_deck):
    '推出一副新牌'
    print('\n -- debug: I made a new deck.')

    # initialize var
    cardJokers = ('♞', '♘')
    cardMarks = ('♠', '♥', '♣', '♦')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

    for c in cardJokers:
        new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    return


def create_deck_52(new_deck):
    '推出一副新牌'
    print('\n -- debug: I made a new deck.')

    # initialize var
#    cardJokers = ('♞', '♘')
    cardMarks = ('♠', '♥', '♣', '♦')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

#    for c in cardJokers:
#        new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n -- debug: I shuffled a deck')

    random.shuffle(deck_to_be_shuffled)
    return


'''
def record_deck_csv(deck_to_be_record, filename):
    '记录一副牌'
    print('\n -- debug: I record a deck')

    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close

    return
'''


def mak_deck_by_type(game_type, new_deck):
    if game_type == 1:
        create_deck_54(new_deck)
        shuffled_deck(new_deck)
        record_deck_csv(new_deck, '大鱼吃小鱼的总发牌.csv')

    if game_type == 2:
        create_deck_52(new_deck)
        shuffled_deck(new_deck)
        record_deck_csv(new_deck, '桥牌的总发牌.csv')

    if game_type == 3:
        create_deck_54(new_deck)
        shuffled_deck(new_deck)
        record_deck_csv(new_deck, '3人斗地主的总发牌.csv')
    if game_type == 4:
        # 发两遍牌，存到一起，再洗一遍
        deck_a = []
        create_deck_54(deck_a)
        new_deck.extend(deck_a)

        deck_b = []
        create_deck_54(deck_b)
        new_deck.extend(deck_b)

        # shuffled & record
        shuffled_deck(new_deck)
        record_deck_csv(new_deck, '四人斗地主-刚洗好的牌.csv')

    return


def record_deck_csv(deck_to_be_record, csv_filename):

    csv_path = os.getcwd() + '\\csv_files\\' + csv_filename

    with open(csv_path, "w", encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(deck_to_be_record)

    return


def read_deck_csv(csv_filename, out_deck):

    in_path = os.getcwd() + '\\csv_files\\' + csv_filename
    with open(in_path, "r", encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            out_deck.extend(line)

    return
