from setuptools import setup, find_packages

setup(
    name='banana_py',
    version='0.1.0',
    description='OAuth2 Backend for MailChimp',
    long_description='',
    keywords='django, mailchimp, oauth2',
    author='Kenneth Love <kenneth@gigantuan.net>, Chris Jones <chris@brack3t.com>',
    author_email='kenneth@gigantuan.net',
    url='replace with github',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['oauth2', 'simplejson', 'django'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
