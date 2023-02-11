import requests


class GitHub:

    def get_user(self, user_name):
        response = requests.get(f"https://api.github.com/users/{user_name}")
        return response.json()

    def search_repo(self, repo_name):
        response = requests.get(
            "https://api.github.com/search/repositories",
            params={'q': repo_name}
        )
        return response.json()
