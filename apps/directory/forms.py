from django import forms

class filterForm(forms.Form):
    industry = forms.CharField(label='industry')
    stage = forms.CharField(label='stage')
    year = forms.CharField(label='year_founded')


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
                    {% for year in options.year_founded %}
                    <option value="{{ year }}">{{ year }}</option>
                    {% endfor %}
                </select>
                <input type="submit" class="btn btn-default" value="Submit">
                <input type="reset" class="btn btn-default" value="Clear Filters">
            </form>

