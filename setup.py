from distutils.core import setup

setup(
    name='captcha2uploadcasesensitive',
    packages=['captcha2uploadcasesensitive'],
    package_dir={'captcha2uploadcasesensitive': 'src/captcha2uploadcasesensitive'},
    version='0.2',
    install_requires=['requests'],
    description='Upload your image and solve captche using the 2Captcha '
                  'Service',
    author='Priyanka Biswas',
    author_email='priyanka.biswas@headout.com',
    url='https://github.com/headout/captcha2uploadcasesensitive/',
    download_url='https://github.com/Mirio/captcha2upload/tarball/0.1',
    keywords=['2captcha', 'captcha', 'Image Recognition'],
    classifiers=["Topic :: Scientific/Engineering :: Image Recognition"],
)
