import { Component, OnInit } from '@angular/core';
import * as socketIO from 'socket.io-client';
import { Observable } from 'rxjs/Observable';
import { HttpService } from '../http.service';
import { trigger, transition, animate, style } from '@angular/animations';

@Component({
  selector: 'app-chatbox',
  templateUrl: './chatbox.component.html',
  styleUrls: ['./chatbox.component.css'],
  animations:[
    trigger('slideInOut', [
      transition(':enter', [
        style({transform: 'translateY(-100%)'}),
        animate('200ms ease-in', style({transform: 'translateY(0%)'}))
      ]),
      transition(':leave', [
        animate('200ms ease-in', style({transform: 'translateY(-100%)'}))
      ])
    ])
  ]
})
export class ChatboxComponent implements OnInit {
  private socket:any;
  users='You';
  message:any;
  messages=[];
  name='';
  visible=false;
  nm=0;

  constructor(private _httpService:HttpService) { 
    this.socket = socketIO('http://localhost:6789');
    this.message='';
  }

  ngOnInit() {
    this.getUser();
    this.socket.on('my_full_broadcast_event',function(data){
      if(data.count>1)  
        this.users=data.count+' users';
      else
        this.users='You';
     }.bind(this));
    this.socket.on('my_broadcast_event',function(data){
      this.messages.push({me:false,content:data.message});
      this.nm+=1;
    }.bind(this));
     
  }
  newMessage(){
    this.socket.emit('newMessage',{
      username:this.name[0].toUpperCase(),
      message:this.message
    },)
    this.messages.push({me:true,content:this.message,name:this.name[0].toUpperCase()});
    this.message='';
  }
  getUser(){
    this._httpService.getUser().subscribe(data=>{
      this.name=data['username'];
    })
  }
  showChat(){
    if(!this.visible){
      this.visible=true;
      this.nm=0;
    }  
    else{
      this.visible=false;
      this.nm=0;
    }
      
  }
}
