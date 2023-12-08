import csv
from icecream import ic

# cardsss = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
# h = []
# sets = []
# highest_count = []
# cards_in_the_set = []
# var = ''
# new_hash = {}


# with open('file.csv') as file:
#     file = csv.reader(file)
#     for line in file:
#         sets.append(line[0].split(' ')[0])
#         h.append(line[0].split(' ')[1])
#         new_hash[line[0].split(' ')[0]] = int(line[0].split(' ')[1])
#     for cards in sets:
#         for card in cards:
#             if cards.count(card) >= 2:
#                 ic(card)
#                 if card not in cards_in_the_set:
#                     if var != '':
#                         var += '.' + str(cards.count(card))
#                     else:
#                         var += str(cards.count(card))
#                     cards_in_the_set.append(card)
#         if var == '2.3':
#             var = '3.2'
#         if var == '':
#             var = '1'
#         ic([float(var)], list(cards))
#         highest_count.append([float(var)] + list(cards))
#         var = ''
#         cards_in_the_set = []
#

    # for item in highest_count:
    #     for element in range(len(item)):
    #         if item[element] == 'T':
    #             item[element] = 10
    #         elif item[element] == 'J':
    #             item[element] = 11
    #         elif item[element] == 'Q':
    #             item[element] = 12
    #         elif item[element] == 'K':
    #             item[element] = 13
    #         elif item[element] == 'A':
    #             item[element] = 14
    #         item[element] = float(item[element])
    #
    # for item in range(len(highest_count)):
    #     highest_count[item] = tuple(highest_count[item])
    #
    #
    # highest_count1 = sorted(highest_count)
    #
    # for item in range(len(highest_count1)):
    #     highest_count1[item] = list(highest_count1[item][1:])
    #
    #
    # res = []
    #
    # for item in highest_count1:
    #     new_str = ''
    #     for element in range(len(item)):
    #         if item[element] == 10.0:
    #             item[element] = 'T'
    #         elif item[element] == 11.0:
    #             item[element] = 'J'
    #         elif item[element] == 12.0:
    #             item[element] = 'Q'
    #         elif item[element] == 13.0:
    #             item[element] = 'K'
    #         elif item[element] == 14.0:
    #             item[element] = 'A'
    #         else:
    #             item[element] = int(item[element])
    #         item[element] = str(item[element])
    #         new_str += item[element]
    #     res.append(new_str)
    #
    # multi = 1
    # total_res = 0
    # for i in res:
    #     total_res += new_hash[i] * multi
    #     multi += 1
    # print(total_res)


#22222222222222222222222222222222222222222222222222

cardsss = ['A', 'K', 'Q', 'T', 'J', '9', '8', '7', '6', '5', '4', '3', '2']
highest_count = []
cards_in_the_set = []
var = ''
new_hash = {}


with open('file.csv') as file:
    file = csv.reader(file)
    for line in file:
        new_hash[line[0].split(' ')[0]] = int(line[0].split(' ')[1])
    for cards in new_hash.keys():
        for card in cards:
            if cards.count(card) >= 2 and card != 'J':
                if card not in cards_in_the_set:
                    if var != '':
                        var += '.' + str(cards.count(card))
                    else:
                        var += str(cards.count(card))
                    cards_in_the_set.append(card)
        if var == '2.3':
            var = '3.2'
        if var == '':
            var = '1'
        value_cards = float(var) + cards.count('J')
        if value_cards == 6.0:
            value_cards = 5.0
        highest_count.append([value_cards] + list(cards))
        var = ''
        cards_in_the_set = []


    for item in highest_count:
        for element in range(len(item)):
            if item[element] == 'T':
                item[element] = 10
            elif item[element] == 'J':
                item[element] = 1
            elif item[element] == 'Q':
                item[element] = 12
            elif item[element] == 'K':
                item[element] = 13
            elif item[element] == 'A':
                item[element] = 14
            item[element] = float(item[element])

    for item in range(len(highest_count)):
        highest_count[item] = tuple(highest_count[item])

    highest_count1 = sorted(highest_count)

    for item in range(len(highest_count1)):
        highest_count1[item] = list(highest_count1[item][1:])

    res = []

    for item in highest_count1:
        new_str = ''
        for element in range(len(item)):
            if item[element] == 10.0:
                item[element] = 'T'
            elif item[element] == 1.0:
                item[element] = 'J'
            elif item[element] == 12.0:
                item[element] = 'Q'
            elif item[element] == 13.0:
                item[element] = 'K'
            elif item[element] == 14.0:
                item[element] = 'A'
            else:
                item[element] = int(item[element])
            item[element] = str(item[element])
            new_str += item[element]
        res.append(new_str)

    multi = 1
    total_res = 0

    for i in res:
        total_res += new_hash[i] * multi
        multi += 1
    print(total_res)
