def find_sublists_with_common_elements(lst):
    result = []
    for i, sublist1 in enumerate(lst):
        for j, sublist2 in enumerate(lst):
            if i != j and any(element in sublist1 for element in sublist2):
                result.append(sublist1)
                break
    return result

