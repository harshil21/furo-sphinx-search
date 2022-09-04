furo-sphinx-search - Search as you type for Read the Docs
=========================================================

https://user-images.githubusercontent.com/37377066/188320224-d6292179-1ac7-4ebd-88ff-5d313df7722f.mp4


This repository is a fork of [readthedocs-sphinx-search](https://github.com/readthedocs/readthedocs-sphinx-search), and is currently modded for use in [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

Modded features
---------------

- Made the theme consistent with Furo. It works with both light and dark mode.
- The theme is now more "material", with rounded corners and cards as results, along with tiny fixes.
- Included the ability to perform an advanced search - Search by attributes, class, methods, parameters (requires [sphinx-paramlinks](https://github.com/sqlalchemyorg/sphinx-paramlinks)), and general documentation.

Note that Advanced Search will work for pure python documentation. Additionally, the search function is slightly [modified](https://github.com/harshil21/furo-sphinx-search/blob/main/sphinx_search/static/js/rtd_sphinx_search.js#L490-L494) for PTB so if you want this feature you'll have to make a couple of changes.

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

The rest of the configuration process remains the same as the original package. Please refer to the [original documentation](https://readthedocs-sphinx-search.readthedocs.io/).
