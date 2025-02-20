from dotenv import load_dotenv
from humanlayer import HumanLayer
from humanlayer.core.models import HumanContactSpec

load_dotenv()

hl = HumanLayer(
    verbose=True,
    run_id="fetch-approval-example",
)

hl.create_human_contact(
    spec=HumanContactSpec(
        msg="test-msg",
        state={"test-key": "test-value"},
    ),
)
