from setuptools import setup, find_packages

readme = open('README.md').read()
setup(name='SparkJobManager',
            version='0.1',
            author='Wang Qiang',
            author_email='wangqiang8511@gmail.com',
            license='MIT',
            description='Package for call spark job server api',
            long_description=readme,
            packages=find_packages())
