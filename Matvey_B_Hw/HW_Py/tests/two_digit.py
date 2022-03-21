import re

# reg = re.compile("[^a-zA-Z ]+")

filename = "readpls.txt"
n = 0
with open(filename, "r") as fh:
    for line in fh:
        # print(str(n) + ')' + line)
        n += 1
        # x = re.findall("[0-9][0-9]", line)
        x = re.findall('\d+', line)
        if (x):
            for i in x:
                if len(i) == 2:
                    print('{n}) {i}'.format(n=n, i=i))

