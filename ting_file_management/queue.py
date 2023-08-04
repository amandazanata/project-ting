from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):

        self.data = list()
        self.length = 0

    def __len__(self):

        return self.length

    def enqueue(self, value):

        self.data.append(value)
        self.length += 1

    def dequeue(self):

        if len(self.data) == 0:
            return None
        clear = self.data.pop(0)
        self.length -= 1
        return clear

    def search(self, index):

        if index < 0 or index > (len(self.data) - 1):
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            for i in range(len(self.data)):
                if i == index:
                    return self.data[index]
