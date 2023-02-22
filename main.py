# from prettytable import PrettyTable
# x = PrettyTable()
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])

# print(x)

# class User:#name of every class is firstletter is capital
#     #pass #for ignore the class and function
#     def __init__(self,user_id,username):#constructor
#         self.id=user_id
#         self.username=username
#         self.followers=0
#         self.following=0
#         print("new user created")

#     def follow(self,user):
#         user.followers+=1
#         self.following+=1


# user_1 = User("001","Angela")
# user_2 = User("002","Omkar")

# user_1.follow(user_2)

# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

class User:
    def __init__(self,user_id,username):
        self.user_id=user_id
        self.user_name=username
        self.follower=0
        self.following=0

    
    def follow(self,user):
        user.follower +=1
        self.following +=1

user_1=User("001","Omkar")
user_2=User("23","23")
user_1.follow(user_2)#user 1 startedd follwing user 2
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
# user_2.follow(user_1)
# print(user_1.follower)
# print(user_1.following)
# print(user_2.follower)
# print(user_2.following)
