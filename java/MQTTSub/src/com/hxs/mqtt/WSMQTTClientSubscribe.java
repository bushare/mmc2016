package com.hxs.mqtt;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URISyntaxException;

import org.fusesource.mqtt.client.BlockingConnection;
import org.fusesource.mqtt.client.MQTT;
import org.fusesource.mqtt.client.Message;
import org.fusesource.mqtt.client.QoS;
import org.fusesource.mqtt.client.Topic;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class WSMQTTClientSubscribe {
	
	private static final Logger LOG = LoggerFactory.getLogger(WSMQTTClientSubscribe.class);
	private final static String CONNECTION_STRING = "tcp://119.29.231.102:1883";
	private final static boolean CLEAN_START = true;
	private final static short KEEP_ALIVE = 30;//心跳30s
	private final static String CLIENT_ID = "mySub";
	public final static long RECONNECTION_ATTEMPT_MAX = 6;
	public final static long RECONNECTION_DELAY = 2000;
	public final static int SEND_BUFFER_SIZE = 2*1024*1024;//发送最大缓冲为2M
	
	public static void main(String[] args) {
		//创建MQTT对象
		MQTT mqtt = new MQTT();
		BlockingConnection conn = null;
		try {
			//设置mqtt broker的ip和port
			mqtt.setHost(CONNECTION_STRING);
			//连接前清空会话信息
			mqtt.setCleanSession(CLEAN_START);
			//设置重新连接的次数
			mqtt.setReconnectAttemptsMax(RECONNECTION_ATTEMPT_MAX);
			//设置重连的间隔时间
			mqtt.setReconnectDelay(RECONNECTION_DELAY);
			//设置心跳时间
			mqtt.setKeepAlive(KEEP_ALIVE);
			//设置缓冲的大小
			mqtt.setSendBufferSize(SEND_BUFFER_SIZE);
			mqtt.setClientId(CLIENT_ID);		
			//获取mqtt的连接对象BlockingConnection
			conn = mqtt.blockingConnection();
			//创建MQTT连接
			conn.connect();	
			//创建相关的MQTT的主题列表
			Topic[] topics = {new Topic("test",QoS.AT_LEAST_ONCE)};
            //订阅相关的主题信息
			byte[] qoses = conn.subscribe(topics);
			while(true){
				//接收订阅的消息内容
				Message msg = conn.receive();
				//获取订阅的消息内容
				byte[] payload = msg.getPayload();			
				// process the message then: 
				LOG.info("MQTTClient Message Topic=" + msg.getTopic() + " Content :" + new String(payload));
				//处理发来的json字符串
				if(dealJson(new String(payload))==0){	
					// 签收消息的回执                 
					msg.ack();	
					break;
				}	
			}
		} catch (URISyntaxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally{
			try {
				conn.disconnect();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
	
	}
	///处理收到消息的函数
	public static int dealJson(String json){
		System.out.println(json); //输出一下接收到的json串
		FileInfo fileInfo = new FileInfo(json);
		FileOutputStream fos = null;
		File file = new File("/Users/apple/upload",fileInfo.fileName); //生成文件的路径
		if(file.exists() && file.length() == fileInfo.fileLen){  // 文件已存在, length()即为文件大小, 文件不存在length()为0
		    System.out.println("文件已存在");
		     return 0;
	    }
	   try {
		   fos = new FileOutputStream(file, true);  // 文件存在就追加, 文件不存在则创建
		   byte[] buffer = Base64Utils.getFromBASE64(fileInfo.content);
		
		   fos.write(buffer, 0, buffer.length);
		   fos.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    return 1;	      
	}

}
