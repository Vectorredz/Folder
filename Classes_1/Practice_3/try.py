def convert_to_dict(lst):
    result_dict = {}
    for key, value in lst:
        result_dict.setdefault(key, []).append(value)
    return result_dict

# Example usage:
input_list = [(100, 'k'), (100, 'p'), (300, 'l')]
output_dict = convert_to_dict(input_list)
print(output_dict)
