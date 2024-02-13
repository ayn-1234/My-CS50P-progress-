class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self.size = 0

    def __str__(self):
        result = ""
        for cookies in range(self.size):
            result += "🍪"
        return result

    def deposit(self, n):
        if n + self.size > self._capacity:
            raise ValueError("Deposit number exceeds capacity")
        elif n < 0:
            raise ValueError("You can't deposit negative cookies")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdraw number exceeds capacity")
        elif n < 0:
            raise ValueError("You can't withdraw negative cookies")

        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(2)
    print(jar)
    print(f"Size: {jar.size}")
    print(f"Capacity: {jar.capacity}")

if __name__ == "__main__":
    main()
#Completed Assingment
#Alhamdulliah
