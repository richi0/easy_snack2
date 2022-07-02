from django.contrib import admin
from .models import Article, Paragraph, Image, City, Country
from forms.models import Comment


class ParagraphInline(admin.StackedInline):
    model = Paragraph
    extra = 0


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline, ImageInline, CommentInline]
    list_display = ("title", "publish_on")
    ordering = ("-publish_on",)
    exclude = ('sent_newsletter',)

    def save_model(self, request, obj, form, change):
        if obj.google_map:
            obj.google_map = obj.google_map.replace('width="600"', 'width="100%"')
            obj.google_map = obj.google_map.replace('height="450"', 'height="100%"')
        super().save_model(request, obj, form, change)


class CityAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)