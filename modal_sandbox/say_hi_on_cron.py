import modal
import os
import time

stub = modal.Stub()


@stub.function(
    schedule=modal.Period(minutes=1), secret=modal.Secret.from_name("my-dummy-secret")
)
def say_hi():
    now = time.ctime()
    secret = os.environ.get("dummy-secret")
    print(f"Hello {os.environ.get('USER', 'Rodney')} at {now}")
    print(f"{secret=}")


if __name__ == "__main__":
    stub.deploy("say_hi")
