
from kubernetes import client, config

def main():
    aToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjMwNjM2MzQxOGVjNTEwNTA2NDUyYmNjNzVmYTAyYzE1MzJlYTY2ZmQifQ.eyJpc3MiOiJodHRwczovL2RleC5kZXguc3ZjOjMyMzg4Iiwic3ViIjoiQ2lOamJqMXFZVzVsTEc5MVBWQmxiM0JzWlN4a1l6MWxlR0Z0Y0d4bExHUmpQVzl5WnhJRWJHUmhjQSIsImF1ZCI6ImV4YW1wbGUtYXBwIiwiZXhwIjoxNjk2ODA2NDAzLCJpYXQiOjE2OTY3MjAwMDMsImF0X2hhc2giOiJwaG9qSURMSWhvWkp6M1Y0UzVjZVBBIiwiY19oYXNoIjoiS0J0WEZ5V2UyM21RenBnS2oyMVhJZyIsImVtYWlsIjoiamFuZWRvZUBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiamFuZSJ9.F4hsDcjOcXnmwWN4Lq6OkUexHWq6EaC0N4HATaH6kVA9kjlVuqwngZYD68babvWNq2dIP5hukvJdPuwXf1pzGyC1VeK-QFmyV32A2QEKOWUsfHguU0iOAtN0Q0wC-bthwal-HPGlaOaNnbSkPLJdsz_PLqC4cPbJAEkTm2zT4hWnfOhw8UErpRe1i4c6RPlyFU0qoikrDA2pinSb7RtIU5LT4QszvZ_eGLkiUTzFaImWsQBxic3nhqPfu6mEY3jO1erh1TYP7evFsznBH1zgpJGDICYPRgPnD0N6ZkXSo35jvKj3x3j3xXtrq2aFkheOAUlJE3J-rT1UcK4BacVK4w"
    aConfiguration = client.Configuration()
    aConfiguration.host = "https://127.0.0.1:16443"
    aConfiguration.verify_ssl = False
    aConfiguration.api_key = {"authorization": "Bearer " + aToken}
    aApiClient = client.ApiClient(aConfiguration)
    v1 = client.CoreV1Api(aApiClient)
    pod_list = v1.list_namespaced_pod("dex")
    for pod in pod_list.items:
        print("%s\t%s\t%s" % (pod.metadata.name,
                              pod.status.phase,
                              pod.status.pod_ip))

if __name__ == '__main__':
    main()