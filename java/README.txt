1.把MQTTSub和MQTTPub导入到eclipse或者myeclipse中
  更改MqttPublishSample.java 和 WSMQTTClientSubscribe.java中发送文件和接收文件的路径。
  更改clientID 和 topic
2.传输的json串格式：
{
    content:“从文件中读取的byte数组，并通过base64转化为string,大小自己定义，我取的10240（10k）”, 
    fileName:”传输文件的名字”,
    fileLen: 传输文件的大小 long型,
    postion: 现在发送文件的位置，即已经发送的byte,long型
}
3.接收端接收到数据后 要把content里的数据按base64解密为byte数组，然后已追加的方式添加到fileName中。