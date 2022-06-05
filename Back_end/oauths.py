from flask import Blueprint, make_response, render_template, request, jsonify, redirect
from config import CLIENT_ID, REDIRECT_URI
from controller import Oauth
import pymongo
from model import UserModel, UserData

# from flask_jwt_extended import (
#     JWTManager, create_access_token, 
#     get_jwt_identity, jwt_required,
#     set_access_cookies, set_refresh_cookies, 
#     unset_jwt_cookies, create_refresh_token,
#     jwt_refresh_token_required,
# )
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)



blue_oauth=Blueprint("oauth", __name__, url_prefix="/oauth")



conn = pymongo.MongoClient('mongodb://user:checkmate12!@54.180.17.138:27017')
mydb = conn.CHECKMATE
User = mydb.User

# 버튼을 클릭하면 여기로
@blue_oauth.route("/url",methods=['GET'])
def oauth_url_api():
    """
    Kakao OAuth URL 가져오기
    """
    kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
       % (CLIENT_ID, REDIRECT_URI)
    #return jsonify(
    #    kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
    #    % (CLIENT_ID, REDIRECT_URI)
    #)
    return redirect(kakao_oauth_url)

# redirect된 주소 
@blue_oauth.route("",methods=['POST'])
def oauth_api():
    # 사용자로부터 authorization code를 인자로 받음
    code = str(request.args.get('code'))
   
    # 전달받은 authorization code를 통해서
    # access_token, refresh_token을 발급
    oauth = Oauth()
    auth_info = oauth.auth(code)
    
    # access_token을 이용해서, Kakao에서 사용자 식별 정보 획득
    user = oauth.userinfo("Bearer " + auth_info['access_token'])
    
    # 해당 식별 정보를 서비스 DB에 저장 (회원가입)
    user = UserData(user)
    
    # 만약 이미 있을 경우, 과정 스킵
    UserModel().upsert_user(user)


    # 사용자 식별 id를 바탕으로 서비스 전용 access_token, refresh_token 발급
     
    # resp = make_response(render_template('index2.html'))
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    #resp.set_cookie("logined", "true")
    #set_access_cookies(resp, access_token)
    #set_refresh_cookies(resp, refresh_token)

    return make_response(jsonify(SUCCESS=True),200)



