def palindrome(word, index=0):
    left_index = index
    right_index = len(word) - 1 - index

    if index >= right_index:
        return f"{word} is a palindrome"

    if word[index] == word[right_index]:
        return palindrome(word, index + 1)

    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))

