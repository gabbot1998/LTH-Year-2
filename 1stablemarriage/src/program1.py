import sys

# "It ain't pretty, but it works"

def main():
    file = sys.stdin.read()
    file = [int(i) for i in file.split()]

    n = file[0]
    del file[0]

    twink = {}
    bear = {}

    for row in range(2 * n):
        line = file[:n+1]
        del file[:n+1]
        i = line[0]
        preferences = line[1:]

        if i not in twink:  # First occurence of index i -> Must be twink
            twink[i] = sort_twink_pref(preferences, n)
        else:  # Must be bear
            bear[i] = preferences

    index_of_bears = list(bear.keys())
    perfect_matches = {}

    while (len(index_of_bears) != 0):
        current_bear = index_of_bears[0]  # The indexing of all bears
        del index_of_bears[0]

        current_twink = bear[current_bear][0]  # The highest rated twink.
        del bear[current_bear][0]  # If most prefered twink has no partner

        if current_twink not in perfect_matches:
            perfect_matches[current_twink] = current_bear

        # Else, if current_bear is higher rated than current partner, replace
        else:
            current_twink_pref = twink[current_twink]
            partner_to_current_twink = perfect_matches[current_twink]
            current_partner_rating = current_twink_pref[partner_to_current_twink - 1]  # Minus one since it is array
            current_bear_rating = current_twink_pref[current_bear - 1]  # Minus one since it is array

            if current_bear_rating < current_partner_rating:
                perfect_matches[current_twink] = current_bear
                index_of_bears.append(partner_to_current_twink)

            else:
                index_of_bears.append(current_bear)

    for person in range(n):
        print(perfect_matches[person+1])


def dict_to_list(dict):
    list = []
    for i in range(len(dict)):
        list.append(dict[i + 1])
    return list


def sort_twink_pref(preferences, n):
    new_list = [0] * n
    # print(preferences)
    for i in range(len(preferences)):
        person = preferences[i]
        new_list[person - 1] = i + 1
    return new_list


if __name__ == "__main__":
    main()
