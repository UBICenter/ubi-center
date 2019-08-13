from setuptools import setup

setup(name='ubicenter',
      version='0.1',
      description='Produce data and visualizations for UBI Center Plan Explorer.',
      url='http://github.com/UBICenter/ubi-center',
      author='Max Ghenis',
      author_email='mghenis@gmail.com',
      license='MIT',
      packages=['ubicenter'],
      install_requires=[
          'numpy',
          'pandas',
          'taxcalc',
          'matplotlib',
          'seaborn',
          'microdf'
      ],
      zip_safe=False)
