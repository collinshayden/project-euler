letter_scores = {"A" : 1, "B": 2, "C": 3, "D" : 4, "E" : 5, "F": 6, "G" : 7, "H": 8, "I" : 9, "J": 10, "K": 11, "L": 12,
"M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

infile = open("euler42_words.txt","r")
words = infile.read().split(",")

def letter_score(name):
    score = 0
    for char in name:
        score += letter_scores[char]
    return score

def gen_triangle_nums(bound):
    num_list = []
    for n in range(1,bound+1):
        num_list.append(int((n*(n+1))/2))
    return num_list

def find_triangle_words(words, bound):
    triangle_nums = gen_triangle_nums(bound)
    triangle_words = []
    for word in words:
        if letter_score(word) in triangle_nums:
            triangle_words.append(word)
    return triangle_words

print(len(find_triangle_words(words, 250)))