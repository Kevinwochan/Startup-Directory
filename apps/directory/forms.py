from django import forms
from directory.choices import *

# create an empty option as a placeholder
YEAR_CHOICES.append(('','Year'))
INDUSTRY_CHOICES.append(('','Industry'))
FUNDING_CHOICES.append(('','Stage'))
COMPANY_TYPE_CHOICES.append(('','Company Type'))

class filterForm(forms.Form):
    industry = forms.ChoiceField(choices=INDUSTRY_CHOICES,
        label="Industry",
        widget=forms.Select(attrs={'class': "form-control mr-2 mt-2",'placeholder':'Industry'}),
        required=False)

    stage = forms.ChoiceField(choices=FUNDING_CHOICES,
        label="Stage",
        widget=forms.Select(attrs={'class': "form-control mr-2 mt-2",'placeholder':'Stage'}),
        required=False)

    year = forms.ChoiceField(choices=YEAR_CHOICES,
        label="Year",
        widget=forms.Select(attrs={'class': "form-control mr-2 mt-2",'placeholder':'Year'}),
        required=False)

    company_type = forms.ChoiceField(choices=COMPANY_TYPE_CHOICES,
        label="Company Type",
        widget=forms.Select(attrs={'class': "form-control mr-2 mt-2",'placeholder':'Type'}),
        required=False)


'''
<form action="/filter" method="GET">
                {% csrf token %}
                <label for="industry">Industry</label>
                <select class="form-control">
                    <option value="" selected="selected">—</option>
                    {% for industry in options.industries %}
                    <option value="{{ industry }}">{{ industry }}</option>
                    {% endfor %}
                </select>
                <label for="stage">Stage</label>
                <select class="form-control">
                    <option value="" selected="selected">—</option>
                    {% for stage in options.stage %}
                    <option value="{{ stage }}">{{ stage }}</option>
                    {% endfor %}
                </select>
                <label for="founded_year">Year</label>
                <select class="form-control">
                    <option value="" selected="selected">—</option>
                    {% for year in options.year_founded %} <option value="{{ year }}">{{ year }}</option>
                    {% endfor %}
                </select>
                <input type="submit" class="btn btn-default" value="Submit">
                <input type="reset" class="btn btn-default" value="Clear Filters">
            </form>
'''
