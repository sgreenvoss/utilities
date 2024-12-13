import table_creation as t
import re

# this is for converting from a grid to a responsive table. specific html classes redacted
# better version would use beautiful soup but i can do that later

f = open("in2.txt", "r")

# use to match what people have used for their fake headers
HEAD_MATCH = "<strong>(.*?)<\/strong>"


def parse_from_grid(grid_num, file):
    """grid_num: number of columns in the grid
    file: file pointer"""

    out = """<table class=""><tbody class="table__body">"""
    in_count = 0
    current_row = []
    heads = []

    for line in file:
        line = line.strip()
        # this is bad and assumes that peoples' fake headers will be denoted by <strong>
        # TODO: fix lol
        if "<strong>" in line[0:10]:
            match = re.search(HEAD_MATCH, line)
            if match:
                heads.append(match.group(1))
                if len(heads) == grid_num:
                    out += t.add_header(0,heads)
                    heads.clear()

        # i only want content - input file has content on each newline
        elif ('<a' in line) or not re.search("div|</?p>|h[1-6]", line) and line[0] != '&nbsp;':
        
            current_row.append(line)
            in_count = (in_count + 1) % grid_num
      
            if in_count == 0:
                out += t.make_row(current_row)
                current_row.clear()
    
    out += "</tbody></table>"
    return out


my_html = parse_from_grid(6, f)
output = open("out2.txt", "w")
output.write(my_html)
output.close()
f.close()
