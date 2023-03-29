import allure


@allure.suite("套件")
@allure.epic("史诗")
@allure.feature("特性")
@allure.story("故事")
@allure.title("{{ case['name'] }} | 作者")
def test():
    """用例描述"""
    {% for step in case['steps'] %}
    with allure.step("{{ step['序号'] }}.{{ step['角色']}}：{{ step['路径'] }} ({{ step['页面'] }})"):
        {%- for s in step[step['角色']] %}
        with allure.step("{{ step['序号'] }}.{{ s }}"):
            pass
        {%- endfor %}
    {% endfor %}
