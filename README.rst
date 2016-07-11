TODO
^^^^
- PEP 249 (DB-API 2.0 Spec): https://www.python.org/dev/peps/pep-0249/

----------


Class-Path Dependency
^^^^^^^^^^^^^^^^^^^^^

This module makes use of the sqlite-jdbc package ("org.xerial:sqlite-jdbc:3.8.11.2")

It will need to be added to the Jython interpreter's class-/import-path. If you are using Jython as an embedded language in Java and you plan on using *any* Python modules which use the sqlite3 C-extension, you'll need to read the setup below.


Embedded Jython
^^^^^^^^^^^^^^^

**Building with Gradle**

First up, you'll want the following gradle plugin for declaring jython module dependencies:

.. code:: gradle

  plugins {
      ...
      id "com.github.hierynomus.jython" version "0.3.0"
  }

You'll also need the sqlite-jdbc jar holding this module together, and include this module as well:

.. code:: gradle

  dependencies {
      ...
      runtime "org.xerial:sqlite-jdbc:3.8.11.2"
      jython "anthonyhendrickson:jython-sqlite3:0.1.0:sqlite3"
  }

*Note: there are other methods of adding the jython-sqlite3 module for runtime usage, but none so clean.*
