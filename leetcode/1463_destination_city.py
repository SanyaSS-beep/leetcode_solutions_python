"""
目标城市
"""
class Solution:
    def destCity(self, paths) -> str:
        # 根据终点站的含义，终点站不会出现在cityAi中，只会在cityBi中，遍历cityBi，返回不在cityAi中的城市，即为终点城市
        cityAi = []
        cityBi = []
        for path in paths:
            cityAi.append(path[0])
            cityBi.append(path[1])
        for i in cityBi:
            if i not in cityAi:
                return i