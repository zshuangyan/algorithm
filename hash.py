import hashlib
import random

CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def hash_str(input: str):
    hash_obj = hashlib.sha1(input.encode("utf-8"))
    hex_dig = hash_obj.hexdigest()
    return hex_dig

def random_string(length, choices=CHARS):
    return ''.join(random.sample(choices, length))

def hash_with_salt(input: str) -> (str, str):
    salt = random_string(16)
    hash_result = hash_str(input+":"+salt)
    return hash_result, salt

if __name__ == "__main__":
    for item in ["java", "python", "golang"]:
        print("word: %-8s, after hash: %s" % (item, hash_str(item)))

    print("test random string generate")
    for i in range(3):
        print("get random string: %s" % random_string(16))


    for item in ["java", "python", "golang"]:
        result, salt = hash_with_salt(item)
        print("word: %-8s, salt: %s, after hash with salt: %s" % (item, salt, result))
