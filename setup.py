from setuptools import setup, find_packages
import networkx
setup(
    name='klassify',
    version='0.7',
    description='Redis based text classification service',
    author='Fatih Erikli',
    author_email='fatiherikli@gmail.com',
    url='https://github.com/fatiherikli/klassify',
    include_package_data=True,
    packages=[
        'klassify',
        'klassify.backend',
    ],
    install_requires=[
        'nltk==3.6.3',
        'tornado==4.3',
        'tornado-redis==2.4.18'
    ],
    classifiers=[
        'Environment :: Web Environment'
    ]
)
