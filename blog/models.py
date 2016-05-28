from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	body = models.TextField()
	image = models.ImageField()
	link = models.URLField()
	posted = models.DateTimeField()
	category = models.ForeignKey('blog.Category')

	def __unicode__(self):
		return '%s' % self.title

	@models.permalink
	def get_absolute_url(self):
		return ('view_blog_post', (), {'slug': self.slug})
	
	def save(self, *args, **kwargs):
	        if not self.slug:
	            self.slug = slugify(self.title)
	        super(Article, self).save(*args, **kwargs)

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __unicode__(self):
		return '%s' % self.title

	@models.permalink
	def get_absolute_url(self):
		return ('view_blog_category', (), {'slug': self.slug})