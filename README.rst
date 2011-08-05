jexp
====

:synopsis: A silly little JS expression builder to let you use native Python to build Javascript expression strings.

This package only allows the creation of simple (that is, non-assignment) Javascript expressions using an intuitive Python DSL.

Logical Expressions
===================

  >>> from jexp import J

  >>> e = J('var_1') & J('var_2')

  >>> str(e)

  '(var_1&&var_2)'

  >>> str(e | 'abc')

  '((var_1&&var_2)||"abc")'

The argument to the J class will be output as a str in the resulting JS- so ``J('my_var')`` is a good way to refer to a var, and ``J(5)`` to the number literal 5. If you need an actual string, you can either add the quotes yourself in the J call - ``J('"my string"')`` - or otherwise combine the J object with a str, as shown above.

Mathematical Expressions
========================

  >>> str(J(5) + 28)

  '(5+28)'

  >>> str(J('my_var') + 28)

  '(my_var+28)'

Division hasn't been implemented, but other things you expect are there.

Comparisons
===========

  >>> e = J(5) <= 6

  >>> str(e)

  '(5<=6)'

  >>> str(e == "test_string")

  '((5<=6)=="test_string")'

Attribute Access
================

  >>> e = J('my_var').attribute
  
  >>> str(e)

  'my_var.attribute'

This should work for any attribute that doesn't start with an underscore (and some that do).

Function Calling
================

  >>> e = J('func')('a','b')

  >>> str(e)

  'func("a","b")'

You can also try this with other J objects.

  >>> str(J('func')(J('arg1'),J('arg2')))

  'func(arg1,arg2)'

