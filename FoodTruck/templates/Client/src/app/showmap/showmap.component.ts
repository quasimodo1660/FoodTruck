import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { HttpService } from '../http.service';
import { ShareButtons } from '@ngx-share/core';
import { faFacebookF,faTwitter,faGooglePlusG,faLinkedinIn } from '@fortawesome/free-brands-svg-icons'

@Component({
  selector: 'app-showmap',
  templateUrl: './showmap.component.html',
  styleUrls: ['./showmap.component.css']
})
export class ShowmapComponent implements OnInit {
  lat;
  lng;
  zoom: number = 15;
  id;
  lunchbox={};
  title: string = 'Pick up location';
  tags:any;
  reviews=[];
  // lat: number = 37.3;
  // lng: number = -121.9;
  fbIcon = faFacebookF;
  tweetIcon=faTwitter;
  gIcon = faGooglePlusG;
  lIcon = faLinkedinIn;
  

  constructor(
    private _httpService: HttpService, 
    private _route: ActivatedRoute, 
    private _router: Router,
    public share:ShareButtons) { }

  ngOnInit() {
    this.getLunchbox();
  }

  getLunchbox(){
    this._httpService.getLunbox(this._route.params['value'].id).subscribe(data=>{
        this.lunchbox=data;
        this.reviews=data['reviews'];
        console.log(this.reviews)
        this.lat=this.lunchbox['lat'];
        this.lng=this.lunchbox['lon'];
        this.tags=this.lunchbox['tags'];
        if(this.reviews.length!==0) 
          this.lunchbox['stars']=(this.reviews.reduce(function(x,y){return x+=y.score},0)/this.reviews.length).toFixed(2);
        else
          this.lunchbox['stars']=0;
      })
  };
  addLike(){
    this._httpService.addLike(this._route.params['value'].id).subscribe(data=>{
      if(data['succes'])
        this.getLunchbox()
    })
  }

}
