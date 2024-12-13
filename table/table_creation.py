import csv

my_html = """<table class="">
    <tbody class="">
        <tr class="">
            <th class="">
                <p>
                    Name
                </p>
            </th>
            <th class="">
                <p>
                    Title/Department
                </p>
            </th>
        </tr>"""

def add_header(head=None, list=[]):
    """can either pass head (for adding one header at a time) or list, an array of headers."""
    row = '<tr class="">'
    if len(list) > 0:
        for item in list:
            print("ITEM IN LIST", item)
            row += '<th class="">'
            row += f"<p>{item}</p></th>"
        row += '</tr>'
    else:
        row += '<th class="">'
        row += f"<p>{head}</p></th></tr>"
    return row

def format_name(name):
    comma = name.index(',')
    last = name[:comma]
    first = name[comma+2:].strip()
    return f"{first} {last}"

def old_make_row(arr):
    #this is old version of new function in other file lol 
    r = ""
    r += f"""<tr class="">
            <td class="">
                <p>{format_name(arr[0])}</p></td>"""
    r += f"""<td class="">
                 <p>{arr[1].strip()}, {arr[2].strip()}</p></td></tr>"""
    return r

def make_row(array):
    """array: list of items, one for each td."""
    output = ""
    output += '<tr class="">'
    for item in array:
        output += f'<td class=""><p>{item}</p></td>'
    output += '</tr>'
    return output

if __name__ == "__main__":
    with open('test.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            my_html += make_row(row)
        my_html += "</tbody></table>"

    f = open("table.txt", "w")
    f.write(my_html)
    f.close()

