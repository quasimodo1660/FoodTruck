import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { HttpService } from '../http.service';

@Component({
  selector: 'app-showmap',
  templateUrl: './showmap.component.html',
  styleUrls: ['./showmap.component.css']
})
export class ShowmapComponent implements OnInit {
  // lat;
  // lng;
  zoom: number = 15;
  id;
  lunchbox: any;
  title: string = 'Pick up location';
  lat: number = 37.3;
  lng: number = -121.9;
  

  constructor(
    private _httpService: HttpService, 
    private _route: ActivatedRoute, 
    private _router: Router) { }

  ngOnInit() {
    this.getLunchbox();
  }

  getLunchbox(){
    this._httpService.getLunbox(this._route.params['value'].id).subscribe(data=>{
        this.lunchbox=data;
        console.log(this.lunchbox)
        // this.lat=this.lunchbox.lat;
        // this.lng=this.lunchbox.lon;
      })
  };


}
