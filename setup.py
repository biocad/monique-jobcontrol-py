from setuptools import setup

setup(name='monique_jobcontrol_py',
      version='0.1.0.0',
      description='Python Jobcontrol for Monique system',
      url='https://github.com/biocad/monique-jobcontrol-py',
      author='Bogdan Neterebskii',
      author_email='neterebskiy@biocad.ru',
      license='BSD3',
      packages=['monique_jobcontrol_py'],
      zip_safe=False, install_requires=['pyzmq'])