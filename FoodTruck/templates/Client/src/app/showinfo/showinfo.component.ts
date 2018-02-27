import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { HttpService } from '../http.service';
import { NgxGalleryOptions, NgxGalleryImage, NgxGalleryAnimation } from 'ngx-gallery';
import 'hammerjs';


@Component({
  selector: 'app-showinfo',
  templateUrl: './showinfo.component.html',
  styleUrls: ['./showinfo.component.css']
})
export class ShowinfoComponent implements OnInit {
  lunchbox={};
  images=[];
  galleryOptions: NgxGalleryOptions[];
  galleryImages: NgxGalleryImage[];

  constructor(
    private _route:ActivatedRoute,
    private _httpService:HttpService
  ) { }

  ngOnInit() {
    this.getLunchbox();
    this.galleryOptions = [
      {
          width: '100%', 
          height: '100%',
          thumbnailsColumns: 4,
          imageAnimation: NgxGalleryAnimation.Slide
      },
      // max-width 800
      {
          breakpoint: 800,
          width: '100%',
          // height: 'auto',
          imagePercent: 80,
          thumbnailsPercent: 20,
          thumbnailsMargin: 20,
          thumbnailMargin: 20
      },
      // max-width 400
      {
          breakpoint: 400,
          preview: false
      }
  ];
  
  this.galleryImages = [
      // {
      //     small: 'http://192.168.1.113:8000/media/Lunchbox/Emily/Beef%20Tofu/Lunchbox.jpg',
      //     medium: 'http://192.168.1.113:8000/media/Lunchbox/Emily/Beef%20Tofu/Lunchbox.jpg',
      //     big: 'http://192.168.1.113:8000/media/Lunchbox/Emily/Beef%20Tofu/Lunchbox.jpg'
      // },
      // {
      //     small: 'assets/2-small.jpg',
      //     medium: 'assets/2-medium.jpg',
      //     big: 'assets/2-big.jpg'
      // },
      // {
      //     small: 'assets/3-small.jpg',
      //     medium: 'assets/3-medium.jpg',
      //     big: 'assets/3-big.jpg'
      // }
  ];
  }
  getLunchbox(){
    this._httpService.getLunbox(this._route.params['value'].id).subscribe(data=>{
        this.lunchbox=data;
        this.images=data['images'];
        for(var j in this.images){
          this.galleryImages.push({
            small: 'http://192.168.1.113:8000/media/'+this.images[j],
            medium: 'http://192.168.1.113:8000/media/'+this.images[j],
            big: 'http://192.168.1.113:8000/media/'+this.images[j],
          })
        }
      console.log(this.galleryImages) 
    })
  };
}

