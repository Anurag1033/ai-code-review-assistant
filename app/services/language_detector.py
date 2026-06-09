def detect_language(filename: str):

    filename = filename.lower()

    if filename.endswith(".py"):
        return "Python"

    elif filename.endswith(".java"):
        return "Java"

    elif filename.endswith(".js"):
        return "JavaScript"

    elif filename.endswith(".cpp"):
        return "C++"

    elif filename.endswith(".cs"):
        return "C#"

    else:
        return "Unknown"