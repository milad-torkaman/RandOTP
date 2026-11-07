import secrets
import random


def create_otp_number(size: int = 6) -> str:
    """
    Make a code random
    """
    dnums = [str(n)*2 for n in range(1, 10)]

    res = []

    if size >= 3:
        rsize = size//3
        for _ in range(rsize):
            res.append(secrets.randbelow(10))
            res.append(random.choice(dnums))

        for _ in range(size - (rsize*3)):
            res.append(secrets.randbelow(10))
    elif size == 2:
        res.append(secrets.randbelow(10))
        res.append(secrets.randbelow(10))
    elif size == 1:
        res.append(secrets.randbelow(10))
    else:
        raise ZeroDivisionError

    random.shuffle(res)
    return ''.join([str(i) for i in res])


if __name__ == "__main__":
    otp_code = create_otp_number()
    print(otp_code)
