import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyEanGenerator",
    version="0.0.7",
    author="VERCHERE Rémi",
    author_email="remi.verchere2@gmail.com",
    description="A simple package to generate EAN13 and EAN8",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url ="https://github.com/Gegelascience/pyEanGenerator",
    
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    license="MIT",
    python_requires=">=3.6",

)