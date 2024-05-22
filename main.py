from jinja2 import Environment, FileSystemLoader
import markdown2
from lijsten import Lijsten
from kiessysteem import stemsimulatie

stemsimulatie()

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("markdown_template.md.j2")
rendered_content = template.render(
    partij_1=Lijsten[0].naam,
    partij_2=Lijsten[1].naam,
    partij_3=Lijsten[2].naam,
    partij_4=Lijsten[3].naam,
    partij_5=Lijsten[4].naam,
)
html_content = markdown2.markdown(rendered_content)
with open("index.html", "w") as file:
    file.write(html_content)
