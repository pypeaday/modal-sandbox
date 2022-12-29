import modal
import os
import time

stub = modal.Stub()


@stub.function(schedule=modal.Period(minutes=1))
def say_hi():
    now = time.ctime()
    print(f"Hello {os.environ.get('USER', 'Rodney')} at {now}")


if __name__ == "__main__":
    stub.deploy("say_hi")
