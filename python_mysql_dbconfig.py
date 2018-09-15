from ConfigParser import ConfigParser as cp


def read_db_config(filename='config.ini', section='mysql'):
  """ Read database config file and return a dictionary object.
  :param filename: name of the config file
  :param section: section of database configuration
  :return: a dictionary of database parameters
  """
  # Create parser and read ini config file
  parser = cp()
  parser.read(filename)

  # get section, default to mysql
  db = {}
  if parser.has_section(section):
    items = parser.items(section)
    for item in items:
      db[item[0]] = item[1]
  else:
    raise Exception('{0} not found in the {1} file'.format(section, filename))

  return db
