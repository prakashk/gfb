def answer(chunk, word):
    # remove substring from input string 
    #  - split the string at given offset,
    #  - remove substring from each part
    #  - join cleaned parts and remove substring again
    def remove_from_offset(chunk, word, offset):
        def clean(s):
            return s.replace(word, "")

        p1, p2 = chunk[0:offset], chunk[offset:]
        return clean(clean(p1) + clean(p2))

    candidates = [remove_from_offset(chunk, word, offset)
                         for offset in range(len(chunk) - len(word))]

    # compare by length first, and then by string itself
    def compare(x, y):
        result = cmp(len(x), len(y))
        return cmp(x, y) if result == 0 else result

    sorted_candidates = sorted(list(set(candidates)), cmp=compare)

    return sorted_candidates[0]

def main():
    test_cases = [
        ("lololololo", "lol"),
        ("goodgooogoogfogoood", "goo"),
        ("xyabcdababcdcdxy", "abcd")
    ]

    for case in test_cases:
        print "Input: ", case
        print "Output:", answer(case[0], case[1])

if __name__ == "__main__":
    main()
