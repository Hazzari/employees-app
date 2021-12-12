from odmantic import Model


class Employee(Model):
    name: str
    email: str
    age: int
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int
