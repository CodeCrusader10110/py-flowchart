"""
asdf
"""
import string
import secrets

def _generate_id() -> str:
    # TODO docstring
    # unique hash ids should be 12 digits (a-z, A-Z, 0-9)
    alphabet = string.ascii_letters + string.digits
    id = ''.join(secrets.choice(alphabet) for _ in range(12))
    return id

def main():
    ids = set()
    for _ in range(10):
        # id = ''
        # while id == '' or id in ids: # how to get new id if id was in set?
        #     id = _generate_id()
        id = _generate_id()
        print(id)

if __name__ == '__main__':
    main()