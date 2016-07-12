from distutils.core import setup

setup (
    name = "jython-sqlite3",
    version = "0.1.3",
    description = "Lightweight wrapper for using sqlite3 in Jython (JVM alternative to C Python's sqlite3 extension module - 'pysqlite')",
    packages = ["sqlite3"],
    author = "Anthony Hendrickson",
    author_email = "ahendrickson@ausinc.com",
    url = "https://github.com/anthonyhendrickson/jython-sqlite3",
    download_url = "https://github.com/anthonyhendrickson/jython-sqlite3/archive/0.1.3.tar.gz"
)
