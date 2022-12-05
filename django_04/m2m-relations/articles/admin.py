from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        is_valid = 0
        for form in self.forms:
            if form.cleaned_data:
                is_valid += form.cleaned_data['is_main']
        if not is_valid:
            raise ValidationError('Укажите основной раздел')
        elif is_valid > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet
    ordering = ['-is_main']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    pass
