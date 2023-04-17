import requests
import json

# Replace 'your_access_token' with your personal GitHub access token
#Make sure the token has the 'repo' permission to access private repositories
#You can obtain one from https://github.com/settings/tokens"

TOKEN = "YOUR TOKEN"
HEADERS = {
    "Authorization": f"bearer {TOKEN}",
    "Content-Type": "application/json",
}

# Replace 'gabotov' with your user GitHub
USER = "gabotov"

#GraphQL query to get all the user's repositories (public and private)
QUERY = """
query($user: String!, $cursor: String) {
  user(login: $user) {
    repositories(first: 100, after: $cursor, isFork: false, ownerAffiliations: OWNER) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        languages(first: 100) {
          edges {
            size
            node {
              name
            }
          }
        }
      }
    }
  }
}
"""

def get_all_repos(user, headers):
    repos = []
    has_next_page = True
    cursor = None

    while has_next_page:
        variables = {
            "user": user,
            "cursor": cursor
        }
        response = requests.post(
            "https://api.github.com/graphql",
            headers=headers,
            json={"query": QUERY, "variables": json.dumps(variables)}
        )
        data = response.json()

        if "errors" in data:
            print("Error en la respuesta de la API:")
            print(json.dumps(data["errors"], indent=2))
            return repos

        user_data = data["data"]["user"]
        repositories_data = user_data["repositories"]
        has_next_page = repositories_data["pageInfo"]["hasNextPage"]
        cursor = repositories_data["pageInfo"]["endCursor"]
        repos.extend(repositories_data["nodes"])

    return repos
