def func1(self):
    try:
        url = self.url.format(self.date, self.Team1, self.team2)
        self.driver.get(url)
        winner_name_money_line = self.driver.find_elements_by_xpath(self.winXpath)[0].text
    except:
        try:
            url = self.url.format(self.date, self.Team2, self.team1)
            self.driver.get(url)

            WinMonLine = self.driver.find_elements_by_xpath(self.winner_name_money_line_xpath)[0].text
        except:
            WinMonLine = None
    return WinMonLine

def func2(self):
    winner_name_money_line = self.__scrape_web()

    if (self.func1()):
        winner_name_money_line_list = winner_name_money_line.split(" ")
        winner_name_money_line_list_idx = len(winner_name_money_line_list) - 1
        try:
            money_line = float(winner_name_money_line_list[winner_name_money_line_list_last_idx])
            team_name = " ".join(winner_name_money_line_list[:-1])
            return {team_name: money_line}
        except:
            return None