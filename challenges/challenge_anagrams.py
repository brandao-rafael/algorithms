# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python


def merge_sort(string_list, start=0, end=None):
    if end is None:
        end = len(string_list)
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(string_list, start, mid)
        merge_sort(string_list, mid, end)
        return merge(string_list, start, mid, end)


def merge(string_list, start, mid, end):
    left = string_list[start:mid]
    right = string_list[mid:end]

    left_i, right_i = 0, 0

    for i in range(start, end):
        if left_i >= len(left):
            string_list[i] = right[right_i]
            right_i += 1
        elif right_i >= len(right):
            string_list[i] = left[left_i]
            left_i += 1
        elif left[left_i] < right[right_i]:
            string_list[i] = left[left_i]
            left_i += 1
        else:
            string_list[i] = right[right_i]
            right_i += 1

    return string_list


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())
    merge_sort(first_list)
    merge_sort(second_list)
    first_ordened = "".join(first_list)
    second_ordened = "".join(second_list)
    if first_ordened == "" or second_ordened == "":
        return (first_ordened, second_ordened, False)
    if first_ordened.lower() == second_ordened.lower():
        return (first_ordened, second_ordened, True)
    return (first_ordened, second_ordened, False)
