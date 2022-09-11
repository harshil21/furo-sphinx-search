furo-sphinx-search - Search as you type for Read the Docs
=========================================================

![image](https://user-images.githubusercontent.com/37377066/189539883-f3b24751-8447-42a5-9d30-757183101234.png)


This repository is a fork of [readthedocs-sphinx-search](https://github.com/readthedocs/readthedocs-sphinx-search), and is currently modded for use in [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

Modded features
---------------

- Made the theme consistent with Furo. It works with both light and dark mode.
- The theme is now more "material", with rounded corners and cards as results, along with tiny fixes.
- Included the ability to perform an advanced search - Search by attributes, class, methods,
  parameters (requires [sphinx-paramlinks](https://github.com/sqlalchemyorg/sphinx-paramlinks), if
  you don't have this, the search filter for that just won't have any effect.),
  and general documentation.
- The `rtd_search` parameter was removed, so no more pushing to history and a better UX.

Note that Advanced Search will work for pure python documentation. If you support for other domains
than the python one, feel free to open an issue or a PR.

Installation
------------

This package is not available via pip, so you'll have to install it manually:

``` bash
pip install git+https://github.com/harshil21/furo-sphinx-search@main
```

or in your ``requirements.txt``:

``` code
git+https://github.com/harshil21/furo-sphinx-search@main
```

The rest of the configuration process remains the same as the original package. Please refer to the
[original documentation](https://readthedocs-sphinx-search.readthedocs.io/).


Credits
-------

- [readthedocs-sphinx-search](https://github.com/readthedocs/readthedocs-sphinx-search) for the
  original code.

License
-------

This project is licensed under the terms of the MIT license (required to be same as upstream license).

