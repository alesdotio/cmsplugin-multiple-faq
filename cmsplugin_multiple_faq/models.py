from django.db import models
from cms.models import CMSPlugin

class FAQList(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return u"%s" % self.title

class FAQEntry(models.Model):
    faq_list = models.ForeignKey(FAQList, related_name="faq_entries")
    question = models.CharField(max_length=128)
    answer = models.TextField()

    def __unicode__(self):
        return u"%s" % self.question

class FAQPlugin(CMSPlugin):
    faq_list = models.ForeignKey(FAQList)

    def copy_relations(self, oldinstance):
        self.faq_list = oldinstance.faq_list