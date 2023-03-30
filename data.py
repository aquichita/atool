from pathlib import Path

"""
Allure报告数据，此处使用静态文件，生产环境使用实时报告获取.
# JENKINS_JOB_URL = "http://XXX/job"
# basic = HTTPBasicAuth("admin", "XXX")
"""
examples = Path.cwd().joinpath("examples")
