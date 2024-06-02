class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title  # Private attribute to hold the title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        author._articles.append(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title  # Getter method for the title attribute

class Author:
    def __init__(self, name):
        self._set_name(name)
        self._articles = []

    def _set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a string and longer than 0 characters.")

    @property
    def name(self):
        return self._name

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError(
                "Name must be a string between 2 and 16 characters."
            )

    name = property(get_name, set_name)

    def get_category(self):
        return self._category

    def set_category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError(
                "Category must be a string and longer than 0 characters."
            )

    category = property(get_category, set_category)

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_articles_count = {article.author: 0 for article in self._articles}
        for article in self._articles:
            author_articles_count[article.author] += 1
        return [author for author, count in author_articles_count.items() if count > 2] or None


author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")

magazine_1 = Magazine("Tech Today", "Technology")
magazine_2 = Magazine("Health Weekly", "Health")

article_1 = author_1.add_article(magazine_1, "How to wear a tutu with style")
article_2 = author_1.add_article(magazine_2, "Dating life in NYC")
