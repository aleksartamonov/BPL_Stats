from parser.parser import parse_document as parse_document

if __name__ == "__main__":
    stat_file = "calendar.html"
    print "main block"
    res = parse_document(stat_file)

    output = open("output.dat", "w")
    for r in res:
        output.write(repr(r)+'\n')
    output.close()