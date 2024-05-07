import re


def decode_matrix(matrix):
    transposed_matrix = list(zip(*matrix))
    columns = ["".join(col) for col in transposed_matrix]
    decoded_columns = [re.sub(r"(?<=\w)?[^\w]+(?=\w)", " ", col) for col in columns]
    decoded_script = "".join(decoded_columns)

    return decoded_script


# Example usage:
matrix = [
    ["%", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "&"],
    ["i", "r", "*"],
]

decoded_script = decode_matrix(matrix)
print(decoded_script)
