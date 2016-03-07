from operator import itemgetter

def answer(names):
    # compute score of a lowercase letter
    def letter_score(letter):
        return ord(letter) - ord('a') + 1

    # compute score of a name (consisting of only lowercase letters)
    def name_score(name):
        return sum([letter_score(ltr) for ltr in name])

    # order input list of names by:
    # - descending order of name score (higher score > lower score)
    # - descending order of lexicographic position (higher position > lower position)

    names_with_scores = [(name, name_score(name)) for name in names]
    sorted_name_scores = sorted(names_with_scores, key=itemgetter(1,0), reverse=True)
    return [name_score[0] for name_score in sorted_name_scores]

def main():
    test_cases = [
        ["annie", "bonnie", "liz", "dannie"],
        ["vi", "abcdefg"],
        ["al", "cj"]
    ]

    for case in test_cases:
        print "Input: ", case
        print "Output:", answer(case)

if __name__ == "__main__":
    main()
