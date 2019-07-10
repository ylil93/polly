from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='polly',
    version='1.0',
    author='Lily Li',
    url='https://github.com/ylil93/polly',
    description='Lambda function to deliver a poll question every week',
    long_description=long_description,
    long_description_content_type='text/markdown',
    data_files=['.env'],
    install_requires=['discord.py', 'python-dotenv'],
    setup_requires=['lambda_setuptools'],
    python_requires='>=3.6',
    lambda_function='polly.polly:lambda_polly',
    lambda_module='polly',
)
