from models import Author, Quote
import connect
import json


def load_json(file):
    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def add_authors(file):
    data = load_json(file)

    for author in data:
        add_author = Author(
            fullname=author["fullname"],
            born_date=author["born_date"],
            born_location=author["born_location"],
            description=author["description"],
        )
        add_author.save()


def add_quotes(file):
    data = load_json(file)

    for quote in data:
        add_quote = Quote(
            tags=quote["tags"],
            author=[
                author.id
                for author in Author.objects()
                if author.fullname == quote["author"]
            ],
            quote=quote["quote"],
        )
        add_quote.save()


if __name__ == "__main__":
    add_authors("authors.json")
    add_quotes("quotes.json")