import os

def read_connlu(treebank):

    sentence = ''
    id = ''
    analysis = ''

    sentences = ''
    prev_line = ''
    var = False
    new_sent = False
    # print(treebank)
    a = 0
    for line in list(treebank):
        # print(line)

        if str(line).startswith('# sent_id = '):
            # print(str(line))
            id = line
        elif str(line).startswith('# text = '):
            # print(str(line))
            sentence = line

        elif str(line) == '\n':
            # print(line)
            new_sent = True
            var = False
        else:
            analysis += line + '\n'

        if var == True and new_sent == True:
            # print(sentence)
            sentences += id + '\n'
            sentences += sentence + '\n'
            sentences += analysis
            # print(sentences)
            id = ''
            analysis = ''
            var = False
            new_sent = False

        if prev_line.__contains__('Adj') and str(prev_line).__contains__('ADV') and not prev_line.__contains__('obl')\
                and str(line).__contains__('Verb') and not str(line).__contains__('\tol\t')\
                and not str(line).__contains__('\tcompound:lvc\t')\
                and not str(line).__contains__('gör') and not str(line).__contains__('göz') \
            and not str(prev_line).__contains__('iyi') and not str(prev_line).__contains__('büsbütün')\
        and not str(prev_line).__contains__('çok') and not str(prev_line).__contains__('türlü') and not str(prev_line).__contains__('yeni')\
                and not str(prev_line).__contains__('yoksa'):
            var = True
            print(sentence)
            print(prev_line)
            print(line)
        # if prev_line.__contains__('Adj') and not prev_line.__contains__('NAdj') and not line.__contains__('NOUN')\
        #         and not line.__contains__('Noun'):
        #     var = True
        #     print(sentence)
        #     print(prev_line)
        #     print(line)
        # if prev_line.__contains__('NOUN') and not prev_line.__contains__('Adj') and not line.__contains__('NOUN')\
        #         and line.__contains__('Adj'):
        #     var = True
        #     print(sentence)
        #     print(prev_line)
        #     print(line)

        # if str(line).__contains__('ADV') and str(line).__contains__('Adj') and not str(line).__contains__('NAdj'):
        #     var = True
        #     a += 1
        #     print(sentence)
        #     print(line)
        #
        # if str(line).__contains__('ADJ') and str(line).__contains__('conj'):
        #     var = True
        #     print(sentence)
        #     print(line)
        # if str(line).__contains__('ADJ') and str(line).__contains__('xcomp'):
        #     var = True
        #     print(sentence)
        #     print(line)

        prev_line = line

    # print(a)
    # print(sentences)

    # treebank_sent = open("treebank_sentences.txt", "w+")
    # for i in range(1):
    #     print(sentence)
    #     treebank_sent.write(sentence)
    #     treebank_sent.close()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = './annotated\ books'
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
        read_connlu(old)
