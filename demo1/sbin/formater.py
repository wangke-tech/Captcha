#!/usr/bin/env python
# encoding: utf-8

import os
path = '../font/'


def rename(path):
    """批量重命名
    """
    for f in os.listdir(path):
        if f.endswith('.gif'):
            if os.path.isfile(os.path.join(path, f)):
                fn = f.replace('gif', 'tiff')
                os.rename(os.path.join(path, f), os.path.join(path, fn))
                print 'rename %s ok' %fn

if '__main__' == __name__:
    rename(path)
