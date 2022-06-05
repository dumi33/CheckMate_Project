import pymongo



class UserModel:
    
    def __init__(self):
        conn = pymongo.MongoClient('mongodb://user:checkmate12!@54.180.17.138:27017')   
        mydb = conn.CHECKMATE
        User = mydb.User

    #  유저 생성 
    def upsert_user(self, user):
        conn = pymongo.MongoClient('mongodb://user:checkmate12!@54.180.17.138:27017')
        mydb = conn.CHECKMATE
        User = mydb.User
        docs = User.find({'id':{'$eq' : user.id}})
        if len(list(docs)) == 0: # 이미 생성한 유저가 아니라면 
            User.insert_one(user.serialize())

    
    # def get_user(self, user_id):
    #     user = self.db.search(Query().id == user_id)
    #     return UserData.deserialize(user[0])

    # def remove_user(self, user_id):
    #     self.db.remove(Query().id == user_id)

class UserData:
    
    def __init__(self, user=None):
        if user:
            user_info = user['kakao_account']['profile']
            self.id = user['id']
            self.nickname = user_info['nickname']
            self.profile = user_info['profile_image_url'] 
            self.thumbnail = user_info['thumbnail_image_url']
        else:
            self.id = None
            self.nickname = None
            self.profile = None
            self.thumbnail = None

    def __str__(self):
        return "<UserData>(id:%s, nickname:%s)" \
                % (self.id, self.nickname)

    def serialize(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "profile": self.profile,
            "thumbnail": self.thumbnail
        }

    @staticmethod
    def deserialize(user_data):
        user = UserData()
        user.id = user_data['id']
        user.nickname = user_data['nickname']
        user.profile = user_data['profile']
        user.thumbnail = user_data['thumbnail']
        return user