import requests


class GitHub:

    def get_user(self, username):
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        return response.json()

    def search_repo(self, name):
        response = requests.get(
            "https://api.github.com/search/repositories",
            params={'q': name}
        )
        return response.json()
