import logging

class pluginmeta(type):
  plugins = dict()

  def __getattr__(cls,key):
    return cls.plugins[key]

class plugin(object):
  '''
  A simple plugins decorator.
  Decorator takes a name as input.
  Optionally, can be given one or more namespaces in addition to the name.
  Otherwise, will default to the 'default' namespace.

  Example:
    @plugin('a_func')
    def a_function():
      ...

    @plugin('test_func','one_namespace','two_namespace')
    def some_function():
      ...
    
    plugin.plugins
    {
      'default': {'a_func': <function a_function at ...>},
      'one_namespace': {'test_func': <function some_function at ...>},
      'two_namespace': {'test_func': <function some_function at ...>},
    }
  '''
  __metaclass__ = pluginmeta

  def __init__(self,namespace):
    self.namespace = namespace

  def __call__(self,f):
    try: plugin.plugins[self.namespace].append(f)
    except KeyError: plugin.plugins[self.namespace] = [f]
    return f
