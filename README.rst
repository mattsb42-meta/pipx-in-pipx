############
pipx-in-pipx
############

.. image:: https://img.shields.io/pypi/v/pipipxx.svg
   :target: https://pypi.python.org/pypi/pipipxx
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/pipipxx.svg
   :target: https://pypi.python.org/pypi/pipipxx
   :alt: Supported Python Versions

.. image:: https://img.shields.io/badge/code_style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black


+----------+-----------------+---------------------------------+
| docs     | read-the-docs   | |Read The Docs|                 |
+----------+-----------------+---------------------------------+
| linux    | static analysis | |Travis CI|                     |
+----------+-----------------+---------------------------------+
| linux    | CPython 3.7     | |CodeBuild Linux CPython 3.7|   |
+----------+-----------------+---------------------------------+
| windows  | CPython 3.7     | |CodeBuild Windows CPython 3.7| |
+----------+-----------------+---------------------------------+


.. |Read The Docs| image:: https://readthedocs.org/projects/pipx-in-pipx/badge/
   :target: https://pipx-in-pipx.readthedocs.io/
   :alt: Documentation Status
.. |Travis CI| image:: https://travis-ci.org/mattsb42/pipx-in-pipx.svg?branch=master
   :target: https://travis-ci.org/mattsb42/pipx-in-pipx
   :alt: Travis CI Test Status
.. |CodeBuild Linux CPython 3.7| image:: https://codebuild.us-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZi9uT0MrNGNXV2RSbitIdTBhM1BXTDBSR2ZjbEZmK3lBTmUxS1hkbUc5azFXVDIwdnFOdjRwUG95QnNHUDFwV0xjemhXcDcvVjdaNFEweGdVRFBsdEZNPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik9TRWdNbmpMKzRwZGxvMUIiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master
   :target: https://us-west-2.console.aws.amazon.com/codesuite/codebuild/projects/LinuxCodeBuild-s5JgvxjQs15C/history?region=us-west-2
   :alt: Linux Python 3.7
.. |CodeBuild Windows CPython 3.7| image:: https://codebuild.us-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiQ1BUdWNIamZaZUpnRkVBdTZxbmJkNmVrMnpCWnlBbFZvVkcyNmp1cG1tZ2dkVzVMYzR1OHE1VnRmZTFSaGhLQ29vK2ZPZEJvKzJwWFhVVTdIZ2dzNjVnPSIsIml2UGFyYW1ldGVyU3BlYyI6Ildkdkw3OW5zdmRmTFQydVAiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master
   :target: https://us-west-2.console.aws.amazon.com/codesuite/codebuild/projects/WindowsCodeBuild-BVQ5nOqkXcWR/history?region=us-west-2
   :alt: Linux Python 3.7


`pipx`_ is great for keeping your CLI tools isolated and your system Python paths clean.
However, it still requires that you install `pipx`_ *itself* in your system Python.

But `pipx`_ is a CLI tool installed through ``pip``...why not install `pipx`_ with `pipx`_?
Why not indeed!


With ``pipx-in-pipx``, all you need to do is install :

.. code:: shell

    $ pip install pipx-in-pipx

But wait! You say.
Didn't you just say that we shouldn't install things to system Python?

Yes.
What ``pipx-in-pipx`` actually does is slightly (but only slightly) evil.
Rather than actually installing anything when you run "install",
``pipx-in-pipx`` instead builds a temporary virtual environment,
installs `pipx`_ there,
and then uses *that* `pipx`_ to install `pipx`_ in your user local space,
just like any other `pipx`_-installed tool.

What you end up with is a `pipx`_ installation that is *itself* managed by `pipx`_.


Sharp Edges
***********

Which Python?
=============

By default, `pipx`_ uses its own Python for each environment that it creates.
Normally, this would be the system Python, whatever it was when you installed `pipx`_.
However, when your are using a ``pipx-in-pipx``-installed `pipx`_,
the default Python that `pipx`_ uses for each environment it creates is instead
whatever Python you used to "install" ``pipx-in-pipx``.

This has two notable side effects:

#. If you uninstall your `pipx`_-managed `pipx`_,
   then all of the tools that you installed using that `pipx`_ will stop working
   because their Pythons suddenly point to nothing.
#. If you want to change the Python used by all of your `pipx`_-managed tools,
   you only need to reinstall one of them (`pipx`_) rather than reinstalling all of them.


Uninstalling
============

`pipx`_ has a handy feature to uninstall *all* `pipx`_-managed tools.
Because you have now made `pipx`_ manage itself,
running ``pipx uninstall-all`` *will also* uninstall `pipx`_.

This is not a bug, but a feature.
By installing `pipx`_ using ``pipx-in-pipx``,
you have expressed an intent that you *want* `pipx`_ to manage itself.
If that's not what you want, this is not the tool for you.

If you at any point uninstall your `pipx`_-managed `pipx`_,
you can simply ``pip install pipx-in-pipx`` again to rebuild it.


.. _pipx: https://pipxproject.github.io/pipx/
