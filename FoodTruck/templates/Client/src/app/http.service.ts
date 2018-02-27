import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class HttpService {

  constructor(private _http: HttpClient) { }
  getLunbox(id){
    return this._http.get('http://192.168.1.113:8000/api/lunchbox/'+id)
  }
}
