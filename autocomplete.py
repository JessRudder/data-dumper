def extract(query):
  POTENTIAL_CHARS = "abcdefghijklmnopqrstuvwxyz"
  results = []

  for char in POTENTIAL_CHARS:
    initial_string = char
    res = query(current_string)

    if len(res) < 5:
      results.append(res)
    else:
      results.append(res)
      current_string = res[-1]
      print(current_string)

  # flatten the multidimensional list to 1D using list comprehension
  results = [j for i in results for j in i]

  return results

def main():
  """Runs your solution -- no need to update (except to maybe try out different databases)."""
  # Sample implementation of the autocomplete API
  database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
  query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
  assert extract(query) == database

main()