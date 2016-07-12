from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert("README.md", "rst")
    long_description = long_description.replace("\r","")
except(OSError):
    print("Pandoc not found. 'long_description' conversion failure.")
    import io
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

setup (
    name = "jython-sqlite3",
    version = "0.1.3.3",
    packages = ["sqlite3"],
    author = "Anthony Hendrickson",
    author_email = "ahendrickson@ausinc.com",
    url = "https://github.com/anthonyhendrickson/jython-sqlite3",
    download_url = "https://github.com/anthonyhendrickson/jython-sqlite3/archive/0.1.3.3.tar.gz",
    description = "Lightweight wrapper for using sqlite3 in Jython (JVM alternative to C Python's sqlite3 extension module - 'pysqlite')",
    long_description = long_description,
    keywords = ["jython", "sqlite", "sqlite3", "pysqlite"]
)
