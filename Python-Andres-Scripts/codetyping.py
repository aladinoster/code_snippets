from typing import NewType
import sys
print(sys.version)

UserId = NewType('UserId', int)
some_id = UserId(524313)


def get_user_name(user_id: UserId):
    print(f'Getting {user_id}')


def get_another_user(user_id: UserId)->str:
    print(f'Getting {user_id}')
    return user_id


if __name__ == "__main__":
    some_id = UserId(524313)
    get_user_name(some_id)
    get_another_user(some_id)
