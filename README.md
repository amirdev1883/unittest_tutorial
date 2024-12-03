## doctest 

```python
"""
>>> sub(2, 2)
0
>>> mult(0, 3)
0
"""

def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(-1, 2)
    1
    >>> add(0, 5)
    5
    """
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

```


## unittest

I used unittest1 folder 
one.py
```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def dev(a, b):
    if b == 0 :
        raise ZeroDivisionError('you cant divide by ziro .................')
    
    return a/b
```
test_one.py
```python
import unittest
import one

class OneTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(one.add(2,3), 5)

    def test_sub(self):
        self.assertEqual(one.sub(0, -3), 3)

    def test_div(self):
        self.assertEqual(one.dev(30, 5), 6)
        self.assertRaises(ZeroDivisionError, one.dev, 50, 3)


if __name__ == '__main__':
    unittest.main()
```

```bash
python3 -m unittest test_one.py
python3 -m unittest -v test_one.py

python3 -m unittest discover
# it will discover the test and run them 
```

### fixtures









