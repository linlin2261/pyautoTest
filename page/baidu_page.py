from poium import Page, NewPageElement ,page_objects,PageElement,PageElements


class BaiduPage(Page):
    search_input = NewPageElement(id_="kw", describe="搜索框")
    search_button = NewPageElement(id_="su", describe="搜索按钮")
    settings = PageElements(name='tj_settingicon', describe="设置下拉框")
    search_setting = NewPageElement(css=".setpref", describe="搜索设置选项")
    save_setting = NewPageElement(css=".prefpanelgo", describe="保存设置")
    #search_result=PageElements(xpath="//div/h3/a",describe="搜索结果")