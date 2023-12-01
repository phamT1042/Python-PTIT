class Team:
    __cnt = 1
    def __init__(self, tenTeam, tenTruong):
        self.__maTeam = 'Team{:02d}'.format(Team.__cnt)
        Team.__cnt += 1
        self.__tenTeam = tenTeam
        self.__tenTruong = tenTruong

    def get_maTeam(self):
        return self.__maTeam
    
    def get_tenTeam(self):
        return self.__tenTeam
    
    def get_tenTruong(self):
        return self.__tenTruong

class ThiSinh:
    __cnt = 1
    def __init__(self, tenTS, maTeam):
        self.__maTS = 'C{:03d}'.format(ThiSinh.__cnt)
        ThiSinh.__cnt += 1
        self.__tenTS = tenTS
        self.__maTeam = maTeam

    def get_maTeam(self):
        return self.__maTeam

    def __str__(self, tenTeam, tenTruong):
        return '{} {} {} {}'.format(self.__maTS, self.__tenTS, tenTeam, tenTruong)

    def __lt__(self, other):
        return self.__tenTS < other.__tenTS

n = int(input())
teams = []
for i in range(n):
    teams.append(Team(input(), input()))  

m = int(input())
tss = []
for i in range(m):
    tss.append(ThiSinh(input(), input()))

tss.sort()
for ts in tss:
    for team in teams:
        if team.get_maTeam() == ts.get_maTeam():
            print(ts.__str__(team.get_tenTeam(), team.get_tenTruong()))  
