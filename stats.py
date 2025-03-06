def num_words(text: str) -> str:
    words = text.split()
    return len(words)

def num_char(text: str) -> str:
    characters = {}
    for word in text:
        for char in word:
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else: 
                characters[char] = 1
    
    return characters

def sort_dict(characters: dict) -> list:
    list_of_chars = []

    for each in characters:
        new_dict = {}
        new_dict['character'] = each
        new_dict['count'] = characters[each]
        list_of_chars.append(new_dict)

    def sort_on(dict):
        return dict["count"]

    list_of_chars.sort(reverse=True, key=sort_on)

    return list_of_chars


