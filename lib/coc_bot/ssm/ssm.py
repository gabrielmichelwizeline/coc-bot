import boto3

ssm = boto3.client("ssm")


def get_parameter_by_name(parameter_name: str) -> str:
    try:
        parameter = ssm.get_parameter(Name=parameter_name)
        return parameter["Parameter"]["Value"]
    except ssm.exceptions.ParameterNotFound:
        return ""
