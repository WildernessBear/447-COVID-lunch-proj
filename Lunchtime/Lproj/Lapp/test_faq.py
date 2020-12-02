from django.template.loader import render_to_string
from django.test import SimpleTestCase

class FAQTemplateTestCase(SimpleTestCase):
    def setUp(self):
        pass

    def test_faq_page(self):
        print("Running FAQTemplatesTestCase: test_faq_page")

        with self.assertTemplateUsed('Lapp/faq.html'):
            render_to_string('Lapp/faq.html', {})
