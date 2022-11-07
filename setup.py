import glob
from setuptools import setup, find_packages

# DO NOT put dependencies here. Dependencies should go into
# requirements.txt and THEY MUST BE pinned versions


exec(open('yolov7/version.py').read())
setup(
    name="yolov7",
    version=__version__,
    packages=find_packages(),
    url='https://github.com/RShevcheCape/yolov7',
    author="Rostyslav Shevchenko",
    description="Implementation of paper - YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors",
    scripts=glob.glob("scripts/*"),
    # This tells setuptools to include the files contained in the MANIFEST.in file
    #include_package_data=True,
    # This avoids the creation of a wheel
    #zip_safe=False,
)

