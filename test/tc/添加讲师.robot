*** Settings ***
Library    pylib.webLib
Suite Setup    open browser
*** Test Cases ***
添加讲师 - tc001
    login    zhangqingqin      1qaz@WSX
    addteacher


添加课件 - tc002
    addcourseware
