from setuptools import setup, find_packages


version = '0.1'

setup(name='GeoAlchemy2',
      version=version,
      description="Using SQLAlchemy with Spatial Databases",
      long_description=open('README.rst').read(),
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Plugins",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Intended Audience :: Information Technology",
          "License :: OSI Approved :: MIT License",
          "Topic :: Scientific/Engineering :: GIS"
      ],
      keywords='geo gis sqlalchemy orm',
      author='Eric Lemoine',
      author_email='eric.lemoine@gmail.com',
      url='http://geoalchemy.org/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests', "doc"]),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'SQLAlchemy>0.7',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )