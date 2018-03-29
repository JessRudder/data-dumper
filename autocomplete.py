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

def prep_next_string(current_string):
  take current string
  if one character, return next single character
  if multiple characters
    pop off last character
    if character is z
      call prep_next_string on everything but z
    else
      push on character thats one position further


def extract(query):
  result = []

  for char in ascii_lowercase:
    initial_string = char
    res = query(initial_string)

    if len(res) < 5:
      results.append(res)
    else:
      results.append(res)
      current_string = shortest_difference(res[4], res[3])
      print(current_string)

  # flatten the multidimensional list to 1D using list comprehension
  result = [j for i in result for j in i]

  return result

def main():
  """Runs your solution -- no need to update (except to maybe try out different databases)."""
  # Sample implementation of the autocomplete API
  database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
  alt_database = ["aaa", "aab", "aac", "aad", "aae", "aaf", "aag", "aah", "aaz", "ab", "aba", "abb", "ac", "ad", "b", "bz", "c", "xx", "xy", "z"]
  query = lambda prefix: [d for d in alt_database if d.startswith(prefix)][:5]
  assert extract(query) == alt_database

main()