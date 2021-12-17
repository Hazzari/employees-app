import re

from odmantic import query

from app.model.employee import Employee


def serializes_search_params(params: dict) -> list:
    """ Формирует из параметров request список поискового запроса
    """
    search_params = []

    if params.get('name'):
        search_params.append(
            query.match(Employee.name, re.compile(f"{params['name']}")))

    if params.get('email'):
        search_params.append(
            query.match(Employee.email, re.compile(f"{params['email']}")))

    if params.get('gender'):
        search_params.append(
            query.match(Employee.gender, re.compile(f"{params['gender']}")))

    if params.get('company'):
        search_params.append(query.match(Employee.company, re.compile(
            f"{params['company']}")))

    if params.get('age_min'):
        search_params.append(Employee.age >= params.get('age_min'))

    if params.get('age_max'):
        search_params.append(Employee.age <= params.get('age_max'))

    if params.get('salary_min'):
        search_params.append(Employee.salary >= params.get('salary_min'))

    if params.get('salary_max'):
        search_params.append(Employee.salary <= params.get('salary_max'))
    return search_params
