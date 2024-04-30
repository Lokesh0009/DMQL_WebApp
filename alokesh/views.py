import pandas as pd
from django.shortcuts import render
from .utils import get_table_names  # Assuming this function is already defined
import psycopg2
from django.conf import settings

def table_names_view(request):
    """Renders a page showing selected table names from the database."""
    tables = get_table_names()

    selected_tables = [tables[i] for i in [10, 11, 12, 14, 15, 16]]
    return render(request, 'welcomepage.html', {'tables': selected_tables})

import pandas as pd
from django.shortcuts import render
import psycopg2
from django.conf import settings

import psycopg2

def table_data_view(request, table_name):
    """Renders a page showing data from a specific table."""

    # Establish a connection to the database
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    # Convert rows to a list of lists
    data = [list(row) for row in rows]

    if not data:
        return render(request, 'table_data.html', {'table_name': table_name, 'data': [], 'columns': []})

    # Render the data in an HTML template
    return render(request, 'table_data.html', {'table_name': table_name, 'data': data, 'columns': columns})


