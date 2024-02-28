def main ():
    print(sort_dict_to_list(count_letters(get_book_content())))
    
def get_book_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    return len(text.split())

def count_letters(text):
    text_lower = text.lower()
    character_dict = {}
    for character in text_lower:
        if character in character_dict: character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict

def sort_dict_to_list(dict):
    lst = []
    for key in dict:
        lst.append({ 'letter': key, 'num': dict[key]})
    lst.sort(reverse=True, key=sort_on)
    return lst

def sort_on(dict):
    return dict['num']

main()


