*********
Changelog
*********

1.0.1 -- 2019-10-27
===================

Administrivia
-------------

* Rename project from ``pipipxx`` to ``pix-in-pipx``.


Bugfixes
--------

* Fix Windows compatibility.
  `<#13 https://github.com/mattsb42/pipx-in-pipx/pull/13>`_

Maintenance
-----------

* Add Windows CI.
  `<#17 https://github.com/mattsb42/pipx-in-pipx/pull/17>`_

1.0.0 -- 2019-05-26
===================

Now that I have CI set up for this on at least one platform,
I am comfortable saying that it is ready for use.

0.0.1b1 -- 2019-05-22
=====================

Bugfixes
--------

* Some installs in Linux were failing due to unable to find src files.
  All logic now in ``setup.py``.
* Removed unnecessary ``userpath verify`` step that was causing errors.
  `<#4 https://github.com/mattsb42/pipx-in-pipx/issues/4>`_
* Removed hard requirement for Python 3.6+.
  Leave that for ``pipx`` to worry about.

0.0.1b0 -- 2019-05-11
=====================

Initial MVP.
