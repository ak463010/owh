from django import template
from store.models.customer import Customer

register = template.Library()


@register.filter(name='id_to_name')
def id_to_name(customer_id):
    try:
        return Customer.objects.get(id=customer_id).name
    except:
        return None
