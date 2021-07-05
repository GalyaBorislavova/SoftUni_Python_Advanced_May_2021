def check_for_vowels(character: chr):
    if character.lower() in ['a', 'o', 'u', 'e', 'i']:
        return True
    return False


text = input()
no_vowels = [ch for ch in text if not check_for_vowels(ch)]
print("".join(no_vowels))