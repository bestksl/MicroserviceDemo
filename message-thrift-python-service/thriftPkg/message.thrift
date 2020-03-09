namespace java com.hobbymatcher.thrift.message
namespace py message.api

service MessageService{

    bool sendMobileMessage(1:string mobile, 2:string messages);

    bool sendEmailMessage(1:string email, 2:string message);

}