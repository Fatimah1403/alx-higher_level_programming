#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    contents = dir(hidden_4)
    for content in contents:
        if content[:2] != "__":
            print(content)
