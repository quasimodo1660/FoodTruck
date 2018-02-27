import { Component, OnInit } from '@angular/core';
import * as socketIO from 'socket.io-client';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-chatbox',
  templateUrl: './chatbox.component.html',
  styleUrls: ['./chatbox.component.css']
})
export class ChatboxComponent implements OnInit {
  private socket:any;
  users='You';
  message:any;
  messages=[];
  

  constructor() { 
    this.socket = socketIO('http://192.168.1.113:6789');
    this.message='';
  }

  ngOnInit() {
    this.socket.on('my_full_broadcast_event',function(data){
      if(data.count>1)  
        this.users=data.count+' users';
      else
        this.users='You';
     }.bind(this));
    this.socket.on('my_broadcast_event',function(data){
      this.messages.push({me:false,content:data.message})
    }.bind(this));
     
  }
  newMessage(){
    this.socket.emit('newMessage',{
      message:this.message
    },)
    this.messages.push({me:true,content:this.message});
    this.message='';
  }
}
