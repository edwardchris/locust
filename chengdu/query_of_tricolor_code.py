from locust import HttpUser, TaskSet, task


class Query_Of_Tricolor_Code(TaskSet):

    def on_start(self):  # 当模拟用户开始执行TaskSet类的时候，on_start方法会被调用
        pass

    @task(1)
    # 个人健康登记信息接入（新增）
    # 个人健康登记信息接入
    def post_jkdj(self):
        global loginUrl, header
        loginUrl_list = ["/gateway/api/1/wllz/jkdj", "/gateway/api/1/wllz/jkdj/xb"]
        for loginUrl in loginUrl_list:
            header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        body_list = [{"source": "0",
                      "person_name": "string",
                      "phone": "string",
                      "card_type": "0",
                      "card_no": "string",
                      "house_type": "0",
                      "recordAddress": "string",
                      "is_cd": "0",
                      "is_reback": "0",
                      "reback_time": "2020-02-25 00:00:00",
                      "reback_xzqhdm": "string",
                      "reback_plan": "string",
                      "reback_plan_xzqhdm": "string",
                      "is_touch_hubei": "0",
                      "is_touch_virus": "0",
                      "is_health": "0",
                      "health_type": "string",
                      "health_check": "0",
                      "create_time": "2020-02-25 00:00:00",
                      "update_time": "2020-02-25 00:00:00",
                      "extended_filed1": "string",
                      "extended_filed2": "string",
                      "last_modify_time": "0"},

                     {"source": "0",
                      "pserson_name": "string",
                      "phone": "string",
                      "card_type": "0",
                      "card_no": "string",
                      "house_type": "0",
                      "recordAddres": "string",
                      "is_cd": "0",
                      "is_reback": "0",
                      "reback_time": "2020-02-25 00:00:00",
                      "reback_xzqhdm": "string",
                      "reback_plan": "string",

                      "reback_plan_xzqhdm": "string",
                      "is_touch_hubei": "0",
                      "is_touch_virus": "0",
                      "is_health": "0",
                      "health_type": "string",
                      "health_check": "0",
                      "create_time": "2020-02-25 00:00:00",
                      "update_time": "2020-02-25 00:00:00",
                      "extended_filed1": "string",
                      "extended_filed2": "string",
                      "last_modify_time": "0"}]
        for body in body_list:
            with self.client.post(loginUrl, data=body, headers=header, catch_response=True) as response:
                if response.status_code != 200:
                    response.failure("响应失败")

    @task(1)
    # 查询个人健康登记信息
    def queryInfo(self):
        loginUrl = "/gateway/api/1/report/queryInfo"
        hashUserCode = "e5089e403ce9873d8e9af3abd5cbde11929d2938c6bdaff6d4255b499877904b"
        personName = "string"
        with self.client.get(loginUrl + "?hashUserCode=" + hashUserCode + "&personName=" + personName,
                             catch_response=True) as response:
            if response.status_code != 200:
                response.failure("响应失败")

    # 查询个人健康登记信息（扫码场景）
    @task(1)
    def queryInfoByUserCode(self):
        loginUrl = "/gateway/api/1/report/queryInfoByUserCode"
        hashUserCode = "e5089e403ce9873d8e9af3abd5cbde11929d2938c6bdaff6d4255b499877904b"
        with self.client.get(loginUrl + "?hashUserCode=" + hashUserCode, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("响应失败")

    # 个人健康状态信息查询(查询三色码)
    @task(1)
    def queryUserHealthStatusInfo(self):
        loginUrl = "/gateway/api/1/report/queryUserHealthStatusInfo"
        hashUserCode = "e5089e403ce9873d8e9af3abd5cbde11929d2938c6bdaff6d4255b499877904b"
        personName = "string"
        with self.client.get(loginUrl + "?hashUserCode=" + hashUserCode + "&pserson_name=" + personName,
                             catch_response=True) as response:
            if response.status_code != 200:
                response.failure("响应失败")


class MyLocust(HttpUser):
    task_set = Query_Of_Tricolor_Code
    host = "http://172.24.59.68:8082"
    min_wait = 1000
    max_wait = 3000
