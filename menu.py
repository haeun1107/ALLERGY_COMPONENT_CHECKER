class Menu:

    def __init__(self):

        self.menu = [{"순두부찌개": ["두부", "양파", "애호박", "표고버섯", "대파", "청양고추", "홍고추"]},
                {"콩비지찌개": ["비지", "김치", "돼지고기", "마늘", "고추", "양파", "대파", "멸치액젓"]},
                {"고등어조림": ["고등어", "양파", "무", "감자", "대파", "고추"]},
                {"만두전골": ["고기만두", "김치만두", "배추", "청경채", "팽이버섯", "양파", "대파", "고추"]},
                {"공깃밥": ["쌀"]}]

        self.components_list = [] # 각 음식에 들어가는 모든 성분 담는 list
        self.food_key = [] # 음식 이름
        self.food_value = [] # 음식에 들어가는 성분

        # 한 곳에 담긴 음식 이름과 성분을 각각의 list로 바꾸어 줌
        for i in range(len(self.menu)):
            self.food_key += self.menu[i].keys()
            self.food_value += self.menu[i].values()

        # 모든 성분을 하나의 list에 담기 위함
        for j in range(len(self.food_value)):
            self.components_list += self.food_value[j]

        # 모든 성분을 하나의 list에 담은 후 set()을 이용한 중복 제거
        components_set = set(self.components_list)
        self.components_list = list(components_set)

        #사전순 정렬
        self.components_list.sort()