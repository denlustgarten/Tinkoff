def index():
    with open('templates/index.html') as templates:
        return templates.read()


def blog():
    with open('templates/blog.html') as templates:
        return templates.read()
