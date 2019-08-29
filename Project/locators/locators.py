
class Locators:
    # steam page

    move_to_games: str = "//div[@id='genre_tab']//a[@class='pulldown_desktop']"
    actions_click: str = "//div[@class='responsive_page_template_content']//a[16]"
    actions_click_en: str = "//div[@class='responsive_page_template_content']//a[7]"
    check_language_en: str = "//div[@id='genre_tab']//a[@class='pulldown_desktop' and contains(text(),'Games')]"
    check_language_ru: str = "//div[@id='genre_tab']//a[@class='pulldown_desktop' and contains(text(),'Игры')]"

    # actions page

    top_sellers = "//div[@id='tab_select_TopSellers']"
    game_discount: str = "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%')]"
    game_final_prise: str = "//div[@class='discount_pct' and contains(text(),'%s')]/.."
    click_max_discount: str = "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%s')]"

    # birth time check
    age_choose: str = "ageYear"
    ageMonth: str = "ageMonth"
    open_page_button: str = "//div[@class='main_content_ctn']//a[@class='btnv6_blue_hoverfade btn_medium']//span[1]"

    # my game
    game1_prise: str = "//div[@class='discount_final_price']"
    game1_discount: str = "//div[contains(@class,'discount_pct')]/.."
    game1_base_discount: str = "//div[@class='bundle_base_discount']"
    click_install_button: str = "//a[@class='header_installsteam_btn_content']"

    # install page

    stem_install_click: str = "//a[@class='about_install_steam_link']"
