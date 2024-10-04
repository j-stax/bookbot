def countWords(content):
    content_as_list = content.split()
    count = len(content_as_list)
    return count

def countCharacters(content):
    charDict = {}
    for i in range(len(content)):
        char = content[i].lower()
        if ord(char) >= 97 and ord(char) <= 122:
            if char in charDict:
                charDict[char] = charDict[char] + 1
            else:
                charDict[char] = 1
    return charDict

def sort_on(dict):
    return dict["count"]

def convertDictToList(a_dict):
    new_list = []
    for char, count in a_dict.items():
        obj = {
            'char': char,
            'count': count
        }
        new_list.append(obj)

    new_list.sort(reverse=True, key=sort_on)
    return new_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = countWords(file_contents)
    char_dict = countCharacters(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{word_count} words found in the document')
    print()
    for obj in convertDictToList(char_dict):
        print(f'The \'{obj["char"]}\' character was found {obj["count"]} times')
    print("--- End report ---")

main()