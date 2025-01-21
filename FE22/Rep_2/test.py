def encode(string: str, shift: int, salt: list):
    """
    Encodes the given string using a shift and salt values interspersed into the ASCII values.
    """
    # Step 1: Apply the shift to the ASCII values of the string
    shifted_ascii = [ord(char) + shift for char in string]

    # Step 2: Interleave the salt values into the shifted ASCII values
    salted_ascii = []
    salt_index = 0  # Tracks the current index of salt
    for idx, value in enumerate(shifted_ascii):
        salted_ascii.append(value)  # Add the shifted value
        if idx % 2 == 0 and salt_index < len(salt):
            salted_ascii.append(salt[salt_index])
            salt_index += 1

    # Add any remaining salt values
    while salt_index < len(salt):
        salted_ascii.append(salt[salt_index])
        salt_index += 1

    # Step 3: Convert the salted ASCII values back into a string
    encoded_string = ''.join(chr(value) for value in salted_ascii)

    return shifted_ascii, salted_ascii, encoded_string


def decode(encoded_string: str, shift: int, salt: list):
    """
    Decodes the encoded string by reversing the encoding process.
    """
    # Step 1: Convert the encoded string into ASCII values
    salted_ascii = [ord(char) for char in encoded_string]

    # Step 2: Remove the salt values to extract the shifted ASCII values
    salt_set = set(salt)  # Use a set for fast lookup of salt values
    shifted_ascii = []
    is_salt_position = True  # Toggle every other position to mimic encoding
    for value in salted_ascii:
        if value in salt_set and is_salt_position:
            is_salt_position = not is_salt_position
            continue
        shifted_ascii.append(value)
        is_salt_position = not is_salt_position

    # Step 3: Reverse the shift to retrieve the original ASCII values
    original_ascii = [value - shift for value in shifted_ascii]

    # Step 4: Convert the original ASCII values back into the original string
    original_string = ''.join(chr(value) for value in original_ascii)

    return salted_ascii, shifted_ascii, original_string


print(encode("hello", 3, [65, 99, 120]))
print(decode("kAhcoxoArc", 3, [65, 99, 120]))
print(encode("hello", 3, [65, 99, 120]) ==
      ([107, 104, 111, 111, 114], [107, 65, 104, 99, 111, 120, 111, 65, 114, 99], 'kAhcoxoArc'))
print(decode("kAhcoxoArc", 3, [65, 99, 120]) ==
      ([107, 65, 104, 99, 111, 120, 111, 65, 114, 99], [107, 104, 111, 111, 114], 'hello'))
