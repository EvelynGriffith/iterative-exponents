# Iterative Exponentiation

## Evelyn Griffith

## Program Output

### What is the output from running the `iterator` program?

- `poetry run iterator --whileloop --forloop --minimum 2 --maximum 10`

```Calculating the powers of 2 from 0 to 10 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? Yes

  Here is the output with the for loop.

   2**0 = 1
   2**1 = 2
   2**2 = 4
   2**3 = 8
   2**4 = 16
   2**5 = 32
   2**6 = 64
   2**7 = 128
   2**8 = 256
   2**9 = 512

  Here is the output with the while loop.

   2**0 = 1
   2**1 = 2
   2**2 = 4
   2**3 = 8
   2**4 = 16
   2**5 = 32
   2**6 = 64
   2**7 = 128
   2**8 = 256
   2**9 = 512

Wow, all of that iteration was exhausting! 😂
```

- `poetry run iterator --forloop --minimum 0 --maximum 5`

```Calculating the powers of 2 from 0 to 5 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? No

  Here is the output with the for loop.

   2**0 = 1
   2**1 = 2
   2**2 = 4
   2**3 = 8
   2**4 = 16

Wow, all of that iteration was exhausting! 😂
```

- `poetry run iterator --whileloop --minimum 0 --maximum 10`



### What is the output from running the test suite for the `iterator` program?

```============================================================== test session starts ==============================================================
platform win32 -- Python 3.8.2, pytest-7.0.1, pluggy-1.0.0
rootdir: C:\Users\gforc\computer-science-102-spring-2022-ee-3-iterative-exponent-EvelynGriffith\iterator
collected 4 items

tests\test_iterate.py ....

=============================================================== 4 passed in 0.10s =============================================================== 
```

## Source Code and Configuration Files

### Describe in detail how the provided source code works

#### How does the following source code segment define the command-line interface for `iterator`?

```
def main(
    forloop: bool = typer.Option(False, "--forloop"),
    whileloop: bool = typer.Option(False, "--whileloop"),
    minimum: int = typer.Option(1, min=0, max=100),
    maximum: int = typer.Option(5, min=0, max=100),
):
```
This is the main CLI function and specifically the argument definition within the naming line of the function. This line will take the names of the 

#### What is the purpose of the following function in the context of the `iterator` program?

```
def convert_bool_to_answer(argument: bool):
    """Return a string-based and human-readable representation of a bool."""
    if argument:
        return "Yes"
    return "No"
```

## Professional Reflection

### What do you find most challenging about implementing and testing Python programs? Why?

TODO: Provide a one-paragraph response that answers this question in your own words.

### In your view, what does it mean to be an ethical Python programmer?

TODO: Provide a one-paragraph response that answers this question in your own words.

### After completing this assignment, what is one experience for which you are grateful?

TODO: Provide a one-paragraph response that answers this question in your own words.
