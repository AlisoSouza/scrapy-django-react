from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from quotes.models import Quote, Author, Tag


class CrawlerPipeline:

    # def process_item(self, item, spider):
    #     try:
    #         # verifica se a quote ja existe
    #         quote = Quote.objects.get(quote=item['quote'])
    #         print("Quote already exists")
    #         return item
    #     except:
    #         Quote.objects.create(quote=item['quote'],
    #                              author=item['author'], tag=item['tag'])

    #         return item
    def process_item(self, item, spider):
        # verifica se o autor ja esta cadastrado no banco
        if not Author.objects.filter(author=item['author']).exists():
            # cadastra o autor no banco
            author = Author.objects.create(author=item['author'])
        else:
            # busca autor no banco
            author = Author.objects.get(author=item['author'])
        tags = []
        for tag in item['tags']:
            # verifica se a tag existe e adiciona numa lista caso nao exista ela sera criada
            if not Tag.objects.filter(tag=tag).exists():
                tag = Tag.objects.create(tag=tag)
                tags.append(tag)
            else:
                tag = Tag.objects.get(tag=tag)
                tags.append(tag)

        # se a quote noa existe ele cria e adiciona o autor como foreign key
        if not Quote.objects.filter(quote=item['quote']).exists():
            quote = Quote.objects.create(quote=item['quote'], author=author)
            quote.tags.add(*tags)
            quote.save()

        else:
            print("Quote already exists")
        return item
