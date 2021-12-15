import json

import pytest


# в зависимостях фреймворка
@pytest.mark.dependency()
def test_count_employees(test_app, test_data, response_data):
    """ Test the number of employee in the database
    """
    response = test_app.get('/api/employee/count/')
    assert response.status_code == 200
    assert int(response.text) >= 0
    response_data.emp_count = int(response.text)


@pytest.mark.dependency(depends=["test_count_employees"])
def test_create_employee(test_app, response_data, test_data):
    """ Create employee
    """
    response = test_app.post('/api/employee/', json.dumps(test_data))
    assert response.status_code == 201
    response_dict = json.loads(response.text)
    assert response_dict['name'] == test_data['name']

    assert int(test_app.get(
        '/api/employee/count/').text) == response_data.emp_count + 1
    response_data.req = response_dict
    response_data.emp_count += 1


@pytest.mark.dependency(depends=["test_create_employee"])
def test_get_employee(test_app, test_data, response_data):
    """ Get employee by id
    """

    _id = response_data.req.get('id')
    response = test_app.get(f'/api/employee/{_id}')

    assert response.status_code == 200
    assert json.loads(response.text) == response_data.req


@pytest.mark.dependency(depends=["test_create_employee"])
def test_update_employee(test_app, test_data, response_data):
    """ Update employee"""
    response_without_changes = test_app.put(
        f'/api/employee/',
        data=response_data.req,
    )
    assert response_without_changes.status_code == 422, f'данные не должны ' \
                                                        f'изменяться'

    response_data.req['name'] = 'New Alex'
    response_data.req['email'] = f'NewEmail@gmail.com'
    response_data.req['age'] = 55
    response_data.req['salary'] = 3456
    response_data.req['id'] = response_data.req['id']

    response = test_app.put(
        f'/api/employee/',
        data=json.dumps(response_data.req),
    )

    assert response.status_code == 200
    assert json.loads(response.text) == response_data.req
    assert response_data.emp_count == int(test_app.get(
        '/api/employee/count/').text)


@pytest.mark.dependency(depends=["test_update_employee"])
def test_delete_employee(test_app, test_data, response_data):
    """ Delete employee"""
    id = response_data.req['id']

    response = test_app.delete('/api/employee/', params={'id': id}, )
    response_404 = test_app.delete(
        '/api/employee/',
        params={'id': '000000000000000000000000'},
    )

    assert response_404.status_code == 404, 'Пользователя с таким id нет'

    assert response.status_code == 200
    count_employees = int(test_app.get('/api/employee/count/').text)
    assert count_employees == response_data.emp_count - 1, \
        f'После удаления пользователей в базе должно быть на одного меньше'
