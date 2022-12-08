def get_unique_slice(line, slice_length, start=0):
    last_index = [-1] * 26
    slice_start = 0
    for i in range(start, len(line)):
        char_val = ord(line[i]) - ord("a")
        if i - slice_start == slice_length:
            return i

        if last_index[char_val] != -1:
            slice_start = max(slice_start, last_index[char_val] + 1)
        last_index[char_val] = i

    return -1


line = input()
start_of_packet = get_unique_slice(line, 4)
start_of_message = get_unique_slice(line, 14, start_of_packet - 4)
print(start_of_packet)
print(start_of_message)
