from get_repos import USER, HEADERS, get_all_repos
import json

repos = get_all_repos(USER, HEADERS)



def results(repos):
    #If repositories are found, proceed with calculating the percentage
    if repos:
        #Add up the size of each language in all repositories
        languages_size = {}

        for repo in repos:
            languages = repo["languages"]["edges"]
            for language in languages:
                language_name = language["node"]["name"]
                language_size = language["size"]
                if language_name not in languages_size:
                    languages_size[language_name] = language_size
                else:
                    languages_size[language_name] += language_size

        # Calculate the percentage of usage for each language
        total_size = sum(languages_size.values())
        languages_percentage = {}

        for language, size in languages_size.items():
            languages_percentage[language] = (size / total_size) * 100

        # Print the percentage of usage for each language
        print(json.dumps(languages_percentage, indent=2))
        return(languages_percentage)

    else:
        print("Not repositories")

res = results(repos)