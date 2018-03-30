from planner.__init__ import __version__
from setuptools import setup, find_packages

setup(name='planner',
      version= __version__,
      py_modules=['planner'],
      install_requires=[
          'Click',
          ],
      entry_points='''
          [console_scripts]
          planner=planner.main:cli
      ''', # This is actually referring to a cli() function...
      description='Because you want to plan your day on the command line',
      url='http://github.com/ModoUnreal/Planner',
      author='Alex Hurtado',
      author_email='modounreal@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)

