from menu import Menu

class Show:

    menu = Menu()

    def showConsol(self, componentName):
        self.Food_Name = []
        self.Food_Components = []
        for i in range(len(self.menu.food_value)):
            for j in range(len(self.menu.food_value[i])):
                if componentName == self.menu.food_value[i][j]:
                    self.Food_Name.append(self.menu.food_key[i])
                    self.Food_Components.append(self.menu.food_value[i])
                    #self.Food_Name.append(( "검색한 성분이 해당되는 음식" + i + ":" + self.menu.food_key[i] + "\n" ))
                    #self.Food_Components.append(( "해당 음식의 다른 성분들" + i + ":" + self.menu.food_value[i] + "\n" ))
                else:
                    continue

        return self.Food_Name, self.Food_Components