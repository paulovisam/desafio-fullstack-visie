import { HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EnvironmentService {
    private production: boolean = true;

    constructor(
    ) { }

    public getEnvironment() {
      if(this.production) {
        return "https://144.22.220.135:8000/api/v1";
      } else {
        return "http://192.168.100.126:8000/api/v1";
      }
    }

    public getOptions() {
      const httpOptions = {
        headers: new HttpHeaders({
          'Content-Type':  'application/json'
        })
      };
      return httpOptions;
    }

}