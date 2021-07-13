def __scrape_web(self):
    """
      Private method, scrapes the web to get the money line.
    """

    try:
        url = self.url.format(self.date, self.team_1, self.team_2)
        self.driver.get(url)

        winner_name_money_line = self.driver.find_elements_by_xpath(self.winner_name_money_line_xpath)[0].text
    except:
        try:
            url = self.url.format(self.date, self.team_2, self.team_1)
            self.driver.get(url)

            winner_name_money_line = self.driver.find_elements_by_xpath(self.winner_name_money_line_xpath)[0].text
        except:
            winner_name_money_line = None

    return winner_name_money_line


def get_pick(self):
    """
      Public method, get winner pick with moneyline.
    """

    winner_name_money_line = self.__scrape_web()

    if winner_name_money_line:
        winner_name_money_line_list = winner_name_money_line.split(" ")
        winner_name_money_line_list_last_idx = len(winner_name_money_line_list) - 1

        try:
            money_line = float(winner_name_money_line_list[winner_name_money_line_list_last_idx])
            team_name = " ".join(winner_name_money_line_list[:-1])

            return {team_name: money_line}
        except:
            return None
