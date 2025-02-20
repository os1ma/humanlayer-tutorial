from dotenv import load_dotenv
from humanlayer import HumanLayer
from humanlayer.core.models import FunctionCallSpec

load_dotenv()

hl = HumanLayer(
    verbose=True,
    run_id="fetch-approval-example",
)

resp = hl.fetch_approval(
    FunctionCallSpec(
        fn="my_func",
        kwargs={"x": 1, "y": 2},
    ),
).as_completed()

print(type(resp))
print(resp)
