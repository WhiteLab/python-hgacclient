import logging

plugins = dict()

def plugin(f):
  '''
  A simple plugins decorator.
  Decorator takes a name as input.
  Optionally, can be given one or more namespaces in addition to the name.
  Otherwise, will default to the 'default' namespace.

  Example:
    @plugin
    def a_function():
      ...

    @plugin
    def some_function():
      ...
    
    plugin.plugins
    {
      'a_function': <function a_function at ...>,
      'some_function': <function some_function at ...>,
    }
  '''
  plugin.__dict__[f.__name__] = f
  return f
