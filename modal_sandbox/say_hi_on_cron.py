import modal
import os
import time

stub = modal.Stub()

# my_image = modal.Image.debian_slim().pip_install(["pandas", "requests"])

my_image = modal.Image.from_dockerhub(
    tag="pypeaday/base-images:python-hello-world-main-3796875126-68"
).pip_install(["pandas", "requests"])

def get_url(package: str) -> str:
    return f"https://pypi.org/pypi/{package}/json"


def read_api_data(url, package: str):
    import pandas as pd
    import requests

    print(f"Pandas version in container: {pd.__version__}")
    # Make a request to the API
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:
        # Convert the response to JSON format
        data = response.json()

        print(f"Author of {package} is {data['info']['author']}")
    else:
        print(f"Got back {response.status_code}")


@stub.function(
    image=my_image,
    schedule=modal.Period(minutes=59),
)
def print_info():
    package = "pandas"
    # return PyPi API URL
    url = get_url(package)
    read_api_data(url, package)

    # BASE_VERSION wasn't found even though using my base iamge...
    print(f"BASE_VERSION = {os.environ.get('BASE_VERSION')}")


@stub.function(
    schedule=modal.Period(minutes=59), secret=modal.Secret.from_name("my-dummy-secret")
)
def say_hi():
    now = time.ctime()
    secret = os.environ.get("dummy-secret")
    print(f"Hello {os.environ.get('USER', 'Rodney')} at {now}")
    print(f"{secret=}")


if __name__ == "__main__":
    stub.deploy("say_hi")

    stub.deploy("print_info")
