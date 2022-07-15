from datetime import date
from django.shortcuts import get_object_or_404, render

from blog.models import Post

all_posts = [
    {"slug": "hike-in-the-mountains",
     "image": "mountains.jpg",
     "author": "Cole",
     "date": date(2022, 4, 7),
     "title": "Mountain Hiking",
     "excerpt": "Hiking in the mountains is great for exercise and meditation.",
     "content": """ Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Iste dicta incidunt harum! Assumenda at, minus harum officiis nulla ipsum 
    laboriosam possimus nesciunt eligendi sed alias, excepturi, illo magni repudiandae vel?

    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Iste dicta incidunt harum! Assumenda at, minus harum officiis nulla ipsum 
    laboriosam possimus nesciunt eligendi sed alias, excepturi, illo magni repudiandae vel?

    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Iste dicta incidunt harum! Assumenda at, minus harum officiis nulla ipsum 
    laboriosam possimus nesciunt eligendi sed alias, excepturi, illo magni repudiandae vel?

    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Iste dicta incidunt harum! Assumenda at, minus harum officiis nulla ipsum 
    laboriosam possimus nesciunt eligendi sed alias, excepturi, illo magni repudiandae vel?
    """
     },
    {"slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
     },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def specific_post(request, post):
    identified_post = get_object_or_404(Post, slug=post)
    return render(request, "blog/specific-post.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
