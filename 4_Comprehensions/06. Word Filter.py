words = input().split()

even_len_words = [word for word in words if len(word) % 2 == 0]

print(*even_len_words, sep="\n")