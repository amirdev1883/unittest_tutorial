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

I used unittest2 folder 

person.py
```python
class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def get_fullname(self) -> str:
        return f'{self.fname}{self.lname}'

    def create_email(self):
        return f'{self.get_fullname()}@email.com'.replace(' ', '')
```
test_person.py
```python
import unittest
from person import Person

class PersonTest(unittest.TestCase):
    def test_get_fullname(self):
        p1 = Person('amir', 'arani')

        self.assertEqual(p1.get_fullname(), 'amirarani')

    def test_create_email(self):
        p1 = Person('amir', 'arani')

        self.assertEqual(p1.create_email(), 'amirarani@email.com')


if __name__ == "__main__":
    unittest.main()
```

but we assign p1 twice this is not effishent 
so we use fixture for assign p1 one time 

you can use this fixtures 
setUp(), tearDown(), setUpClass(), tearDownClass(), setUpModule(), tearDownModule()

```python
import unittest
from person import Person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('amir', 'arani')

    def tearDown(self):
        del self.p1

    def test_get_fullname(self):
        self.assertEqual(self.p1.get_fullname(), 'amirarani')

    def test_create_email(self):
        self.assertEqual(self.p1.create_email(), 'amirarani@email.com')

if __name__ == "__main__":
    unittest.main()
```

```
python3 -m unittest discover
python3 -m unittest test_person.py
```

### nose

```
pip install nose
```
```bash
nosetests

nosetests test_one.py
nosetests -v test_one.py
```
use this command to find test and run them

I used nose folder for this lesson

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

test_nose.py
```python
import one

def test_add():
    assert one.add(0, 8) == 8
    assert one.add(-2, -2) == -4
    assert one.add(-1, 4) == 3
    assert one.add(2, 3) == 5

def test_sub():
    assert one.sub(2, 2) == 0
    assert one.sub(2, -2) == 4
    assert one.sub(8, 0) == 8

```

## pytest 

```bash
pip install pytest

pytest test_one.py 
pytest -v test_one.py
```

you can run unittest test by pytest too











