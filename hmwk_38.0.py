import sys
import inspect
from inspect import getmodule

import requests
from PIL.ImageMode import getmode


def introspection_info(obj):
    atr_methods = dir(obj)
    methods = []
    attributes = []
    c = []
    for i in atr_methods:
        if callable(getattr(obj, i)) == True:
            methods.append(i)
        else:
            attributes.append(i)
    return f'type: {type(obj)}, attributes: {attributes}, methods: {methods}, module: {getmodule(introspection_info)}, function: {inspect.isfunction(obj)}, class: {inspect.isclass(obj)}, builtin: {inspect.isbuiltin(obj)}'

number_info = introspection_info(42)
print(number_info)