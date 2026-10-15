# Lab 5 - Quadratic Roots

The lines that ask for `a`, `b` and `c` are already in `main.py`. Leave them as
they are. The prompts are `Enter coefficient a: `, `Enter coefficient b: ` and
`Enter coefficient c: `.

Open `main.py` and complete the following:

1. Update the header with your information (Name, Purpose, Author, Created, Updated).
2. Calculate the discriminant, `b² - 4ac`.
3. If the discriminant is negative, print `No Real Roots`.
4. If the discriminant is zero, there is one root. Print it once.
5. Otherwise there are two roots. Print both, smallest first.
6. Print each root on its own line as `Root: ____`, rounded to one decimal place with `round()`.

For example, a root of 5 prints as `Root: 5.0`, and roots of 8 and 5 print as:

```
Root: 5.0
Root: 8.0
```

Assume `a` is never 0.

## Running your program

Open `main.py` and press the Run button in the top right corner of VS Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B** to run the tests. You will see one line per test:

```
[PASS] 1. Header is filled in
[FAIL] 2. Two roots, negative a
```

When a test fails it shows what was expected and what your program printed. Fix your code and press Ctrl+Shift+B again. Keep going until all tests pass.

## Reminders

- Fill in every field of the header before you write any code.
- Write comments as you go. Explain what the discriminant tells you.
- Tests check your output exactly. `root: 5.0` is not the same as `Root: 5.0`.
- The quadratic formula gives the two roots in different orders depending on the sign of `a`. Use `min()` and `max()` to print them smallest first.
