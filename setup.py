import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ALMassachusetts',
      version='0.1.2',
      description=('A docassemble extension of the AssemblyLine project that provides a foundation of Massachusetts-specific data, functionality, and questions.'),
      long_description='# docassemble.ALMassachusetts\r\n\r\nA docassemble extension of the AssemblyLine project that provides a foundation of Massachusetts-specific data, functionality, and questions.\r\n\r\n## Author\r\n\r\nSuffolk Law School Legal Innovation and Technology Lab\r\n',
      long_description_content_type='text/markdown',
      author='AssemblyLine Team',
      author_email='litlab@suffolk.org',
      license='The MIT License (MIT)',
      url='https://suffolklitlab.org/docassemble-AssemblyLine-documentation/docs',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.MACourts>=0.0.58.2'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ALMassachusetts/', package='docassemble.ALMassachusetts'),
     )

