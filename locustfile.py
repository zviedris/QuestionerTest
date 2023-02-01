from locust import HttpUser, task, between
import random

class HelloWorldUser(HttpUser):
    wait_time = between(0.5, 2.5)
    
    @task
    def getStatistics(self):
        quest = random.randint(1,9)
        self.client.get("/statistics/question/" + str(quest))

    @task
    def saveResponse(self):
        arr=[]
        arr = [0 for i in range(10)]
        for x in range(0, 10):
            arr[x]=x+1

        arr2 = [0 for i in range(9)]
        for x in range(0, 9):
            arr2[x]=random.randint(0,5)       

        self.client.post("/response/save", json={
    "questionerId": 1,
    "Answers": [
        {"questionId": arr[0],
         "numericValue": arr2[0]
         },
         {"questionId": arr[1],
         "numericValue": arr2[1]
         },
         {"questionId": arr[2],
         "numericValue": arr2[2]
         },
         {"questionId": arr[3],
         "numericValue": arr2[3]
         },
         {"questionId": arr[4],
         "numericValue": arr2[4]
         },
         {"questionId": arr[5],
         "numericValue": arr2[5]
         },
         {"questionId": arr[6],
         "numericValue": arr2[6]
         },
         {"questionId": arr[7],
         "numericValue": arr2[7]
         },
         {"questionId": arr[8],
         "numericValue": arr2[8]
         },
         {"questionId": arr[9],
         "textValue": "test"
         }         
    ]
})