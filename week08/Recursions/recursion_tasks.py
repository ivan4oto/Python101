def deep_find_dfs(data, givenkey):
    for key, values in data.items():
        if givenkey in data.keys():
            return data[givenkey]
        elif type(values) == dict:
            item = deep_find_dfs(data[key], givenkey)
            if item is not None:
                return item

def deep_find_bfs(data, givenkey):
    tocheck = []
    for i in data:
        if i == givenkey:
            return data[givenkey]
        elif type(data[i]) == dict:
            tocheck.append(data[i])
    item = deep_find_bfs(tocheck[0], givenkey)
    if item is not None:
        return item

def deep_find_all_dfs(data, givenkey):
    found_keys = []
    for key, value in data.items():
        if key == givenkey:
            found_keys.append(value)

        elif type(value) == dict:
            results = deep_find_all_dfs(value, givenkey)
            for result in results:
                found_keys.append(result)

    return found_keys

def deep_update(data, givenkey, val):
    for key, value in data.items():
        if key == givenkey:
            data[key] = val
        elif type(value) == dict:
            deep_update(value, givenkey, val)
    return data



if __name__ == "__main__":
    pass
