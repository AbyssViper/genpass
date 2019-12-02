# -*- coding: utf-8 -*-
__author__ = 'AbyssViper'

import hashlib
import random
import time
import base64

input_value = input("Please input: ")
CANDIDATE_CHARS = ["%", "$", "^", "&", "(", ")", "#", "!", "=", "."]
PART_COUNT = 8


def get_md5_16(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()[8:-8]


def get_timestamp():
    return int(time.time())


def get_b64_part(data):
    b64_part_result = ""

    b64_result = str(base64.b64encode(data.encode("UTF-8")).decode("UTF-8"))
    random_index_list = []
    for i in range(PART_COUNT):
        random_index_list.append(random.randint(0, len(b64_result) - 1))

    for index in random_index_list:
        b64_part_result += b64_result[index]

    return b64_part_result


def get_result(data):
    result = ""

    hash_result = list(get_md5_16(data))
    random_int_time = random.randint(0, get_timestamp())

    for char_data in str(random_int_time):
        index = int(char_data)
        random_int_len = random.randint(0, len(hash_result) - 1)
        hash_result[random_int_len] = CANDIDATE_CHARS[index]

    for char_data in hash_result:
        result += char_data

    return "Result: " + result + "@" + get_b64_part(data)


if __name__ == '__main__':
    print("Current encryption content is: " + input_value)
    print(get_result(input_value))
