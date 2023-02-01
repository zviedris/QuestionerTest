# questioner tests

Precondition - install phyton and locust librarys

To run test - that populates questioner answers:
1)Edit locustfile.py - with id that is populated in your database
2)Run locust in terminal
3)http://localhost:8089/ - locust test enviorment - to set users and start test - use http://localhost:1323 - as your endpoint
4)Run tests while they populate DB with needed amount of data

Recommended user count - 300 with 50 users per second - gets around 100 requests per second - with bigger loads you need 8cpu pc
