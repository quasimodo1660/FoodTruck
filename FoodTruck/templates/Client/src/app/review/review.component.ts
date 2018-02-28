import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { HttpService } from '../http.service';

@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css']
})
export class ReviewComponent implements OnInit {
  lunchbox={};
  reviews=[];
  review:any;
  uID:any;
  lID=0;

  constructor(
    private _route:ActivatedRoute,
    private _httpService:HttpService
  ) { }

  ngOnInit() {
    this.getLunchbox();
    this.getUser();
    this.review={
      score:1,
      content:''
    } 
  }

  getLunchbox(){
    this._httpService.getLunbox(this._route.params['value'].id).subscribe(data=>{
      this.lunchbox=data;
      this.reviews=data['reviews'];
    })
  }
  getUser(){
    this._httpService.getUser().subscribe(data=>{
      this.uID=data['uID']
    })
  }
  onSubmit(){
    this.review.user=this.uID;
    this.lID=this._route.params['value'].id
    this.review.lunchbox= +this.lID
    console.log(this.review)
    this._httpService.addReview(this.review).subscribe(data=>{
      if(data['errors'])
        console.log(data['errors']);
      else
        this.getLunchbox()   
    })
  }
}
