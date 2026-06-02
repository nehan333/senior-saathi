import json

def get_schemes():

    with open("backend/schemes.json") as f:

        schemes = json.load(f)

    return schemes


def search_scheme(q):

    with open("backend/schemes.json") as f:

        schemes = json.load(f)

    results = []

    for scheme in schemes:

        if q.lower() in scheme["name"].lower():

            results.append(scheme)

    return results
