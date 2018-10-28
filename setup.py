from setuptools import find_packages, setup

setup(
    name="weather",
    version = "0.1",
    description = "micro app providing weather data",
    author = "jam",
    packages = find_packages(),
    install_requires = ["Flask==1.0.2","requests","flask-nicely","flask_sqlalchemy","PyMySQL","tornado==5.1.1","pytz"],
)
