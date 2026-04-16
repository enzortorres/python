from pprint import pprint
def count_word(string: str) -> dict:
    string = string.lower()
    
    pontuacoes = ",./:;-"
    for p in pontuacoes:
        string = string.replace(p, "")
        
    words_array = string.split()
    words_dict = {}

    for word in words_array:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict

print(count_word("Testando som som oi oi"))
pprint(count_word("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries."))
