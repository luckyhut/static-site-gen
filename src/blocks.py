def markdown_to_blocks(markdown):
    strings = markdown.split("\n\n")
    result = []
    for string in strings:
        if string != '':
            result.append(string.strip())
    return result
