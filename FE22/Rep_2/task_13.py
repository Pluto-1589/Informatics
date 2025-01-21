# Your implementation of the necessary class(es)

def encode(original, insertion, num):

    # COMPLICATED PART
    for i in insertion:
        original_ins = "".join(char + insertion[i % len(insertion)]
                               for i, char in enumerate(original))
        original_ins_lst = [c for c in original_ins]

    ord_lst = []

    for i in original_ins:
        ord_lst.append(ord(i))

    ord_lst = [i + num for i in ord_lst]

    char_conv_lst = [chr(i) for i in ord_lst]

    res_encoded = "".join(char_conv_lst)

    return (original_ins_lst, ord_lst, res_encoded)


def decode(encryption, insertion, num):

    encryption_ord = [ord(i) for i in encryption]

    rotate_encryption = [i - num for i in encryption_ord]

    decode_letters = [chr(i) for i in rotate_encryption]

    decode_encryption = [
        char for char in decode_letters if char not in insertion]

    res_decoded = "".join(decode_encryption)

    return (encryption_ord, decode_letters, res_decoded)


print(encode("hello", "xyz", -2))
# print(decode("fvcwjxjvmw", "xyz", -2))
# print(encode("hello", "xyz", -2) ==
#       (['h', 'x', 'e', 'y', 'l', 'z', 'l', 'x', 'o', 'y'], [102, 118, 99, 119, 106, 120, 106, 118, 109, 119], 'fvcwjxjvmw'))
# print(decode("fvcwjxjvmw", "xyz", -2) ==
#       ([102, 118, 99, 119, 106, 120, 106, 118, 109, 119], ['h', 'x', 'e', 'y', 'l', 'z', 'l', 'x', 'o', 'y'], 'hello'))
