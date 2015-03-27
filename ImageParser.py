import sys
from PIL import Image


header = """
-- MADE BY T. Dendale
-- WIDTH =  256
-- HEIGHT =  256

DEPTH =  """

header_2 = """;
WIDTH = 15;
ADDRESS_RADIX = HEX;
DATA_RADIX = HEX;
CONTENT
BEGIN\n"""

if (len(sys.argv) > 2):
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    im = Image.open(input_filename)

    f = open(output_filename, 'w');

    print("> Image size: ")
    print(im.size)
    print("")
    w = im.size[0]
    h = im.size[1]

    print("> Writing to file: "+ output_filename)

    f.write(header)
    f.write(str(w*h))
    f.write(header_2)

    index = 0;


    for x in range(0, w):
        for y in range(0, h):
            r = im.getpixel((x,y))[0] & 248
            g = im.getpixel((x,y))[1] & 248
            b = im.getpixel((x,y))[2] & 248

            total = r<<7 | g << 2 | b >> 3;


            hexa = hex(total)

            if (total == 0):
                hexa = "0x0000"

            f.write(hex(index)[2:] + ":\t"+hexa[2:]+";\n")

            index += 1

    f.write("END;")

    print(">>> DONE");

else:
    print("NEED MOAR INFO")