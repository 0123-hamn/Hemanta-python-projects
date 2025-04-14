import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    while True:
        try:
            plen = int(input("Enter password length (minimum 4): "))
            if plen < 4:
                print("Password length must be at least 4 characters")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print("Your password is:", "".join(random.sample(s,plen)))


