#newlineify
with open("in.txt", "r", encoding="utf-8") as f:
    file = f.readlines()
    out = ""
    for line in file:
        line = line.strip(" ")
        if "<br>\n" in line:
            line = line.replace("\n", "")
        out += line
    
output = open("out.txt", "w")
output.write(out)
output.close()
