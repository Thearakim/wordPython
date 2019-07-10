def top_words(text):
    from collections import Counter

    split_it = text.lower().split()
    new_list = list()
    for word in split_it:
        if word[0] == "'" or word[len(word)-1] == " ' " or not word:
            continue
        else:
            new_word = ''.join([x for x in word if x.isalpha() or x == "'"])
            new_list.append(new_word)
    result = list()
    top_list = Counter(new_list)
    top_list = top_list.most_common(3)
    for x in top_list:
        for y in x:
            try:
                check = y.isdigit()
                result.append(y)
            except AttributeError:
                continue
    if len(result) == 1:
        return []
    else:
        return result


# print(top_words("Welcome to Kirirom: Kirirom Institute of Tech*&*(8&*nology and Kirirom National Parc. To contact us, send a message to us!?"))
# print(top_words("Can't cant Cant can't"))
# print(top_words("Hello ' ' ' WOrld &()*hello world ////dog /// cat world hello can't can't can't can't "))
# print(top_words(". ??? // ###### // // ???"))
# print(top_words("I've a cat. i've an apple"))