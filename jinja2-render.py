import codecs
import csv
import glob
import jinja2

template_file =  "template.html"

def read_data(f):
    ''' Reading data from the csv file
    Args:
        f: name of the file
    '''
    with codecs.open(f, "rU", "utf-8") as cf:
        reader = csv.DictReader(cf)
        return list(reader)

def render_template(data):
    ''' Rendering the data into the template
    Args:
        data: data to use in the template
    '''
    f = open(template_file, "r")
    c = f.read()
    template = jinja2.Template(c)
    with open("books.html", "wb") as html:
        html.write(template.render(**data))
 
def main():
    data = {}
    for f in glob.glob("*.csv"):
        data[f[:-4]] = read_data(f)
    render_template(data)
 
if __name__ == "__main__":
    main()
