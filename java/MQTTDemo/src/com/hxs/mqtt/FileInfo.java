package com.hxs.mqtt;

public class FileInfo {
	public String type; //D标志发送数据，客户端收到后往文件中追加数据 F标志要发送文件，客户端收到后建立新文件
	public String content ; //读取的文件内容，并把byte转化为base64字符串
	public String fileName ;//文件名字
	public long fileLen ; //文件长度
	public long position ; //该数据在文件中的位置 即已经发送的字节数
}
