import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css']
})
export class ReviewComponent implements OnInit {

  constructor(
    private _route:ActivatedRoute
  ) { }

  ngOnInit() {
    console.log('review got id '+this._route.params['value'].id)
  }

}
