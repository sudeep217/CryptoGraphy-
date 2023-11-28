import hashlib

def hash_string(string, algorithm):
    if algorithm == "sha256":
        result = hashlib.sha256(string.encode())
    elif algorithm == "sha384":
        result = hashlib.sha384(string.encode())
    elif algorithm == "sha224":
        result = hashlib.sha224(string.encode())
    elif algorithm == "sha512":
        result = hashlib.sha512(string.encode())
    elif algorithm == "sha1":
        result = hashlib.sha1(string.encode())
    else:
        print("Invalid algorithm choice")
        return None
    return result.hexdigest()

def main():
    user_string = input("Enter the string: ")
    user_algorithm = input("Choose the hashing algorithm (sha256, sha384, sha224, sha512, sha1): ")
    hashed_result = hash_string(user_string, user_algorithm)
    if hashed_result is not None:
        print(f"The hexadecimal equivalent of {user_algorithm.upper()} is:")
        print(hashed_result)
if __name__ == "__main__":
    main()