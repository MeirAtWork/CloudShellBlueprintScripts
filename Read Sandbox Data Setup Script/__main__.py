from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.api.cloudshell_api import SandboxDataKeyValue


def read_keys(sandbox, components=None):
    """
    orchestration stage functions MUST have (sandbox, components) signature
    :param Sandbox sandbox:
    :return:
    """
    api = sandbox.automation_api
    res_id = sandbox.id

    data = api.GetSandboxData(res_id)

    for keyValue in data.SandboxDataKeyValues:
        print(keyValue.Key + " :: " + keyValue.Value)


sandbox = Sandbox()
DefaultSetupWorkflow().register(sandbox)
sandbox.workflow.on_configuration_ended(read_keys, None)
sandbox.execute_setup()