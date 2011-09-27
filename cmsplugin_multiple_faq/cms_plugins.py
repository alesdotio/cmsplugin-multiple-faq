from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from models import FAQPlugin, FAQListPlugin

class CMSFAQPlugin(CMSPluginBase):
    model = FAQPlugin
    name = _("FAQ Plugin")
    render_template = "cmsplugin_multiple_faq/faqlist_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object':instance.faq_list,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSFAQPlugin)

class CMSFAQListPlugin(CMSPluginBase):
    model = FAQListPlugin
    name = _("FAQ List Plugin")
    render_template = "cmsplugin_multiple_faq/faqlist_list_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object_list':instance.faq_list.all(),
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSFAQListPlugin)