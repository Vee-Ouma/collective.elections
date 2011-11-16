# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='matem.voting',
      version=version,
      description="A voting system for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Héctor Velarde',
      author_email='hector.velarde@gmail.com',
      url='https://github.com/collective/matem.voting',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['matem'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )