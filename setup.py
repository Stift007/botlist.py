from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='botlistpy',
  version='0.0.1',
  description='An async wrapper around BotList.me\'s API',
  long_description=open('README.txt').read(),
  url='',  
  author='DS_Stift007',
  author_email='dsstift@icloud.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='botlist api wrapper', 
  packages=find_packages(),
  install_requires=['aiohttp','requests'] 
)