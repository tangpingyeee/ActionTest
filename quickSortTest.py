import pytest
import sys
import os

os.chdir('../ActionTest')
print(os.getcwd())
sys.path.append('')
import quickSort
import random


class TestSort:
    def test_EmptyList(self):
        l = []
        result = quickSort.quick_sort(l)
        assert list(result) == []

    def test_SingleNumberList(self):
        l = []
        r = random.randint(1, 100)
        l.append(r)
        result = quickSort.quick_sort(l)
        assert list(result) == [r]

    def test_randomList(self):  # 内部循环20次
        for j in (0, 20):
            l = []
            for i in (1, random.randint(0, 20)):
                u = random.randint(1, 100)
                l.append(u)
            result = quickSort.quick_sort(l)
            tr = sorted(l)
            assert list(result) == list(tr)


if __name__ == "__main__":
    pytest.main(['-v', 'quickSortTest.py::TestSort'])
