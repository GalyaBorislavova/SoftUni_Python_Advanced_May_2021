lengths = {word: len(word) for word in input().split(", ")}

print(*[f"{key} -> {value}" for key, value in lengths.items()], sep=", ")
