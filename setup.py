
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='tfnumpy',
      version="0.0.1a01",
      description="Collection of Simple Numerical Routines using TensorFlow",
      long_description="Collection of simple numerical routines, independent of each other",
      classifiers=[
          "Topic :: Scientific/Engineering :: Information Analysis",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
      ],
      keywords="numerics computation tensorflow",
      url="https://github.com/stephenhky/TFNumPy",
      author="Kwan-Yuet Ho",
      author_email="stephenhky@yahoo.com.hk",
      license='MIT',
      packages=['tfnumpy',
                'tfnumpy.embed',
                ],
      install_requires=[
          'numpy', 'tensorflow',
      ],
      tests_require=[
          'unittest2',
      ],
      include_package_data=True,
      test_suite="test",
      zip_safe=False)
