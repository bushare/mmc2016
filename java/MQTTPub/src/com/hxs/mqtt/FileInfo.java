package com.hxs.mqtt;

import com.google.gson.Gson;

public class FileInfo {
	public String content ; //读取的文件内容，并把byte转化为base64字符串
	public String fileName ;//文件名字
	public long fileLen ; //文件长度
	public long position ; //该数据在文件中的位置 即已经发送的字节数
	
	public FileInfo(byte[] content,String fileName,long fileLen,long position){
		this.content = Base64Utils.getBASE64(content);
		this.fileName = fileName;
		this.fileLen = fileLen;
		this.position = position;
	}
	//json串作为参数的构造函数
	public FileInfo(String jsonStr){
		Gson gson = new Gson();
		FileInfo fileInfo =  gson.fromJson(jsonStr, FileInfo.class);
		this.content = fileInfo.content;
		this.fileName = fileInfo.fileName;
		this.fileLen = fileInfo.fileLen;
		this.position = fileInfo.position;
	}
	//对象转json字符串
	public String getJSONFromObj(){
		Gson gson = new Gson();
		return gson.toJson(this);
	}
	//json字符串转对象
	public void getObjFromJSON(String jsonStr){
		Gson gson = new Gson();
		FileInfo fileInfo =  gson.fromJson(jsonStr, FileInfo.class);
		this.content = fileInfo.content;
		this.fileName = fileInfo.fileName;
		this.fileLen = fileInfo.fileLen;
		this.position = fileInfo.position;
	}
}
