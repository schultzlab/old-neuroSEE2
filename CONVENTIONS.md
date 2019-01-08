<!-- MarkdownTOC -->

- [Symbols](#symbols)
    - [Operators](#operators)
    - [Commas and colons](#commas-and-colons)
    - [Calling functions](#calling-functions)
    - [Brackets](#brackets)
    - [Indentation](#indentation)
- [Operators](#operators-1)
- [Names](#names)
    - [Variable And Functions](#variable-and-functions)
    - [Classes](#classes)
    - [Constants](#constants)

<!-- /MarkdownTOC -->

# Python 
Please try to follow the [PEP8 conventions](https://www.python.org/dev/peps/pep-0008/).
Below are a few common things to be aware of. (Adapted from [here](https://gist.github.com/math2001/3a6839f9d51a139b26cf2c4ecab02c9f))
## Symbols

### Operators


```python
# no
if this=='is ugly':
    print('right?')

# yes
if this == 'is beautiful':
    print('right?')

# same for '=', '+', '-', '/', '%', etc
```

### Commas and colons

The commas are a bit special, but natural: no space before, one space after. Same apply for colons.

```python
# no
if 'this' :
    print('is','ugly' , 'right?')
    my_dict = {'key' :"value"}

# yes
if 'this':
    print('is', 'ugly', 'right?')
    my_dict = {'key': "value"}
```

### Calling functions

This is just for when you *call* functions.

```python
# no
this ('is', 'ugly', 'right?')

# yes
this('is', 'beautiful', 'right?')
```

### Brackets

This convention applies for `[]`, `()`, and `{}`: no space after opening bracket or before the 
closing one.

```python
# no
my_tuple = ( 'this', 'is', 'ugly', 'right?' )
my_list = [ 'this', 'is', 'ugly', 'right?' ]

# yes
my_tuple = ('this', 'is', 'beautiful', 'right?')
my_list = ['this', 'is', 'beautiful', 'right?']
```

### Indentation

Your python code should be indented with tabs. (PEP8 actually recommends 4 spaces, but I disagree. Either way,
the important thing is that we are consistently only using one of the two; tabs.)

## Operators

For booleans (`True`, `False`) and `NoneType` (`None`), you should compare them using the `is` and 
`is not` operators, instead of `!=` and `==`:

```python
# no
if this == True:
    print('is ugly right?')

# yes
if this is True:
    print('is beautiful right?')
```

Though bear in mind that there *is* a difference between the two; `==` checks for
value equality and `is` checks whether two things are the same object in memory. 

## Names

### Variable And Functions

In python, your variable names should be written in `snake_case`. Not in `camelCase`, `PascalCase`,
or `I_Do_Not_Know_The_Name_Of_This_One`. Same apply for functions.

```python
# no
thisIsUgly == 'right?'
def And_This_Is_Too():
    return True

# yes
this_is_beautiful == 'right?'
def and_this_is_too():
    return True
```

### Classes

The classes you create are different: they should be written in `PascalCase`.

```python
# no
class this_is:

    def __init__(self):
        print('ugly')
        return 'right?'

# yes
class ThisIs:

    def __init__(self):
        print('beautiful')
        return 'right?'
```

### Constants
Please name your constants in `UPPER_CASE_WITH_UNDERSCORES`.