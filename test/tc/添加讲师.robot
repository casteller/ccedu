*** Settings ***
#Library    pylib.studyLib
Library   pylib.webLib
Suite Setup   open browser
Suite Teardown   close browser
*** Test Cases ***
#添加讲师 - tc001
#    get_cookie
#    addteacher  马云  阿里  阿里巴巴  总裁

添加讲师 - tc002
    login   zhangqingqin    tfwsdx@2019
    changeback
    addteacher


