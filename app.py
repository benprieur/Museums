import requests

url = 'http://apicollections.parismusees.paris.fr/graphql'
headers={'auth-token': '1515a207-3e75-4189-976d-2853914fe9c8', 'Content-Type': 'application/json'}

query = """
{
  nodeQuery(filter: {conditions: [
    {field: "type", value: "oeuvre"}
    {field: "field_oeuvre_auteurs.entity.field_auteur_auteur.entity.field_lref_adlib", value: "42468"}
  ]}) {
    count
    entities {
      ... on NodeOeuvre {
        title
        nid
      }
    }
  }
}
"""

response = requests.post(url, json={'query': query}, headers=headers)
print (response)

if response.status_code == 200:
    print(response.json())
else:
    raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))