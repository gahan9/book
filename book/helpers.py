from django.core.urlresolvers import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML, Submit
from crispy_forms.layout import *
# from crispy_forms.bootstrap import PrependedText, FormActions, StrictButton, InlineField
from crispy_forms.bootstrap import *

add_book_helper = FormHelper()
add_book_helper.form_tag = True
# add_book_helper.form_id = 'id-registerform'
add_book_helper.form_class = 'form-horizontal'
add_book_helper.form_method = 'POST'
# add_book_helper.form_action = '/'
add_book_helper.form_show_labels = True   # default = True
add_book_helper.label_class = 'col-lg-2'
add_book_helper.field_class = 'col-lg-4'
add_book_helper.layout = Layout(
    Field('name', css_class='form-control'),
    Field('image', css_class='form-control'),
    Field('author', css_class='form-control'),
    Field('pub', css_class='form-control'),
    PrependedText('price', "₹", css_class='form-control', ),
    Field('published_date', css_class='form-control'),
    Div(FormActions(Submit('Save changes', value="Save", css_class="btn-primary align-right"),), css_class="container")
)


search_helper = FormHelper()
search_helper.form_tag = True
# search_helper.form_id = 'id-registerform'
search_helper.form_class = 'form-inline'
search_helper.form_method = 'POST'
# search_helper.form_action = '/'
search_helper.form_show_labels = True   # default = True
# search_helper.label_class = 'col-lg-2'
# search_helper.field_class = 'col-lg-6'
search_helper.layout = Layout(
    Row(
        InlineField('name', css_class='form-control'),
        InlineField('author', css_class='form-control'),
        InlineField('pub', css_class='form-control'),
        FormActions(Submit('Save changes', value="Search", css_class="btn-info align-right"),),
        css_class="text-center"
    )
)

