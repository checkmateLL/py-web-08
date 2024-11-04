from models import Author, Quote
from mongoengine import connect
import configparser

config = configparser.ConfigParser()
config.read('part-one/config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

def search_quotes():
    while True:
        command = input("Enter command (name: author_name, tag: tag_name, tags: tag1,tag2, or exit): ").strip()
        
        if command.lower() == 'exit':
            print("Goodbye!")
            break
            
        try:
            command_type, value = command.split(':', 1)
            command_type = command_type.strip().lower()
            value = value.strip()

            if command_type == 'name':
                author = Author.objects(fullname=value).first()
                if author:
                    quotes = Quote.objects(author=author)
                    for quote in quotes:
                        print(f"\nAuthor: {quote.author.fullname}\nQuote: {quote.quote}\nTags: {', '.join(quote.tags)}\n")
                else:
                    print(f"Author {value} not found")

            elif command_type == 'tag':
                quotes = Quote.objects(tags=value)
                for quote in quotes:
                    print(f"\nAuthor: {quote.author.fullname}\nQuote: {quote.quote}\nTags: {', '.join(quote.tags)}\n")

            elif command_type == 'tags':
                tags = value.split(',')
                quotes = Quote.objects(tags__in=tags)
                for quote in quotes:
                    print(f"\nAuthor: {quote.author.fullname}\nQuote: {quote.quote}\nTags: {', '.join(quote.tags)}\n")
            
            else:
                print("Unknown command. Available commands: name, tag, tags, exit")
        
        except ValueError:
            print("Invalid command format. Use format 'command: value'")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    search_quotes()