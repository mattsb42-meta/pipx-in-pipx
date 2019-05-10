#######
pipipxx
#######

.. image:: https://img.shields.io/pypi/v/pipipxx.svg
   :target: https://pypi.python.org/pypi/pipipxx
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/pipipxx.svg
   :target: https://pypi.python.org/pypi/pipipxx
   :alt: Supported Python Versions

.. image:: https://img.shields.io/badge/code_style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black

.. image:: https://readthedocs.org/projects/pipipxx/badge/
   :target: https://pipipxx.readthedocs.io/en/stable/
   :alt: Documentation Status

.. image:: https://travis-ci.org/awslabs/pipipxx.svg?branch=master
   :target: https://travis-ci.org/awslabs/pipipxx
   :alt: Travis CI Test Status

.. image:: https://ci.appveyor.com/api/projects/status/REPLACEME/branch/master?svg=true
   :target: https://ci.appveyor.com/project/REPLACEME
   :alt: AppVeyor Test Status

.. important::

    This project is a work in progress and is not yet ready for use.

`pipx`_ is great for keeping your CLI tools isolated and your system Python paths clean.
However, it still requires that you install `pipx`_ *itself* in your system Python.

But `pipx`_ is a CLI tool installed through ``pip``...why not install `pipx`_ with `pipx`_?
Why not indeed!


With ``pipipxx`` (pronounced "pipx in pipx"), all you need to do is:

.. code:: shell

    $ pip install pipipxx

But wait! You say.
Didn't you just say that we shouldn't install things to system Python?

Yes.
What ``pipipxx`` actually does is slightly (but only slightly) evil.
Rather than actually installing anything when you run "install",
``pipipxx`` instead builds a temporary virtual environment,
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
However, when your are using a ``pipipxx``-installed `pipx`_,
the default Python that `pipx`_ uses for each environment it creates is instead
whatever Python you used to "install" ``pipipxx``.

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
By installing `pipx`_ using ``pipipxx``,
you have expressed an intent that you *want* `pipx`_ to manage itself.
If that's not what you want, this is not the tool for you.

If you at any point uninstall your `pipx`_-managed `pipx`_,
you can simply ``pip install pipipxx`` again to rebuild it.


.. _pipx: https://pipxproject.github.io/pipx/
