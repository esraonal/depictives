import os
from collections import defaultdict

def read_connlu(treebank):

    sentence = ''
    analysis = ''

    var = False
    new_sent = False
    # print(treebank)
    a = 0

    whole_text = ''
    adjectives = ''
    adjs =list()

    sent_num = 0
    w = 0
    w2 = 0

    for i in range(len(treebank)):

        columns = []
        prev_columns = []
        next_columns = []

        if str(treebank[i]).startswith('# sent_id = '):
            id = treebank[i]
        elif str(treebank[i]).startswith('# text = '):
            sentence = treebank[i]

        elif str(treebank[i]) == '\n':
            new_sent = True
            var = False
        else:
            analysis += treebank[i] + '\n'

            columns = treebank[i].split('\t')
            prev_columns = treebank[i-1].split('\t')
            next_columns = treebank[i+1].split('\t')


        try:
            if str(columns[1]).lower() != str(prev_columns[1].lower()) and str(columns[4]) == 'Adj' and \
                    str(next_columns[4]) == 'Verb' and str(next_columns[2]) != 'ol' and \
                     str(next_columns[2]) != 'bul' and str(next_columns[2]) != 'et' \
                    and str(next_columns[2]) != 'görün' and str(columns[1]).lower() != 'iyi' \
                    and str(next_columns[2]) != 'say' and str(columns[1]).lower() != 'ilk' \
                    and str(columns[1]).lower() != 'çok':
                var = True
                w += 1
                whole_text += sentence + '\n' + treebank[i] + '\n' + treebank[i+1] + '\n'

                if not adjs.__contains__(str(columns[1].lower()) + str(next_columns[2])):
                    w2 +=1
                    adjectives += str(columns[1].lower()) + '\t' + str(next_columns[2] + '\n')
                    adjs.append(str(columns[1].lower()) + str(next_columns[2]))

                print(sentence)
                print(treebank[i])
                print(treebank[i+1])

        except IndexError:
            pass

    debups = open("bare_adj.txt", "a+")
    redup_mods = open("bare_adj_modifiers.txt", "a+")

    for i in range(1):
        debups.write('Number of instances: ' + str(w) + '\n\n')
        debups.write(whole_text)
        debups.close()

        redup_mods.write('Number of pairs: ' + str(w2) + '\n\n')
        redup_mods.write(adjectives)
        redup_mods.close()


    #     try:
    #         print(columns[4])
    #         and not str(columns[7]) == 'compound:redup'
    #         not str(columns[1]).lower() == str(prev_columns[1].lower())\
    #                             and
    #          and str(columns[4]) == 'Adj'
    #         if str(columns[3]) == 'ADV' and \
    #                 str(columns[1]).lower().endswith('ken') and not str(columns[1]).lower().endswith('erken') \
    #                 and not str(columns[1]).lower().endswith('irken') and not str(columns[1]).lower().endswith('urken') and not str(columns[1]).lower().endswith('ırken') \
    #                 and not str(columns[1]).lower().endswith('ürken') and not str(columns[1]).lower().endswith('arken'):
    #             var = True
    #             w += 1
    #             whole_text += sentence + '\n' + treebank[i] + '\n' + treebank[i+1] + '\n'
    #
    #             if not adjs.__contains__(str(columns[1].lower())):
    #                 w2 +=1
    #                 # print(str(columns[1].lower()))
    #                 # print(str(next_columns[2]))
    #
    #                 adjectives += str(columns[1].lower()) + '\n'
    #                 adjs.append(str(columns[1].lower()))
    #
    #
    #             print(sentence)
    #             print(treebank[i])
    #             print(treebank[i+1])
    #
    #     except IndexError:
    #         # print()
    #         pass
    #
    # debups = open("yken_adj.txt", "w+")
    # redup_mods = open("yken_adj_modifiers.txt", "w+")
    # # print(whole_text)
    # for i in range(1):
    #     debups.write('Number of instances: ' + str(w) + '\n\n')
    #     debups.write(whole_text)
    #     debups.close()
    #
    #     redup_mods.write('Number of pairs: ' + str(w2) + '\n\n')
    #     redup_mods.write(adjectives)
    #     redup_mods.close()

    #     try:
    #         # print(columns[4])
    #         # and not str(columns[7]) == 'compound:redup'
    #         # not str(columns[1]).lower() == str(prev_columns[1].lower())\
    #         #                     and
    #         if str(columns[1]).lower() == str(prev_columns[1]).lower() and (str(columns[4]) == 'Adj' or str(prev_columns[4]) == 'Adj' or
    #                 str(prev_columns[1]).lower() == 'sessiz' or str(prev_columns[1]).lower() == 'kara'):
    #             var = True
    #             w += 1
    #             whole_text += sentence + '\n' + treebank[i-1] + '\n' + treebank[i] + '\n' + treebank[i+1] + '\n'
    #             if str(next_columns[4]) == 'Verb':
    #                 w2 += 1
    #                 # print(str(columns[1].lower()))
    #                 # print(str(next_columns[2]))
    #                 if not adjs.__contains__(str(columns[1].lower()) + str(prev_columns[1]).lower() + str(next_columns[2]).lower()):
    #                     adjectives += str(columns[1].lower()) + '\t' + str(prev_columns[1].lower() + '\t' + str(next_columns[2] + '\n'))
    #                     adjs.append(str(columns[1].lower()) + str(prev_columns[1]).lower() + str(next_columns[2]).lower())
    #
    #             elif not adjs.__contains__(str(columns[1].lower()) + str(prev_columns[1]).lower()):
    #                 w2 +=1
    #                 # print(str(columns[1].lower()))
    #                 # print(str(next_columns[2]))
    #
    #                 adjectives += str(columns[1].lower()) + '\t' + str(prev_columns[1] + '\n')
    #                 adjs.append(str(columns[1].lower()) + str(prev_columns[1]).lower())
    #
    #             print(sentence)
    #             print(treebank[i - 1])
    #             print(treebank[i])
    #     except IndexError:
    #         pass
    #
    # debups = open("dup_adj.txt", "a+")
    # redup_mods = open("dup_adj_modifiers.txt", "a+")
    #
    # for i in range(1):
    #     debups.write('Number of instances: ' + str(w) + '\n\n')
    #     debups.write(whole_text)
    #     debups.close()
    #
    #     redup_mods.write('Number of pairs: ' + str(w2) + '\n\n')
    #     redup_mods.write(adjectives)
    #     redup_mods.close()


    #     try:
    #         if str(columns[4]) == 'Adj' and \
    #                 str(next_columns[1]).lower() == 'olarak':
    #             var = True
    #             w += 1
    #             whole_text += sentence + '\n' + treebank[i] + '\n' + treebank[i+1] + '\n'
    #
    #             if not adjs.__contains__(str(columns[1].lower()) + str(next_columns[2])):
    #                 w2 +=1
    #                 adjectives += str(columns[1].lower()) + '\t' + str(next_columns[2] + '\n')
    #                 adjs.append(str(columns[1].lower()) + str(next_columns[2]))
    #
    #             print(sentence)
    #             print(treebank[i])
    #             print(treebank[i+1])
    #
    #     except IndexError:
    #         pass
    #
    # debups = open("olarak_adj.txt", "a+")
    # redup_mods = open("olarak_adj_modifiers.txt", "a+")
    #
    # for i in range(1):
    #     debups.write('Number of instances: ' + str(w) + '\n\n')
    #     debups.write(whole_text)
    #     debups.close()
    #
    #     redup_mods.write('Number of pairs: ' + str(w2) + '\n\n')
    #     redup_mods.write(adjectives)
    #     redup_mods.close()

def main():
    path = './annotated books'
    folder_paths=[]
    for r, d, f in os.walk(path):
        # print(f)
        # print(r)
        for file in f:
            # print(os.path.join(r, file))
            if str(file).endswith('.conllu'):
                folder_paths.append(os.path.join(r, file))

    for folder in folder_paths:
        # print(folder)
        with open(folder, 'r', encoding='utf-8-sig') as f:
            # dictionary = f.read()
            old = f.readlines()
            # print(old)
        read_connlu(old)

if __name__ == '__main__':
    main()