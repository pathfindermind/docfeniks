from django import template
from feedback_app.models import ContactForm


register = template.Library()

@register.inclusion_tag('feedback_app/form.html', takes_context=True)
def showfeedback(context):
	form = ContactForm()
	return {"form": form}
