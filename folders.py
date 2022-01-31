import os


def path():
  pass


def dictionary(way, a={}):
    for filename in os.listdir(way):
        if os.path.isdir(way + '\\' + filename):
            dictionary(way + '\\' + filename)
        else:
            a.update({way + '\\' + filename: os.path.getsize(way + '\\' + filename)})
    return a
  


def duplicate():
  pass


def print_duplicate():
  pass


if __name__ == '__main__':
