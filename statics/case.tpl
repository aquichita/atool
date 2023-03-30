import allure


@allure.suite("suite")
@allure.epic("epic")
@allure.feature("feature")
@allure.story("story")
@allure.title("{{ case['name'] }} | Author")
def testXXX():
    """description"""
    {% for step in case['steps'] %}
    with allure.step("{{ step['序号'] }}.{{ step['角色']}}：{{ step['路径'] }} ({{ step['页面'] }})"):
        {%- for s in step[step['角色']] %}
        with allure.step("{{ step['序号'] }}.{{ s }}"):
            pass
        {%- endfor %}
    {% endfor %}
