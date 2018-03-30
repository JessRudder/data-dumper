from string import ascii_lowercase

# Compare two strings and return the shortest string that is different between the two
# EX: key_term = application
#     comparison_term = applicant
# Should return => "applicat"
def shortest_difference(key_term, comparison_term):
  s = ""
  for idx, char in enumerate(key_term):
    if key_term[idx] == comparison_term[idx]:
      s += char
    else:
      s += char
      break
  return s

# Take in the current string and return the next string that should be used in the query
# Should increment the final letter by 1 until it reaches 'z', then it should step up
# One level and increment the next letter by 1.  For single character string that are
# at 'z' it should return None
# EX: "aaa", "axz", "a", "z"
#
# Should return => "aab", "ay", "b", None
def prep_next_string(current_string):
  current_string = current_string
  last_char = current_string[-1]
  next_char_pos = ascii_lowercase.find(last_char) + 1

  if current_string == "z":
    return None
  elif last_char == "z":
    return prep_next_string(current_string[:-1])
  else:
    return current_string[:-1] + ascii_lowercase[next_char_pos]

def extract(query):
  current_string = "a"
  result = []

  while current_string != None:
    res = query(current_string)

    if len(res) < 5:
      result.append(res)
      current_string = prep_next_string(current_string)
    else:
      result.append(res[0:4])
      current_string = shortest_difference(res[4], res[3])


  # flatten the multidimensional list to 1D using list comprehension
  result = [j for i in result for j in i]

  return result

def main():
  """Runs your solution -- no need to update (except to maybe try out different databases)."""
  # Sample implementation of the autocomplete API
  database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
  alt_database = ["aaa", "aab", "aac", "aad", "aae", "aaf", "aag", "aah", "aaz", "ab", "aba", "abb", "ac", "ad", "b", "bz", "c", "xx", "xy", "z"]
  query1 = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
  query2 = lambda prefix: [d for d in alt_database if d.startswith(prefix)][:5]

  assert extract(query1) == database
  assert extract(query2) == alt_database

main()
