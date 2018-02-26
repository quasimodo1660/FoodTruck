import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-showinfo',
  templateUrl: './showinfo.component.html',
  styleUrls: ['./showinfo.component.css']
})
export class ShowinfoComponent implements OnInit {

  constructor(
    private _route:ActivatedRoute
  ) { }

  ngOnInit() {
    console.log('showInfo got id '+this._route.params['value'].id)
  }

}
