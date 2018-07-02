def func(a, b=4, c=88):
    print(a, b, c)

func(b=1, c=2, 42)  # positional argument after keyword one

"""
  File "arguments.default.error.py", line 4
    func(b=1, c=2, 42)
                  ^
SyntaxError: non-keyword arg after keyword arg
"""
