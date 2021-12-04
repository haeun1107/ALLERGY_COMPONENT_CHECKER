from menu import Menu

class Show:

    # menu의 클래스인 Menu의 객체 생성
    menu = Menu()

    # consolEdit에 사용자가 입력한 성분이 포함된 모든 음식을 띄우기 위한 함수
    def showConsol(self, componentName): # 사용자가 입력한 값을 인자로 받음
        self.Food_Name = [] # 사용자가 입력한 성분이 해당되는 음식 이름을 담는 리스트
        self.Food_Components = [] #사용자가 입력한 성분이 해당되는 음식에 포함되는 다른 성분들을 담는 리스트
        self.nonFood_Name = [] # 사용자가 입력한 성분이 해당되지 않는 음식 이름을 담는 리스트
        self.nonFood_Components = [] #사용자가 입력한 성분이 해당되지 않는 음식에 포함되는 다른 성분들을 담는 리스트

        for i in range(len(self.menu.food_value)):
            for j in range(len(self.menu.food_value[i])):
                if componentName == self.menu.food_value[i][j]:
                    self.Food_Name.append(self.menu.food_key[i])
                    self.Food_Components.append(self.menu.food_value[i])

        for r in self.menu.food_key:
            if r not in self.Food_Name:
                self.nonFood_Name.append(r)

        for s in self.menu.food_value:
            if s not in self.Food_Components:
                self.nonFood_Components.append(s)

        return self.Food_Name, self.Food_Components, self.nonFood_Name, self.nonFood_Components