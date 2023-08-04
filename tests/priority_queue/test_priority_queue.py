import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():

    pQueue = PriorityQueue()
    list_1 = {
        "qtd_linhas": 5
    }
    list_2 = {
        "qtd_linhas": 1
    }
    list_3 = {
        "qtd_linhas": 2
    }

    pQueue.enqueue(list_1)
    pQueue.enqueue(list_2)
    pQueue.enqueue(list_3)

    assert len(pQueue) == 3

    assert pQueue.search(2) == {
        "qtd_linhas": 5
    }

    assert pQueue.dequeue() == {
        "qtd_linhas": 1
    }

    assert len(pQueue) == 2

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pQueue.search(-1)
