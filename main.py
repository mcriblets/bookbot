def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    count = word_count(file_contents)
    cha_count = character_count(file_contents)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document" )
    print (" ")
    sort = parse_dict(cha_count)
    print("--- End report ---")
 
   
def word_count(text):
    words = 0
    word_split = text.split()
    
    for word in word_split:
        words += 1
        
    #print(words) 
    return words  
    
 
def character_count(text):
    text = text.lower()
    word_split = text.split()
    characters = {}
    spaces = 0
            
    for word in word_split:
        for letter in word:
            if letter not in characters:
                characters[letter] = 1
            elif letter in characters:
                characters[letter] += 1
            else:
                pass
            
    for character in text:
        if character == " ":
            spaces += 1
        else:
            pass
        
    characters[" "] = spaces
    #print(characters)
    return characters


def parse_dict(dict):
    list = []
    for character in dict:
        if character.isalpha():
            list.append({"letter": character, "count": dict.get(character)})

    list.sort(key=lambda letter: letter["count"], reverse=True)
    
    for item in list:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    
        
main()