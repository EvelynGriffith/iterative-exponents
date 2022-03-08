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

 ```Should I use a for loop? No
  Should I use a while loop? Yes

  Here is the output with the while loop.

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

```def main(
    forloop: bool = typer.Option(False, "--forloop"),
    whileloop: bool = typer.Option(False, "--whileloop"),
    minimum: int = typer.Option(1, min=0, max=100),
    maximum: int = typer.Option(5, min=0, max=100),
):
```

This is the main CLI function and specifically the argument definition within the naming line of the function. The first two lines will take the names of the specific ways that we will be running the programs, in the run command, and will allow us to classify the way that we will call either the for or while loop functions respectively when we run the final commands for the program. The next two lines are a way for use to specify parameters for the minimum and the maximum.

#### What is the purpose of the following function in the context of the `iterator` program?

```def convert_bool_to_answer(argument: bool):
    """Return a string-based and human-readable representation of a bool."""
    if argument:
        return "Yes"
    return "No"
```

This function will take a boolean answer from another function and will allow that answer to be converted into a "human readable boolean" answer that can then be passed into a CLI function. This is very useful because it can give us an answer to complex functions so that we can understand what the program is passing in and out.

## Professional Reflection

### What do you find most challenging about implementing and testing Python programs? Why?

To be honest I think the most challenging aspect of the lab was more in the coding of the display of the outputs as opposed to in the test cases. Once I had my code correctly implemented my test cases were able to run smoothly. I did use my test cases in order to figure out some errors which was helpful.

### In your view, what does it mean to be an ethical Python programmer?

I think being an ethical programmer is honoring other people's work as well as your own and only taking credit for your work, and I also think that being an ethical programmer is making sure to use the skills that you have with computers in order to help better technology and not as a way to abuse other people's lack of knowledge. For example people that hack into bank accounts or personal accounts for other things in order to acquire certain information are not using their abilities with coding ethically.

### After completing this assignment, what is one experience for which you are grateful?

I was really greatful for the teamwork and comradery at my table this week. I thought that working with the TLs as well as working with my classmates was really refreshing and fun especailly after COVID.