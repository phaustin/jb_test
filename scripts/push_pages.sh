#! /bin/bash
mkdir -p _build/multi_level
cp -a multi_level/toc/_build/* _build/multi_level/.
ghp-import  --no-jekyll -p _build
