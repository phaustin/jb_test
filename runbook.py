# python cleanup.py books/toc_urllink
# python runbook.py build --toc books/toc_urllink/_toc_urllink.yml books/toc_urllink
# python cleanup.py books/toc_withheaders
# python runbook.py build --toc books/toc_withheaders/_toc_withheaders.yml books/toc_withheaders

from jupyter_book.commands import main

if __name__ == "__main__":
    main()
