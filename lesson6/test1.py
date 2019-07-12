from collections import Counter


if __name__ == '__main__':
    temp_str = ''
    with open('test1', 'r') as f:
        for line in f:
            temp_str += line
    temp_str = temp_str.split()
    temp_counter = Counter(temp_str)
    counter = temp_counter.most_common(5)
    place = 1
    final_str = ''
    for j in counter:
        final_str += "on the {} place is '{}' with {} occurrences\n".format(place, j[0], j[1])
        place += 1
    with open('test1_result.txt', 'w') as f:
        f.write(final_str)
