

class SimpleDatabase:

    class Items:
        count = 0
        items = []

        @classmethod
        async def create(cls):
            cls.items.append(f"Item {cls.count}")
            cls.count += 1

        @classmethod
        async def get_all(cls):
            return cls.items

        @classmethod
        async def get(cls, index: int):
            try:
                item = cls.items[index]
            except IndexError:
                item = None
            return item

    class Users:
        count = 0
        users = []

        @classmethod
        async def create(cls):
            cls.users.append(f"User {cls.count}")
            cls.count += 1

            return cls.users[cls.count - 1]

        @classmethod
        async def get_all(cls):
            return cls.users

        @classmethod
        async def get(cls, index: int):
            try:
                user = cls.users[index]
            except IndexError:
                user = None
            return user
