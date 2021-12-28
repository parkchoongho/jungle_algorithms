graph = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

digits = "23"

word_list = []


def dfs(index, word):
    if index >= len(digits):
        if len(word) > 0:
            word_list.append(word)
        return
    for character in graph[digits[index]]:
        new_word = word + character
        dfs(index + 1, new_word)


dfs(0, "")

print(word_list)
