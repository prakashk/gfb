from operator import itemgetter

def answer(meetings):
    sorted_meetings = sorted(meetings, key=itemgetter(0,1))
    unique_meetings = remove_duplicates(sorted_meetings)
    all_meeting_groups = [non_overlapping_group([], unique_meetings)]
    for m in unique_meetings:
        all_meeting_groups.append(non_overlapping_group([], remove_from_list(m, unique_meetings)))
    return max_length(all_meeting_groups)

def remove_duplicates(lol):
    out_lst = []
    if len(lol) <= 1:
        return lol
    else:
        head, tail = lol[0], lol[1:]
        out_lst.append(head)
        prev = head
        for l in tail:
            if prev != l:
                out_lst.append(l)
            prev = l
        return out_lst

def non_overlapping_group(acc, lst):
    if len(lst) == 0:
        return acc
    else:
        head, tail = lst[0], lst[1:]
        if len(acc) == 0:
            return non_overlapping_group([head], tail)
        else:
            last_entry_found = acc[-1]
            if overlaps(last_entry_found, head):
                return non_overlapping_group(acc, tail)
            else:
                acc.append(head)
                return non_overlapping_group(acc, tail)

# check if two meetings overlap
# inputs are assumed to be ordered
def overlaps(m1, m2):
    def start(m):
        return m[0]
    def end(m):
        return m[1]

    return end(m1) > start(m2)

# remove the specified element from given list and return the rest
def remove_from_list(x, lst):
    out_lst = []
    for el in lst:
        if el != x:
            out_lst.append(el)
    return out_lst

# find length of the largest list in the list of lists
def max_length(lol):
    return max([len(l) for l in lol])

def main():
    test_cases = [
        [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]],
        [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
    ]

    for case in test_cases:
        print "Input: ", case
        print "Output:", answer(case)

if __name__ == "__main__":
    main()
