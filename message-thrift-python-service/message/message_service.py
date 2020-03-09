# coding=utf-8
from message.api import MessageService
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'imoocd@163.com'
authCode = 'aA111111'


class MessageServiceHandler:
    def sendMobileMessage(self, mobile, messages):
        print "send Mobile Message: ", messages, " to ", mobile
        return True

    def sendEmailMessage(self, email, message):
        print "send Email Message: email:", email, "message: ", message
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj['From'] = sender
        messageObj['To'] = email
        messageObj['Subject'] = Header('卡萨拉你好', 'utf-8')
        try:
            smtpObj = smtplib.SMTP('smtp.163.com')
            smtpObj.login(sender, authCode)
            smtpObj.sendmail(sender, [email], messageObj.as_string())
        except smtplib.SMTPException, ex:
            print "send mail failed!"
            print ex
        print "send mail success"
        return True


if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", "9090")
    t_factory = TTransport.TFramedTransportFactory()
    p_factory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, transport, p_factory)
    print "python thrift server start"
    server.serve()
    print "python thrift server exit"
