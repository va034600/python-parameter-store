from src.ssm_manager import SsmManager

print("start")

ssm_manager = SsmManager(region_name="ap-northeast-1")
ssm_manager.load_parameter(base_ssm_path="/aaa")
print(ssm_manager.parameters)
