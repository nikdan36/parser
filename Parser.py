def reader(filename):

    regexp = r''
    with open (filename) as f:
        log = f.read()

        print(log)

if __name__ == '__main__':
    reader('log.log')