from django.contrib import admin
from .models import Post, Tag, Author

class PostInline(admin.TabularInline):
    model = Post
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")
    inlines = [PostInline]



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )

    search_fields = (
        "title",
        "content",
    )

    list_filter = (
        "author",
    )
    filter_horizontal = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)