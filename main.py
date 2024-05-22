from jinja2 import Environment, FileSystemLoader
import markdown2
from lijsten import Lijsten
from kiessysteem import (
    kandidatenlijst1,
    kandidatenlijst2,
    kandidatenlijst3,
    kandidatenlijst4,
    kandidatenlijst5,
)


env = Environment(loader=FileSystemLoader("."))
template = env.get_template("markdown_template.md.j2")
rendered_content = template.render(
    partij_1=Lijsten[0].naam,
    partij_2=Lijsten[1].naam,
    partij_3=Lijsten[2].naam,
    partij_4=Lijsten[3].naam,
    partij_5=Lijsten[4].naam,
    stemmen_partij_1=Lijsten[0].stemmen,
    stemmen_partij_2=Lijsten[1].stemmen,
    stemmen_partij_3=Lijsten[2].stemmen,
    stemmen_partij_4=Lijsten[3].stemmen,
    stemmen_partij_5=Lijsten[4].stemmen,
    kandidaten1=zip(Lijsten[0].kandidaten, kandidatenlijst1),
    kandidaten2=zip(Lijsten[1].kandidaten, kandidatenlijst2),
    kandidaten3=zip(Lijsten[2].kandidaten, kandidatenlijst3),
    kandidaten4=zip(Lijsten[3].kandidaten, kandidatenlijst4),
    kandidaten5=zip(Lijsten[4].kandidaten, kandidatenlijst5),
)
html_content = markdown2.markdown(rendered_content)
with open("index.html", "w") as file:
    file.write(html_content)
print("Website klaar om online te zetten")
