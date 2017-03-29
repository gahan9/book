from django.core.urlresolvers import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML, Submit
from crispy_forms.layout import *
# from crispy_forms.bootstrap import PrependedText, FormActions, StrictButton, InlineField
from crispy_forms.bootstrap import *

add_book_helper = FormHelper()
# add_book_helper.form_tag = True
# add_book_helper.form_id = 'id-registerform'
add_book_helper.form_class = 'form-horizontal'
# add_book_helper.form_method = 'POST'
# add_book_helper.form_action = reverse_lazy('index')
# add_book_helper.form_show_labels = True
add_book_helper.label_class = 'col-md-6'
add_book_helper.field_class = 'col-md-6'
add_book_helper.layout = Layout(
    # Div(
    #     Div(
    #         Field('name', css_class='form-control'),
    #         css_class="col-md-3"
    #         ),
    #     css_class="form-row"
    #     ),
    Field('name', css_class='form-control col-md-3'),
    Field('image', css_class='form-control col-md-3'),
    Field('author', css_class='form-control'),
    Field('pub', css_class='form-control'),
    PrependedText('price', "₹", css_class='form-control', ),
    Field('published_date', css_class='form-control datepicker'),
    # Field('availability', css_class='form-control'),
    Div(FormActions(Submit('Save changes', value="Save", css_class="btn-primary align-right"),), css_class="container")

)
