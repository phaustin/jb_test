#!/bin/bash -v
$PYTHON  -m pip install https://clouds.eos.ubc.ca/~phil/docs/wheels/jupyter_book-0.7.1.dev0-py3-none-any.whl --upgrade --no-deps
$PYTHON  -m pip install https://clouds.eos.ubc.ca/~phil/docs/wheels/jupyter_cache-0.2.2-py3-none-any.whl --upgrade --no-deps
$PYTHON  -m pip install https://clouds.eos.ubc.ca/~phil/docs/wheels/myst_nb-0.8.3-py3-none-any.whl --upgrade --no-deps
ls -ltd $PREFIX/lib/python3.7/site-packages/jupyter_book/*
