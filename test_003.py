def find_word(lst_words, search=""):
    search = str(input("Search key word>")).lower()
    if search == "end":
        return
    else:
        for w in lst_words:
            if w.startswith(search):
                print(w)
        find_word(lst_words, search)


def find_word_v2(lst_words):
    loop_stop = True
    while loop_stop:
        search = str(input("Search key word>")).lower()
        if search == "end":
            loop_stop = False
        else:
            for w in lst_words:
                if w.startswith(search):
                    print(w)


def add_words():
    is_active = True
    lst_words = []

    while is_active:
        word = str(input(">")).lower()
        if word == "end":
            find_word_v2(lst_words)
            is_active = False
        else:
            lst_words.append(word)


if __name__ == "__main__":
    add_words()
