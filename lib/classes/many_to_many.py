class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all_articles.append(self)
        author.add_article(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("name must be a string between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("category must be a non-empty string")
        self._category = new_category

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
        return [author for author, count in author_articles_count.items() if count > 2]

author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")

magazine_1 = Magazine("Tech Today", "Technology")
magazine_2 = Magazine("Health Weekly", "Health")


article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
article_2 = Article(author_1, magazine_2, "Dating life in NYC")


print(hasattr(author_1, "name"))  # True
print(len(author_1.name) > 0)  # True
print(hasattr(author_2, "name"))  # True
print(len(author_2.name) > 0)  # True