package com.hobbymatcher.user.service;

import com.hobbymatcher.thrift.user.UserInfo;
import com.hobbymatcher.thrift.user.UserService;
import org.apache.thrift.TException;

/**
 * @author HaoxuanLi
 * @version 1.0
 * @date 2020/3/9 16:30
 */
public class UserServiceImpl implements UserService.Iface {

    @Override
    public UserInfo getUserById(int id) throws TException {
        return null;
    }

    @Override
    public UserInfo getUserByName(String username) throws TException {
        return null;
    }

    @Override
    public void regiserUser(UserInfo userInfo) throws TException {

    }
}
