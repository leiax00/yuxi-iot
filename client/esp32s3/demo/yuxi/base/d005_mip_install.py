# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mip

def init_dependencies(dependencies=None):
    if dependencies is None:
        dependencies = []
    for dep in dependencies:
        mip.install(dep)


if __name__ == '__main__':
    init_dependencies(['base64'])