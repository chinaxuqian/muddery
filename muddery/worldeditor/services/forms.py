
"""
World data forms.
"""

from wtforms import Form, validators, widgets, fields
from wtforms.fields import simple
from sqlalchemy import Integer, Float, String, Unicode, Text, UnicodeText, DateTime, Boolean
from django.conf import settings
from muddery.server.database.db_manager import DBManager
from muddery.worldeditor.dao.general_query_mapper import get_all_fields


def get_form(table_name):
    """
    Get a form of a table.
    """
    session_name = settings.WORLD_DATA_APP
    model = DBManager.inst().get_model(session_name, table_name)
    model_fields = get_all_fields(table_name)

    cls = Form

    # Add default form fields according to the field type.
    for model_field in model_fields:
        model_column = getattr(model, model_field)
        form_column_type = None
        if model_field == "id":
            form_column_type = fields.HiddenField
        elif type(model_column.type) == Integer:
            form_column_type = fields.DecimalField
        elif type(model_column.type) == Float:
            form_column_type = fields.FloatField
        elif type(model_column.type) == String or type(model_column.type) == Unicode:
            form_column_type = fields.StringField
        elif type(model_column.type) == Text or type(model_column.type) == UnicodeText:
            form_column_type = fields.TextAreaField
        elif type(model_column.type) == DateTime:
            form_column_type = fields.DateTimeField
        elif type(model_column.type) == Boolean:
            form_column_type = fields.BooleanField
        else:
            # default input field
            form_column_type = fields.StringField

        setattr(cls, model_field, form_column_type())

    return cls
