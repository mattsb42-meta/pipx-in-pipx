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


+----------+-----------------+-------------------+
| docs     | read-the-docs   | |Read The Docs|   |
+----------+-----------------+-------------------+
| tests    | static analysis | |Static Analysis| |
+----------+-----------------+-------------------+
| tests    | all tests       | |Tests|           |
+----------+-----------------+-------------------+


.. |Read The Docs| image:: https://readthedocs.org/projects/pipx-in-pipx/badge/
   :target: https://pipx-in-pipx.readthedocs.io/
   :alt: Documentation Status
.. |Static Analysis| image:: https://github.com/mattsb42-meta/pipx-in-pipx/workflows/static%20analysis/badge.svg
   :target: https://github.com/mattsb42-meta/pipx-in-pipx/actions?query=workflow%3A%22static+analysis%22
   :alt: Static Analysis
.. |Tests| image:: https://github.com/mattsb42-meta/pipx-in-pipx/workflows/tests/badge.svg
   :target: https://github.com/mattsb42-meta/pipx-in-pipx/actions?query=workflow%3Atests
   :alt: Tests


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
This is whatever you used when you installed `pipx`_.
This is most commonly the system Python,
but if you use ``pipx-in-pipx`` to install your `pipx`_,
it is the Python binary in the `pipx`_-managed virtualenv for `pipx`_.
This, in turn, points to the Python that you used to install ``pipx-in-pipx``.

This has a few notable side effects:

#. If you uninstall your `pipx`_-managed `pipx`_ (``pipx uninstall pipx``),
   all of the tools that you installed using that `pipx`_ will stop working
   because their Pythons suddenly point to nothing.

   * If you do this, you can fix it by installing ``pipx-in-pipx`` again.

#. If you reinstall all `pipx`_ packages (``pipx reinstall-all``),
   this uninstalls your `pipx`_-managed `pipx`_.

   * If you do this, you can fix it by installing ``pipx-in-pipx`` again.
   * If you want to reinstall all other packages,
     tell `pipx`_ to ignore `pipx`_ (``pipx reinstall-all --skip pipx``).
   * To reinstall `pipx`_, install ``pipx-in-pipx`` again.

#. Because all `pipx`_-managed packages use the Python in the `pipx`_ virtualenv,
   you can change the Python for all packages by
   installing ``pipx-in-pipx`` again.

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
