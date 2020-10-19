from typing import List, Dict

import boto3


class SsmManager:
    def __init__(self, region_name: str):
        self.__ssm = boto3.client('ssm', region_name=region_name)
        self.__parameters = []
        self.__base_ssm_path = None

    @property
    def parameters(self) -> List[Dict[str, any]]:
        return [{
            'name': item['Name'].replace(f'{self.__base_ssm_path}/', ''),
            'value': item['Value']
        } for item in self.__parameters]

    def load_parameter(self, base_ssm_path: str) -> None:
        self.__base_ssm_path = base_ssm_path
        result = []
        next_token = None
        while True:
            dict_parameter = {
                'Path': base_ssm_path,
                'Recursive': True,
                'WithDecryption': True,
            }
            if next_token is not None:
                dict_parameter['NextToken'] = next_token
            response = self.__ssm.get_parameters_by_path(**dict_parameter)
            parameters = response['Parameters']
            result.extend(parameters)
            if 'NextToken' not in response:
                break
            next_token = response['NextToken']
        self.__parameters = result
