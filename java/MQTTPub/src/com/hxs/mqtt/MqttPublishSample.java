package com.hxs.mqtt;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MqttPublishSample {

    /**
     * @param args
     */
    public static void main(String[] args) {
        String topic        = "test";
        String content      = "Message from MqttPublishSample";
        int qos             = 2;
        String broker       = "tcp://119.29.231.102:1883";
        String clientId     = "JavaSample";
        MemoryPersistence persistence = new MemoryPersistence();
        try {
            MqttClient sampleClient = new MqttClient(broker, clientId, persistence);
            MqttConnectOptions connOpts = new MqttConnectOptions();
            connOpts.setCleanSession(true);
            sampleClient.connect(connOpts);
            //获取文件信息
            String filePath = "/Users/apple/Downloads/Nightwish - Last Of The Wilds.mp3"; //指定文件路径  
            File file = new File(filePath); //创建文件对象  
            //把文件信息封装成FileInfo对象
            FileInfo fileInfo = new FileInfo(null,file.getName(),file.length(),0);
            String jsonFileStr = fileInfo.getJSONFromObj();
            MqttMessage message = new MqttMessage(jsonFileStr.getBytes());
            message.setQos(qos);
           // sampleClient.publish(topic, message);
            //开始读取文件
			FileInputStream fis = new  FileInputStream(file);
			byte[] buffer = new byte[102400]; ///每次读取1024个
		    int len;
		    int position = 0;
		     while((len = fis.read(buffer)) != -1){ 
		         fileInfo = new FileInfo(buffer,file.getName(),file.length(),position);
		         jsonFileStr = fileInfo.getJSONFromObj();
		         System.out.println(jsonFileStr);
		         message = new MqttMessage(jsonFileStr.getBytes());
		         message.setQos(qos);
		         sampleClient.publish(topic, message); 
		         position += len;
		         Arrays.fill(buffer,new Byte((byte) 0));//清空buffer
			     Thread.sleep(1000);
		     }
		     fis.close();
        } catch(MqttException me) {
            System.out.println("reason "+me.getReasonCode());
            System.out.println("msg "+me.getMessage());
            System.out.println("loc "+me.getLocalizedMessage());
            System.out.println("cause "+me.getCause());
            System.out.println("excep "+me);
            me.printStackTrace();
        }catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
}