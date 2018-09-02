from flask import Flask, render_template
from pycode.services.query_models import company_info as comp_i, campaign_info as camp_i

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/companies')
def companies():
    companies_list = comp_i.get_company_all()
    return render_template('companies.html', companies = companies_list)


@app.route('/companies/<name>')
def companiesByName(name):
    companies_list = comp_i.get_company_name(name)
    return render_template('companies.html', companies = companies_list)


@app.route('/companies/industry/<name>')
def companiesByIndustry(name):
    companies_list = comp_i.get_company_industry(name)
    return render_template('companies.html', companies = companies_list)


@app.route('/campaign')
def campaign():
    campaign_list = camp_i.get_campaign_count_by_target()
    return render_template('companies.html', campaign = campaign_list)


if __name__ == '__main__':
    app.run()
