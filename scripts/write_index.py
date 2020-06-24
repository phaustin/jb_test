import jinja2
from collections import namedtuple

template="""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Book list</title>
</head>
<body>
     <div class="container">
      <p>Books built {{book_dir}}</p>
      <ul>
        {% for item in book_list %}
        <li><a href="{{item.url}}">{{item.descrip}}</a></li>
        {% endfor %}
      </ul>
    </div>
</body>
</html>
"""
link_tuple = namedtuple('link',["descrip","url"])

def make_page(book_dir, link_list):
    j2_template = jinja2.Template(template)
    str_out = j2_template.render(book_dir=book_dir, book_list=link_list)
    return str_out

if __ name__ == "__main__":
    link1 = link_tuple(descrip = "a", url="1")
    link2 = link_tuple(descrip = "b", url="2")
    my_list = [link1, link2]
    str_out = make_page("book dir",my_list)
    with open('index.html','w',encoding="utf8") as outfile:
        outfile.write(str_out)
