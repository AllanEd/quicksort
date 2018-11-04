class Index(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Quicksort(object):
    def __init__(self, numbers):
        self.numbers = numbers

    def sort(self):
        index = Index(0, len(numbers) - 1)
        self.quicksort(index)

    def quicksort(self, index):
        if index.left < index.right:
            q = self.partition(index)
            self.quicksort(Index(index.left, q - 1))
            self.quicksort(Index(q + 1, index.right))

    def partition(self, index):
        x = self.numbers[index.right]
        i = index.left - 1

        for j in range(index.left, index.right):
            if self.numbers[j] <= x:
                i = i + 1
                self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]

        i = i + 1
        self.numbers[i], self.numbers[index.right] = self.numbers[index.right], self.numbers[i]
        return i


if __name__ == '__main__':
    numbers = [5, 3, 2, 7, 3, 4]
    quicksort = Quicksort(numbers)
    quicksort.sort()
    print(quicksort.numbers)
