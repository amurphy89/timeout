from setuptools import setup


setup(
    name = 'timeout',
    version = '0.1.0',
    packages = ['timeout'],
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'timeout = timeout.__main__:main'
        ]
})