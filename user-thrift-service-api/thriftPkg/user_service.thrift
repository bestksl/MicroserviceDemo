namespace java com.hobbymatcher.thrift.user

struct UserInfo{
    1:i32 id;
    2:string username,
    3:string password,
    4:string mobile,
    5:string email,
    6:string realName
}


service UserService{
    UserInfo getUserById(1:i32 id);

    UserInfo getUserByName(1:string username);

    void regiserUser(1:UserInfo userInfo)
}