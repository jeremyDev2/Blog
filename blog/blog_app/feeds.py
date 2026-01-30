import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post

# XML post's, for services
class LatestPostsFeed(Feed):

    title = "My Blog"
    # lazy version of reverse() for classes(does not build url, before class innitialize)
    link = reverse_lazy("blog:post_list")
    description = "New post of my blog" 
    
    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish

